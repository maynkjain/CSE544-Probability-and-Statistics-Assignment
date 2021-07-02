"""
Created on Mon Apr 19 20:43:09 2021

@author: mayankjain
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import copy

def calculate_ecdf(x):
    n = len(x)
    x.sort()
    y = []
    yi = 0
    
    for i in x:
        yi += 1/n
        y.append(yi)
    
    return (x, y)

def plot_and_find_diff(male_data, female_data):
    male_age, male_cdf = calculate_ecdf(male_data)
    female_age, female_cdf = calculate_ecdf(female_data)

    cols = dict()
    cols["male_minus"] = 0;
    cols["male_plus"] = 0;
    cols["female_minus"] = 0;
    cols["female_plus"] = 0;

    table = []

    j = 0

    mx_diff = 0
    index = 0
    for i in range(len(male_data)):
        col_temp = copy.copy(cols)
        if (i == 0):
            col_temp["male_minus"] = 0
        else:
            col_temp["male_minus"] = table[i-1]["male_plus"]
 
        col_temp["male_plus"] = male_cdf[i]

        while(j<len(female_age) and female_age[j] < male_age[i]):
            j+=1
        
        if j != len(female_age):
            col_temp["female_minus"] = female_cdf[j-1]

            if (female_age[j] == male_age[i]):
                col_temp["female_plus"] = female_cdf[j];
            else:
                col_temp["female_plus"] = female_cdf[j-1];
        else:
            col_temp["female_minus"] = 0
            col_temp["female_plus"] = 0

        diff1 = abs(col_temp["male_minus"] - col_temp["female_minus"])
        diff2 = abs(col_temp["male_plus"] - col_temp["female_plus"])

        diff = max(diff1, diff2)
        if (mx_diff < diff):
            mx_diff = diff
            index = i

        table.append(col_temp)

    plt.grid(True)
    plt.step(male_age, male_cdf, where="post", label = "Male")
    plt.step(female_age, female_cdf, where="post", label = "Female")
    plt.xlabel("Age")
    plt.ylabel("eCDF")
    plt.legend(loc="upper left")
    title='eCDF with %d samples (male). Sample mean = %.2f.' % (len(male_age), np.mean(male_age))
    plt.title(title)

    plt.annotate('Max diff= ' + str(mx_diff), 
            xy=(male_age[index], mx_diff), 
            xytext=(index, 0.4), 
            arrowprops = dict(facecolor='green'))

    return mx_diff



data = pd.read_csv('data_q4_2.csv')

row,col = data.shape
male_age_data = []
female_age_data = []
for index, row in data.iterrows():
    if(row['gender'] == "Male"):
        male_age_data.append(row['age'])
    else:
        female_age_data.append(row['age'])

len_male_data = len(male_age_data)
len_female_data = len(female_age_data)

mxdiff = plot_and_find_diff(male_age_data, female_age_data)
print("Max Diff is: ", mxdiff)
plt.show()