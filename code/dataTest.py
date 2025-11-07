import requests
# from bs4 import BeautifulSoup as bs
import json
import pandas as pd

serviceKey=''
rType='json'
num='32'
url='https://api.odcloud.kr/api/15088856/v1/uddi:f88e5a0d-52e2-4fdf-badc-dd0eb3127aeb?page=1&perPage=10&serviceKey='+serviceKey+'&pageNo=1&numOfRows='+num+'&resultType='+rType

res=requests.get(url).text
data=json.loads(res)
# print(data)
subways=data["data"]
subway_list=[]
i=0
for subway in subways:
    type_of_track=subway["선별"]
    peak=subway["첨두"]
    best_peak=subway["최고"]
    most_crowded=subway["최대 혼잡구간"]
    subway_list.append(tuple([type_of_track,peak,best_peak,most_crowded]))
    i+=1

# print(subway_list)
df=pd.DataFrame(subway_list,columns=['type_of_track','peak','best_peak','most_crowded'])
print(df)
# print(subway_list)