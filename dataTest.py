apikey='U+FQCt+nIIQxSTHrl0ZeNwe5+tCOfA1WLqpy4mQA+VQ89XAT9kprS78B1D0sRgxBxVL7dp1l8xtT5dIqc9HALw=='

import requests 
import pandas as pd
import json
url = 'https://api.odcloud.kr/api/15088856/v1/uddi:f88e5a0d-52e2-4fdf-badc-dd0eb3127aeb'
params ={'serviceKey' : apikey, '선별' : '분당선'}

response = requests.get(url, params=params)
print(response.content.decode('utf-8'))

dict = json.loads(response.text)

#데이터 프레임만 선택하여 doc 객체에 저장
doc = dict["data"]

# 데이터 프레임으로 변환
data = pd.DataFrame(doc)

print(data.head())