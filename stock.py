import requests
import pandas as pd
url = "https://finance.naver.com/item/sise_day.naver?code=005930&page={}"   # page = {} 포맷팅
head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
# df_1 = pd.concat([pd.read_html(requests.get(url.format(x), headers=head).text)[0].dropna() for x in range(4,1,-1)])
# print(df_1)
a_prac = 1

def sentences(sentence):
    if type(sentence) != str:
        return False
    else:
        return sentence[:3]+'입니다'
print(sentences(a_prac))
Encore = ['진만쿤',310,'정연쿤']
Mortgage = [1.5, 3, 6]
import random
text = '{0}님께서는 최저이율 {1}% 로 대출가능하세요'
# for name,perc in zip(Encore, Mortgage):
#     print(text.format(name,perc))

tmp = [1, 2, 3.0, 'Hi']
a = tmp.copy()
for i in tmp:
    print(type(i))