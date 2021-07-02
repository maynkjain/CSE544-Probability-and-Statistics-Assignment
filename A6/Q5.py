#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 15:42:26 2021

@author: mayankjain
"""

import pandas as pd
import numpy as np

def calculate(y_variable,features):
    
    y_mat_train = pd.read_csv('q5.csv',usecols = y_variable).head(400)
    
    # print("y_mat_train: ",y_mat_train.shape)
    
    x_mat_train = pd.read_csv('q5.csv',usecols = features).head(400)
    x_mat_train_transpose = x_mat_train.T
    
    #print(x_mat_train.shape)
    #print("x_mat_train_transpose.shape: ",x_mat_train_transpose.shape)
    
    product_of_X_and_X_transpose = np.matmul(x_mat_train_transpose.values,x_mat_train.values)
    #print(product_of_X_and_X_transpose.shape)
    
    df_inv = np.linalg.inv(product_of_X_and_X_transpose)
    
    #print(df_inv)
    
    invmulx_transpose = np.matmul(df_inv,x_mat_train_transpose.values)
    
    coeff = np.matmul(invmulx_transpose,y_mat_train.values)
    
    print("coeff: ",coeff)
    
    y_mat_test = pd.read_csv('q5.csv',usecols = y_variable).tail(100)
    x_mat_test = pd.read_csv('q5.csv',usecols = features).tail(100)
    
    y_estimated_test = x_mat_test.dot(coeff)
    
    #print(y_estimated_test)

    error = abs(y_mat_test.values - y_estimated_test)
    
    #print("error : ",error)
    
    error_trans = error.T
    
    sse = error_trans.dot(error)
    
    print ("sse: ",sse.values)



y_variable = ['Chance of Admit']
features_a = ['GRE Score','TOEFL Score','University Rating','SOP','LOR','GPA','Research']
print("Part A")
calculate(y_variable,features_a)

features_b = ['TOEFL Score','SOP','LOR']
print("Part B")
calculate(y_variable,features_b)

features_c = ['GRE Score','GPA']
print("Part C")
calculate(y_variable,features_c)
