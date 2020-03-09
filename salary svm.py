# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:40:00 2020

@author: POOVAYUVA
"""

import pandas as pd
import numpy as np

salary_train = pd.read_csv(r"C:\Users\POOVAYUVA\Desktop\EXCELR ASSIGN\NAIVE\SalaryData_Train.csv")
salary_test = pd.read_csv(r"C:\Users\POOVAYUVA\Desktop\EXCELR ASSIGN\NAIVE\SalaryData_Test.csv")
string_columns=["workclass","education","maritalstatus","occupation","relationship","race","sex","native"]

from sklearn import preprocessing
number = preprocessing.LabelEncoder()
for i in string_columns:
    salary_train[i] = number.fit_transform(salary_train[i])
    salary_test[i] = number.fit_transform(salary_test[i])
    
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


colnames = salary_train.columns
len(colnames[0:13])
trainX = salary_train[colnames[0:13]]
trainY = salary_train[colnames[13]]
testX  = salary_test[colnames[0:13]]
testY  = salary_test[colnames[13]]


# Create SVM classification object 
# 'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'

# kernel = linear
from sklearn.svm import SVC

help(SVC)

model_linear = SVC(kernel = "linear")
model_linear.fit(trainX,trainY)
pred_test_linear = model_linear.predict(testX)

np.mean(pred_test_linear==testY) # Accuracy = 85.233

# Kernel = poly
model_poly = SVC(kernel = "poly")
model_poly.fit(trainY,trainY)
pred_test_poly = model_poly.predict(testX)

np.mean(pred_test_poly==testY) # Accuracy = 94.499

# kernel = rbf
model_rbf = SVC(kernel = "rbf")
model_rbf.fit(trainX,trainY)
pred_test_rbf = model_rbf.predict(testX)

np.mean(pred_test_rbf==testY) # Accuracy = 97.016



