import requests
import json

response=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=4bd9af7ca0814c52a3cfa7a5111fcc92')
data=response.text
print(data)
with open('news_article.csv','w',encoding="utf-8") as f:
    f.write(data)
