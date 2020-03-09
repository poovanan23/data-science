import pandas as pd
import numpy as np
fraud = pd.read_csv(r"C:\Users\POOVAYUVA\Desktop\dtassign\Fraud_check.csv")
col=list(fraud.columns)
fraud = fraud.iloc[:,[2,0,1,3,4,5]]
def clear(x):
    if x<=30000:
      return "RISKY"
    else:
        return "GOOD"
fraud['Taxable']=fraud['Taxable'].apply(clear)
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
fraud['Taxable'].unique()
colnames = list(fraud.columns)
predictors = colnames[1:5]
target = colnames[0]
import numpy as np
fraud['is_train'] = np.random.uniform(0, 1, len(fraud))<= 0.75
fraud['is_train']
train,test = fraud[fraud['is_train'] == True],fraud[fraud['is_train']==False]

from sklearn.model_selection import train_test_split
train,test = train_test_split(fraud,test_size = 0.2)

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(train[predictors],train[target])
preds = model.predict(test[predictors])
pd.Series(preds).value_counts()
pd.crosstab(test[target],preds)

np.mean(train.Taxable == model.predict(train[predictors]))
np.mean(preds==test.Taxable)
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
graph.write_png ('fraud.png')
import os
os.environ['PATH'] = os.environ['PATH']+';'+os.environ['CONDA_PREFIX']+r"\Library\bin\graphviz"
Image(graph.create_png())
