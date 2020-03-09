# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:19:20 2020

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
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


colnames = salary_train.columns
len(colnames[0:13])
trainX = salary_train[colnames[0:13]]
trainY = salary_train[colnames[13]]
testX  = salary_test[colnames[0:13]]
testY  = salary_test[colnames[13]]

sgnb = GaussianNB()
smnb = MultinomialNB()
spred_gnb = sgnb.fit(trainX,trainY).predict(testX)
confusion_matrix(testY,spred_gnb)
print ("Accuracy",(10759+1209)/(10759+601+2491+1209)) # 0.79468%

spred_mnb = smnb.fit(trainX,trainY).predict(testX)
confusion_matrix(testY,spred_mnb)
print("Accuracy",(10891+780)/(10891+780+2920+780))  # 75%
