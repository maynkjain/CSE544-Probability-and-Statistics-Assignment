#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 17:57:00 2021

@author: mayankjain
"""
import pandas as pd
import numpy as np
import random


def getp_val(glucose_data,len_stroke_data,observed_T,num_permutation):
    
    count = 0
    trials = 0
    
    while trials <  num_permutation:
        temp_data = np.array(glucose_data)
        np.random.shuffle((temp_data))
      
        d1 = temp_data[0:len_stroke_data]
        d2 = temp_data[len_stroke_data:]
        
        #print("d1 length", len(d1))
        #print("d2 length", len(d2))
        
        mean_d1 = np.mean(d1)
        mean_d2 = np.mean(d2)
        
        mean_diff = abs(mean_d1 - mean_d2)
        
        if mean_diff > observed_T:
            count+=1
        
        trials+=1
    
    p_val = count/num_permutation
    return p_val
 

   
data = pd.read_csv('data_q4_1.csv')

row,col = data.shape

stroke_data = []
no_stroke_data = []
for index, row in data.iterrows():
    if(row['stroke'] == 1):
        stroke_data.append(row['avg_glucose_level'])
    else:
        no_stroke_data.append(row['avg_glucose_level'])
   
# print("Glucose level of Stroke patients: ")      
# print(stroke_data)
# print("Glucose level of Non Stroke patients: ")
# print(no_stroke_data)

len_stroke_data = len(stroke_data)
len_no_stroke_data = len(no_stroke_data)

#print("len_stroke_data: ", len_stroke_data, " len_no_stroke_data: ", len_no_stroke_data)

mean_of_stroke_data = np.mean(stroke_data)

mean_of_non_stroke_data = np.mean(no_stroke_data)

#print("mean of stroke data: " , mean_of_stroke_data)
#print("mean of non stroke data: " , mean_of_non_stroke_data)

observed_T = abs(mean_of_stroke_data - mean_of_non_stroke_data)

print("observed_T= ",observed_T)
print("alpha = ",0.05)

glucose_data = np.concatenate((stroke_data, no_stroke_data))

p_val = getp_val(glucose_data,len_stroke_data,observed_T,200)
print("For n = 200 random permutations, p_value: ", p_val)
print("Therefore, NULL hypothesis for ",200, "permutations can be rejected as p-value is less than alpha")

p_val = getp_val(glucose_data,len_stroke_data,observed_T,1000)
print("For n = 1000 random permutations, p_value: ", p_val)
print("Therefore, NULL hypothesis for ",1000, "permutations can be rejected as p-value is less than alpha")

 