import requests

url = "https://www.starbucks.co.kr/store/getStore.do?r=GKYHQKU7D3"
payload = {"in_biz_cds" : "0",
"in_scodes" : "0",
"ins_lat" : "37.566535",
"ins_lng" : "126.9779692",
"search_text" : "",
"p_sido_cd" : "01",
"p_gugun_cd" : "",
"in_distance" : "0",
"in_biz_cd" : "",
"isError" : "true",
"searchType" : "C",
"set_date" : "",
"all_store" : "0",
"T03" : "0",
"T01" : "0",
"T27" : "0",
"T12" : "0",
"T09" : "0",
"T30" : "0",
"T05" : "0",
"T22" : "0",
"T21" : "0",
"T10" : "0",
"T36" : "0",
"T43" : "0",
"T48" : "0",
"P10" : "0",
"P50" : "0",
"P20" : "0",
"P60" : "0",
"P30" : "0",
"P70" : "0",
"P40" : "0",
"P80" : "0",
"whcroad_yn" : "0",
"P90" : "0",
"new_bool" : "0",
"iend" : "1000",
"rndCod" : "IZVHHSIFWC",}
r = requests.post(url, data=payload)
star = r.json()['list']
r_cnt = 0
dt_cnt = 0
for i in star:

    if i['s_name'][-1] == 'R':
        # print(i['s_name'])
        r_cnt += 1
    if i['s_name'][-2:] == 'DT':
        # print(i['s_name'])
        dt_cnt += 1

star_gu_dict = {}
for store in star: #딕셔너리 안에 없을 때 1로 초기화, 사전에 담고 난 후 else 로 개수 증가
    if store['gugun_name'] not in star_gu_dict:
        star_gu_dict[store['gugun_name']] = 1
    else:
        star_gu_dict[store['gugun_name']] += 1
# 딕셔너리 items()로 추출하고, 리스트화 하면 키,벨류가 튜플에 담김  ->  튜플(키,벨류)
sorted_star = sorted(star_gu_dict.items(), key=lambda x: x[1],reverse=True)
print(sorted_star[0],sorted_star[-1])
print()
print(f'서울시 구 : {len(star_gu_dict)} 개 구')
print(f'일반 매장 : {len(star)-r_cnt-dt_cnt} 개')
print(f'리저브 매장 : {r_cnt} 개 , 드라이브스루 매장 : {dt_cnt} 개')


date_star = {}
# weekday = dict(zip(range(0,7),[0,0,0,0,0,0,0]))
weekday = dict(zip(range(0,7),'월화수목금토일'))  # 0 : 월
master = dict(zip('월화수목금토일',[0,0,0,0,0,0,0])) # 월화수목금토일 -> 0123456
from datetime import datetime

for i in star:
    date_star = datetime.strptime(i['open_dt'],'%Y%m%d')
    master[weekday[date_star.weekday()]] += 1
print(master)

open_star = {}
for i in star:
    open_star[i['s_name']] = int(i['open_dt'])
open_asc = sorted(open_star.items(), key=lambda x: x[1])
