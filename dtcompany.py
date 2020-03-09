# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:02:13 2020

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

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(train[predictors],train[target])
preds = model.predict(test[predictors])
pd.Series(preds).value_counts()
pd.crosstab(test[target],preds)

import matplotlib.pyplot as plt
#plot

import graphviz
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO 
from sklearn.tree import export_graphviz 
from IPython.display import Image 
import pydotplus
dot_data = StringIO()
export_graphviz(company,out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names =company,class_names=company)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png ('company.png')
import os
os.environ['PATH'] = os.environ['PATH']+';'+os.environ['CONDA_PREFIX']+r"\Library\bin\graphviz"
Image(graph.create_png())

