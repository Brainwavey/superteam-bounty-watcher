import time
from datetime import datetime
import requests
import xray


TARGET_URL = 'https://superteam.fun/api/listings?status=open&sortBy=Date&order=desc'
print('Booting Fathom OS Watcher protocol')

while True:
    current_time= datetime.now().strftime('%H, %M, %S')
    print(f'scanning super team data pipe at {current_time}')

    response= requests.get(TARGET_URL)
    data= response.json()
    for target in data:
        name= target ['title']
        amount = target['rewardAmount']
        duration = target['deadline']
        coin = target['token']
        print(f'bounty : {name} | reward : {amount} | deadline: {duration} | token: {coin}')

    print("-" * 50)
    print('going dark for 20 seconds')
    time.sleep(20)
clean_target = xray.format_data(target)
print(clean_target)