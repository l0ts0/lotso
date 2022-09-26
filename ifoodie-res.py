#import
from audioop import avg
from cgitb import text
from sqlite3 import Cursor
import requests 
from bs4 import BeautifulSoup
import json
import time
import pandas as pd
import csv
import pymysql
from sqlalchemy import create_engine

dbcon=pymysql.connect('localhost', port=3306, user='root', passwd='', charset='utf8', db='pydb')

alldata=pd.DataFrame()
url='https://ifoodie.tw/api/restaurant/explore/?city_name=%E5%8F%B0%E4%B8%AD%E5%B8%82&order_by=recent&limit=15'
#請求抓到網址
resp=requests.get(url)
#轉成json格式
getdata=json.loads(resp.content)
#篩選出要爬取的資料
todataframe=pd.DataFrame(getdata['response'])
phone=pd.DataFrame(todataframe['phone'])
address=pd.DataFrame(todataframe['address'])
avg_price=pd.DataFrame(todataframe['avg_price'])
rating=pd.DataFrame(todataframe['rating'])
admin_name=pd.DataFrame(todataframe['admin_name'])
opening_hours_list=pd.DataFrame(todataframe['opening_hours_list'])
categories=pd.DataFrame(todataframe['categories'])
name=pd.DataFrame(todataframe['name'])
alldata=pd.concat([alldata , phone , address , avg_price , rating , admin_name , opening_hours_list , categories , name],axis=1)
i=15
#soup=BeautifulSoup(resp.text)
#allcom=soup.find_all("a",class_="jsx-3292609844")
#print(allcom)
#迴圈把資料抓出來
for i in range(15, 45, 15):
  url='https://ifoodie.tw/api/restaurant/explore/?city_name=%E5%8F%B0%E4%B8%AD%E5%B8%82&order_by=recent&offset='+str(i)+'&limit=15'
  resp=requests.get(url)
  getdata=json.loads(resp.content)
  todataframe=pd.DataFrame(getdata['response'])
  phone=pd.DataFrame(todataframe['phone'])
  address=pd.DataFrame(todataframe['address'])
  avg_price=pd.DataFrame(todataframe['avg_price'])
  rating=pd.DataFrame(todataframe['rating'])
  admin_name=pd.DataFrame(todataframe['admin_name'])
  opening_hours_list=pd.DataFrame(todataframe['opening_hours_list'])
  categories=pd.DataFrame(todataframe['categories'])
  name=pd.DataFrame(todataframe['name'])
  alldata=pd.concat([alldata , phone , address , avg_price , rating , admin_name , opening_hours_list , categories , name],axis=1)
  comurl=str

  time.sleep(5)
alldata.to_csv('ifood.csv', encoding='utf-8-sig', index=False)
# sql="insert into rest(phone,name,opening_hours_list,categories) value ('"+alldata+"')"
#lldata.to_sql(name='rest', con=engine)
'''try:
  Cursor.execute(sql)
  engine.commit()
  print("資料已存入")
except:
  engine.rollback()
  print("資料存入失敗")'''
#engine.close()