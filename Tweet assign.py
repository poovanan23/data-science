import pandas as pd

import numpy as np


import tweepy

from tweepy import OAuthHandler

consumer_key = "5bCYi8EL0CIMP2dWUCM14WRbX"
consumer_secret = "sbG9D1ILcVMACyEgj49eXN0ATSAO2G1hJDrzVuX9Lj9Bq3r4Pu"
access_key = "1177957293360443393-GC2l2D62OPAnwnX8uSDolorfKLrv0z"
access_secret = "MvyCDuW6bcFUO4Q2uObe62ZOM77D6cOqzseqBJCwsm5bZ"
    

def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")    
    alltweets = []	
    new_tweets = api.user_timeline(screen_name = screen_name,count=600)
    alltweets.extend(new_tweets) 
    outtweets = [[tweet.created_at,tweet.entities["hashtags"],tweet.entities["user_mentions"],tweet.favorite_count,
                  tweet.geo,tweet.id_str,tweet.lang,tweet.place,tweet.retweet_count,tweet.retweeted,tweet.source,tweet.text,
                  tweet._json["user"]["location"],tweet._json["user"]["name"],tweet._json["user"]["time_zone"],
                  tweet._json["user"]["utc_offset"]] for tweet in alltweets]
    
    import pandas as pd
    tweets_df = pd.DataFrame(columns = ["time","hashtags","user_mentions","favorite_count",
                                    "geo","id_str","lang","place","retweet_count","retweeted","source",
                                    "text","location","name","time_zone","utc_offset"])
    tweets_df["time"]  = pd.Series([str(i[0]) for i in outtweets])
    tweets_df["hashtags"] = pd.Series([str(i[1]) for i in outtweets])
    tweets_df["user_mentions"] = pd.Series([str(i[2]) for i in outtweets])
    tweets_df["favorite_count"] = pd.Series([str(i[3]) for i in outtweets])
    tweets_df["geo"] = pd.Series([str(i[4]) for i in outtweets])
    tweets_df["id_str"] = pd.Series([str(i[5]) for i in outtweets])
    tweets_df["lang"] = pd.Series([str(i[6]) for i in outtweets])
    tweets_df["place"] = pd.Series([str(i[7]) for i in outtweets])
    tweets_df["retweet_count"] = pd.Series([str(i[8]) for i in outtweets])
    tweets_df["retweeted"] = pd.Series([str(i[9]) for i in outtweets])
    tweets_df["source"] = pd.Series([str(i[10]) for i in outtweets])
    tweets_df["text"] = pd.Series([str(i[11]) for i in outtweets])
    tweets_df["location"] = pd.Series([str(i[12]) for i in outtweets])
    tweets_df["name"] = pd.Series([str(i[13]) for i in outtweets])
    tweets_df["time_zone"] = pd.Series([str(i[14]) for i in outtweets])
    tweets_df["utc_offset"] = pd.Series([str(i[15]) for i in outtweets])
    tweets_df.to_csv(screen_name+"_tweets.csv")
    return tweets_df


data = get_all_tweets("NASA")

data = data["text"]


with open("C:\\Users\\POOVAYUVA\\Desktop\\EXCELR ASSIGN\\text mining\\text mining\\TXT\\stp.txt", "r") as f:
    stop_words = f.read()

stop_words = stop_words.split("\n")

corpus = " ".join(data)

new_doc = [w for w in corpus.split(" ") if not w in stop_words]

corpus = " ".join(new_doc)


import re
corpus = re.sub("[^A-Za-z ]+", "", corpus)
corpus = corpus.lower()
stop_words2 = ["rt","the","today","we","i", "so","space"]
corpus = [w for w in corpus.split(" ") if not w in stop_words2]

corpus = " ".join(corpus)

from nltk.stem import PorterStemmer

lst = PorterStemmer()

corpus = [lst.stem(w) for w in corpus.split(" ")]

corpus = " ".join(corpus)

from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer()
count_vect = vect.fit_transform(corpus.split(" "))
count_vect.shape
names = vect.get_feature_names()

report = pd.DataFrame(count_vect.toarray(), columns = names)

file = {}
for i in report.columns:
    file[i] = report[i].sum()
    
import matplotlib.pyplot as plt

va = []
item =[]
for key, value in file.items():
    if value >10:
       va.append(value)
       item.append(key)
    
plt.bar(item, va)


from wordcloud import WordCloud

cloud = WordCloud(width = 800, height = 800,background_color = 'white', min_font_size = 10).generate(corpus)

plt.imshow(cloud)
