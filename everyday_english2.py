import pandas as pd
import schedule as sc
import random
import requests
import time

acc_token = 'ここにLINE Notifyで取得したアクセストークンを入力する'
target_url = 'https://www.eitangokentei.com/chu2-eitango/' 

def send_line():
    rand = random.randint(0, 613)
    data = pd.read_html(target_url)
    msg = data[0][0][rand] + 'は日本語でなんというでしょうか？'
    url ='https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + acc_token}
    payload = {'message': msg}
    requests.post(url, headers=headers, params=payload)
    time.sleep(15)
    msg = '答えは「' + data[0][1][rand] + '」です。'
    payload = {'message': msg}
    requests.post(url, headers=headers, params=payload)

sc.every().day.at('00:00').do(send_line)


while True:
    sc.run_pending()