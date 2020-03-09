# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:50:36 2020

@author: POOVAYUVA
"""
colnames = smscsv.columns

string_columns=['type', 'text']

from sklearn import preprocessing
number = preprocessing.LabelEncoder()
for i in string_columns:
    smscsv[i] = number.fit_transform(smscsv[i])
    
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix



from sklearn.model_selection import train_test_split

x=smscsv.drop("type",axis=1)
y=smscsv["type"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=1)


sgnb = GaussianNB()
smnb = MultinomialNB()
spred_gnb = sgnb.fit(x_train,y_train).predict(x_test)
confusion_matrix(y_test,spred_gnb)
print ("Accuracy",(10759+1200)/(10759+601+2400+1200)) # 0.79468%

spred_mnb = smnb.fit(x_train,y_train).predict(test_X)
confusion_matrix(test_y,spred_mnb)
print("Accuracy",(10891+780)/(10891+780+2920+780))  # 75%
