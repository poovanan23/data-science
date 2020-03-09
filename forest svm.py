# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:16:41 2020

@author: POOVAYUVA
"""

import pandas as pd
import numpy as np

forest = pd.read_csv(r"C:\Users\POOVAYUVA\Desktop\EXCELR ASSIGN\SVM ASSIGN\forestfires.csv")

colnames = forest.columns

string_columns=['month', 'day', 'FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind',
       'rain', 'area', 'dayfri', 'daymon', 'daysat', 'daysun', 'daythu',
       'daytue', 'daywed', 'monthapr', 'monthaug', 'monthdec', 'monthfeb',
       'monthjan', 'monthjul', 'monthjun', 'monthmar', 'monthmay', 'monthnov',
       'monthoct', 'monthsep', 'size_category']

from sklearn import preprocessing
number = preprocessing.LabelEncoder()
for i in string_columns:
        forest[i] = number.fit_transform(forest[i])


from sklearn.model_selection import train_test_split

x=forest.drop("size_category",axis=1)
y=forest["size_category"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=1)

        

from sklearn.svm import SVC

from sklearn.metrics import confusion_matrix


model_linear = SVC(kernel = "linear")
model_linear.fit(x_train,y_train)
pred_test_linear = model_linear.predict(x_test)

np.mean(pred_test_linear==y_test) # Accuracy = 98.71

# Kernel = poly
model_poly = SVC(kernel = "poly")
model_poly.fit(x_train,y_train)
pred_test_poly = model_poly.predict(x_test)

np.mean(pred_test_poly==y_test) # Accuracy = 99.35

# kernel = rbf
model_rbf = SVC(kernel = "rbf")
model_rbf.fit(x_train,y_train)
pred_test_rbf = model_rbf.predict(x_test)

np.mean(pred_test_rbf==y_test) # Accuracy = 75.0
