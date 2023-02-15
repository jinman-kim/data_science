payload = {"in_biz_cds":"0",
"in_scodes":"0",
"ins_lat":"37.566535",
"ins_lng":"126.9779692",
"search_text":"",
"p_sido_cd":"01",
"p_gugun_cd":"",
"in_distance":"0",
"in_biz_cd":"",
"isError":"true",
"searchType":"C",
"set_date":"",
"all_store":"0",
"T03":"0",
"T01":"0",
"T27":"0",
"T12":"0",
"T09":"0",
"T30":"0",
"T05":"0",
"T22":"0",
"T21":"0",
"T10":"0",
"T36":"0",
"T43":"0",
"T48":"0",
"P10":"0",
"P50":"0",
"P20":"0",
"P60":"0",
"P30":"0",
"P70":"0",
"P40":"0",
"P80":"0",
"whcroad_yn":"0",
"P90":"0",
"new_bool":"0",
"iend":"1000",
"rndCod":"CZVMPDMCTR",}

import requests
import json
url = "https://www.starbucks.co.kr/store/getStore.do?r=PO47G07Y8Y"
url_sido = "https://www.starbucks.co.kr/store/getSidoList.do"
r2 = requests.post(url_sido, data=payload)
total = []
for data in r2.json()['list']:
    payload['p_sido_cd'] = data['sido_cd'] # sido_cd = 전체
    r = requests.post(url, data=payload)
    total += r.json()['list']
    # print(data['sido_cd'], data['sido_nm'])
print(len(total))
store = {x['s_name'] : x['open_dt'] for x in total}
store_open_desc = sorted(store.items(), key=lambda x:x[1], reverse=True)
print(store_open_desc[:4])


import pickle
x = 'starbucks3'

with open(f'./{x}.pkl',"wb") as f:
    pickle.dump(total,f)

