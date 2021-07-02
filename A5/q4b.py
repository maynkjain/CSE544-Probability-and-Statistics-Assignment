#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 20:25:40 2021

@author: mayankjain
"""

import pandas as pd
import numpy as np
import random
random.seed(10)

def getp_val(glucose_data,len_stroke_data,observed_T,num_permutation):

    count = 0
    trials = 0
    
    while trials <  num_permutation:
        temp_data = np.array(glucose_data)
        random.shuffle((temp_data))
        
        d1 = temp_data[0:len_stroke_data]
        d2 = temp_data[len_stroke_data:]
        
        
        mean_d1 = np.mean(d1)
        mean_d2 = np.mean(d2)
        
        mean_diff = abs(mean_d1 - mean_d2)
        
        if mean_diff > observed_T:
            count+=1
        
        trials+=1
    
    p_val = count/num_permutation
    return p_val
 

   
data = pd.read_csv('data_q4_2.csv')

#print(data.shape)
row,col = data.shape
#print(row)
#print(col)
male_age_data = []
female_age_data = []
for index, row in data.iterrows():
    if(row['gender'] == "Male"):
        male_age_data.append(row['age'])
    else:
        female_age_data.append(row['age'])
   

len_male_data = len(male_age_data)
len_female_data = len(female_age_data)

#print("len_male_data: ", len_male_data, " len_female_data: ", len_female_data)

mean_of_male_data = np.mean(male_age_data)

mean_of_female_data = np.mean(female_age_data)

print("mean of male age data: " , mean_of_male_data)
print("mean of female age data: " , mean_of_female_data)

observed_T = abs(mean_of_male_data - mean_of_female_data)

print("observed_T= ",observed_T)
print("alpha = ",0.05)

age_data = np.concatenate((male_age_data, female_age_data))

p_val = getp_val(age_data,len_male_data,observed_T,1000)
print("For n = 1000 random permutations, p_value: ", p_val)
print("Therefore, NULL hypothesis for ",1000, "permutations can be accepted as p-value is more than alpha")




 