from email import message
import requests
import json
url = "https://ifoodie.tw/api/checkin/?restaurant_id=5ff280b022613957d283c264&limit=12"

res = requests.get(url)

# 把 JSON 轉成 Python 可存取之型態
res_json = res.json()

# 我們要的每日成交資訊在 data 這個欄位
#daily_price_list = res_json.get("response")
#response_list=res_json['response']
#response_dict=dict.fromkeys(response_list)
print(res_json['response'][0]['id'])
print(res_json['response'][0]['user']['display_name'])
print(res_json['response'][0]['message'])
print(res_json['response'][0]['photo'])
# 該欄位是 List 所以用 for 迴圈 出
#for daily_price in daily_price_list:
#    print(daily_price)