import requests
import json
import pandas as pd
from  vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
response=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=4bd9af7ca0814c52a3cfa7a5111fcc92')
data=response.text
analyzer= SentimentIntensityAnalyzer()
print(data)
json_data=json.loads(data)
print(type(json_data["articles"]))
print(json_data["articles"])
with open('news_article2.json','w',encoding="utf-8") as f:
    f.write(data)
df1=pd.read_json("news_article2.json")
pd.set_option('display.max_columns',None)
print(df1["articles"])
print(type(df1["articles"][0]))
print(df1["articles"][0]["title"])
neg=[]
pos=[]
neu=[]
title_l=[]
for n in range(df1.shape[0]):
    try:
        title=df1["articles"][n]["title"]
        desc=df1["articles"][n]["description"]
        title_a= analyzer.polarity_scores(title)
        desc_a= analyzer.polarity_scores(desc)
        neg.append((title_a["neg"]+desc_a["neg"])+2)
        pos.append((title_a["pos"]+desc_a["pos"])+2)
        neu.append((title_a["neu"]+desc_a["neu"])+2)
        print(title_a)
    except:
        neg.append(0.0)
        pos.append(0.0)
        neu.append(0.0)

    title_l.append(title)
df2=pd.DataFrame()
df2["Headline"]=title_l
df2["Negative"]=neg
df2["Positive"]=pos
df2["Neutral"]=neu

pd.set_option('display.max_columns',None)

print("Average nagative sentiment",df2.mean()[0])
print("Average positive sentiment",df2.mean()[1])
print("Average neutral sentiment",df2.mean()[2])

