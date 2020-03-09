# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:48:07 2020

@author: POOVAYUVA
"""

import pandas as pd

from sklearn import tree

company = pd.read_csv("C:\\Users\\POOVAYUVA\\Desktop\\dtassign\\Company_Data.csv")

def clear(x):
    if x>10:
      return 1
    else:
        return 0
company['Sales']=company['Sales'].apply(clear)
def clear(x1):
    if x1=="Yes":
        return 1
    else:
        return 0
company['Urban']=company['Urban'].apply(clear)
def clear(x2):
    if x2=="Yes":
        return 1
    else:
        return 0
company['US']=company['US'].apply(clear)

def clear(x3):
    if x3=="Good":
      return 2
    elif x3=="Medium":
       return 1
    else:
        return 0
company['ShelveLoc']=company['ShelveLoc'].apply(clear)


company.head()

colnames = list(company.columns)
predictors = colnames[1:11]
target = colnames[0]
import numpy as np
company['is_train'] = np.random.uniform(0, 1, len(company))<= 0.75
company['is_train']
train,test = company[company['is_train'] == True],company[company['is_train']==False]

from sklearn.model_selection import train_test_split
train,test = train_test_split(company,test_size = 0.2)

X = company[predictors]
Y = company[target]

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_jobs=3,oob_score=True,n_estimators=15,criterion="entropy")


np.shape(company) # 600,6 => Shape 

#### Attributes that comes along with RandomForest function
rf.fit(X,Y) # Fitting RandomForestClassifier model from sklearn.ensemble 
rf.estimators_ # 
rf.classes_ # class labels (output)
rf.n_classes_ # Number of levels in class labels 
rf.n_features_  # Number of input features in model 10 here.

rf.n_outputs_ # Number of outputs when fit performed

rf.oob_score_  # 0.85
rf.predict(X)
##############################

company['rf_pred'] = rf.predict(X)
cols = ['rf_pred','Sales']
company[cols].head()
company["Sales"]

from sklearn.metrics import confusion_matrix
confusion_matrix(company['Sales'],company['rf_pred']) # Confusion matrix

pd.crosstab(company['Sales'],company['rf_pred'])



print("Accuracy",(322+78)/(322+78+0+0)*100)

# Accuracy is 100.00
company["rf_pred"]

import matplotlib.pyplot as plt
#plot

import graphviz
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO 
from sklearn.tree import export_graphviz 
from IPython.display import Image 
import pydotplus
dot_data = StringIO()
export_graphviz(company, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names =company,class_names=company)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_jpeg ('companyrf.jpeg')
import os
os.environ['PATH'] = os.environ['PATH']+';'+os.environ['CONDA_PREFIX']+r"\Library\bin\graphviz"
Image(graph.create_jpeg())

