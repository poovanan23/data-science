# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:24:29 2020

@author: POOVAYUVA
"""

import pandas as pd
import numpy as np
# Reading the fraudcheckData #################
fraud = pd.read_csv(r"C:\Users\POOVAYUVA\Desktop\rfassign\Fraud_check.csv")
fraud.head()
fraud.columns
fraud = fraud.iloc[:,[2,0,1,3,4,5]]
def clear(x):
    if x<=30000:
      return "RISKY"
    else:
        return "GOOD"
fraud['Taxable.Income']=fraud['Taxable.Income'].apply(clear)
def clear(x1):
    if x1=="YES":
        return 1
    else:
        return 0
fraud['Urban']=fraud['Urban'].apply(clear)

def clear(x2):
    if x2=="YES":
        return 1
    else:
        return 0
fraud['Undergrad']=fraud['Undergrad'].apply(clear)

def clear(x3):
    if x3=="Single":
      return 0
    elif x3=="Married":
       return 1
    else:
        return 2
fraud['Marital.Status']=fraud['Marital.Status'].apply(clear)

        
fraud.head()

colnames = list(fraud.columns)

predictors = colnames[1:5]
target = colnames[0]


X = fraud[predictors]
Y = fraud[target]

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_jobs=3,oob_score=True,n_estimators=15,criterion="entropy")
# n_estimators -> Number of trees ( you can increase for better accuracy)
# n_jobs -> Parallelization of the computing and signifies the number of jobs 
# running parallel for both fit and predict
# oob_score = True means model has done out of box sampling to make predictions

np.shape(fraud) # 600,6 => Shape 

#### Attributes that comes along with RandomForest function
rf.fit(X,Y) # Fitting RandomForestClassifier model from sklearn.ensemble 
rf.estimators_ # 
rf.classes_ # class labels (output)
rf.n_classes_ # Number of levels in class labels 
rf.n_features_  # Number of input features in model 4here.

rf.n_outputs_ # Number of outputs when fit performed

rf.oob_score_  # 0.72333
rf.predict(X)
##############################

fraud['rf_pred'] = rf.predict(X)
cols = ['rf_pred','Taxable.Income']
fraud[cols].head()
fraud["Taxable.Income"]

from sklearn.metrics import confusion_matrix
confusion_matrix(fraud['Taxable.Income'],fraud['rf_pred']) # Confusion matrix

pd.crosstab(fraud['Taxable.Income'],fraud['rf_pred'])



print("Accuracy",(476+117)/(476+117+0+7)*100)

# Accuracy is 98.8333
fraud["rf_pred"]

import matplotlib.pyplot as plt
#plot

import graphviz
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO 
from sklearn.tree import export_graphviz 
from IPython.display import Image 
import pydotplus
dot_data = StringIO()
export_graphviz(fraud, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names =fraud ,class_names=fraud)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png ('fraudrf.png')
import os
os.environ['PATH'] = os.environ['PATH']+';'+os.environ['CONDA_PREFIX']+r"\Library\bin\graphviz"
Image(graph.create_png())
