# -*- coding:utf-8 -*-

import requests

DEV_ID = 'FIELD_SENSOR_2_DUMMY'

URL = 'https://api.ohf.ag/iot/data'

sensor_data = '4c4c11e10184003c008904bc'

# Sigfox callback example
# { "id": "{device}", "time": "{time}", "data": "{data}"}
r = requests.post(URL, json={"id": DEV_ID, "data": sensor_data})
