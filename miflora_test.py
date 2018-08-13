# -*- coding:utf-8 -*-

import requests

DEV_ID = 'MIFLORA_DUMMY'

URL = 'https://api.ohf.ag/iot/data'

sensor_data = [26.2, 59, 1970, 1376, 21]  # 光照, 水分, 溫度, 肥力, 電力

r = requests.post(URL, json={"id": DEV_ID, "data": sensor_data})
