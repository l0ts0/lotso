from requests import request
from selenium import webdriver
import bs4
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import json
import requests
import csv
#無視窗化----------------------------------------------
def tryloop():
    try:
        phone=driver.find_element(By.XPATH,'//div[@class="_2RxyDB58m1nhUr5OzaAR5K"]')
    except:
        driver.execute_script('window.scrollBy(0,1000)')
        time.sleep(1)
        tryloop()
chrome_options=Options()
chrome_options.add_argument('--headless')#控制是否要無視窗化
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('log-level=3')#不顯示log
#selenium設定
path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
chrome_options.binary_location=path
driver=webdriver.Chrome(chrome_options=chrome_options)
#----------------------------------------------------------
url='https://ifoodie.tw/explore/%E5%8F%B0%E4%B8%AD%E5%B8%82/list'
driver.get(url)
dataid={}
n=15
for i in range(0,15):
        dataid[i]=driver.find_elements(By.XPATH,'//div[contains(@class,"jsx-3292609844 restaurant-item  track-impression-ga")]')[i].get_attribute('data-id')#用xpath定位class抓data-id屬性
for j in range(2,5):
    nextpage=url+'?page='+str(j)
    driver.get(nextpage)
    time.sleep(5)
    for i in range(0,15):
        dataid[i+n]=driver.find_elements(By.XPATH,'//div[contains(@class,"jsx-3292609844 restaurant-item  track-impression-ga")]')[i].get_attribute('data-id')#用xpath定位class抓data-id屬性
        n=n+15
header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
with open ('com.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer=csv.writer(csvfile)
    fieldnames = ['id', '姓名', '評論', '照片']
    writer.writerow(['id', '姓名', '評論', '照片'])
    for q in range(0,15):
        comurl='https://ifoodie.tw/api/checkin/?restaurant_id='+dataid[q]+'&limit=12'#用迴圈抓取各餐廳的json檔
        time.sleep(3)
        resp=requests.get(comurl,headers=header)
        resp_json=resp.json()
        for k in range(0,3):
        #writer.writerow(dataid[k])#餐廳id
            try:
                writer.writerow([resp_json['response'][k]['user']['display_name'], resp_json['response'][k]['message'], resp_json['response'][k]['photo']])#該餐廳的評論者
            except:
                continue
        #writer.writerow(resp_json['response'][k]['message'])#評論者的評論
        #writer.writerow(resp_json['response'][k]['photo'])#評論者的上傳的照片
            time.sleep(3)


