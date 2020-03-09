# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:49:26 2020

@author: POOVAYUVA
"""
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
import requests
import matplotlib.pyplot as plt

from wordcloud import WordCloud

reviews = []
for i in range(1,51):
  ip=[]  
  url="https://www.amazon.in/product-reviews/B07HGMQX6N/ref=acr_dpproductdetail_text?ie=UTF8&showViewpoints=1"+str(i)
  response = requests.get(url)
  soup = bs(response.content,"html.parser")
  review = soup.findAll("span",attrs={"class","a-size-base review-text review-text-content"})
  for i in range(len(review)):
    ip.append(review[i].text)  
    print(review[i])
  reviews=reviews+ip 
  
with open("C:\\Users\\POOVAYUVA\\Desktop\\EXCELR ASSIGN\\text mining\\text mining\\TXT\\stp.txt", "r") as f:
    stop_words = f.read()

stop_words = stop_words.split("\n")

corpus = " ".join(reviews)

new_doc = [w for w in corpus.split(" ") if not w in stop_words]

corpus = " ".join(new_doc)


import re
corpus = re.sub("[^A-Za-z ]+", "", corpus)
corpus = corpus.lower()
stop_words2 = ["i", "so", "product","phone", "m30s","samsung", "android"]
corpus = [w for w in corpus.split(" ") if not w in stop_words2]

corpus = " ".join(corpus)

from nltk.stem import PorterStemmer

lst = PorterStemmer()

corpus = [lst.stem(w) for w in corpus.split(" ")]

corpus = " ".join(corpus)

from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer()
count_vect = vect.fit_transform(corpus.split(" "))

names = vect.get_feature_names()

data = pd.DataFrame(count_vect.toarray(), columns = names)

report = {}
for i in data.columns:
    report[i] = data[i].sum()
    
import matplotlib.pyplot as plt

va = []
item =[]
for key, value in report.items():
    if value >=9:
       va.append(value)
       item.append(key)
    
plt.bar(item, va)

# The Product has an good review report
# people mostly spoken about the camera, battery and ites quality
with open("C:\\Users\\POOVAYUVA\\Desktop\\EXCELR ASSIGN\\text mining\\text mining\\TXT\\poswords.txt", "r") as f:
    pos_words = f.read()

pos_words = pos_words.split("\n")


  
with open("C:\\Users\\POOVAYUVA\\Desktop\\EXCELR ASSIGN\\text mining\\text mining\\TXT\\negwords.txt", "r", encoding ="ISO-8859-1") as f:
    neg_words = f.read()

neg_words = neg_words.split("\n")


pos = [w for w in corpus.split(" ") if w in pos_words]
neg = [w for w in corpus.split(" ") if w in neg_words]

neg_cloud = WordCloud(width = 800, height = 800,background_color = 'white', min_font_size = 10).generate(" ".join(neg))

plt.imshow(neg_cloud)



pos_cloud = WordCloud(width = 800, height = 800,background_color = 'white', min_font_size = 10).generate(" ".join(pos))

plt.imshow(pos_cloud)


cloud = WordCloud(width = 800, height = 800,background_color = 'white', min_font_size = 10).generate(corpus)

plt.imshow(cloud)

