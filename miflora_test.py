# -*- coding:utf-8 -*-

import requests

DEV_ID = 'MIFLORA_DUMMY'

URL = 'https://api.ohf.ag/iot/data'

sensor_data = [26.2, 59, 1970, 1376, 21]  # 溫度, 土壤溼度, 光照, 電導度, 電力 https://github.com/open-homeautomation/miflora/blob/master/demo.py

r = requests.post(URL, json={"id": DEV_ID, "data": sensor_data})
