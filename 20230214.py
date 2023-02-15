
# if distance < 0 :
#     print('마이너스는 없습니당')
# elif distance <= 3: #3이면 택시
#     print('걸어가세요')
# elif 3 < distance < 10: # 9.99면 버스
#     print('버스타세요')
# elif distance >= 10:
#     print('택시타세요')

# for year in range(1900,2101):
#     if year % 4 == 0 and year % 100 != 0:
#         print(year)
#     elif year % 4 == 0 and year % 400 == 0:
#         print(year)

# nested_loop = [(i,j) for i in range(5) for j in range(5)]
# print(nested_loop)


# def check_yoon(year):
#     if type(year) != 'int':
#         return 'type error: please input dtype:int'
#     if year % 4 == 0 and year % 100 != 0 or year % 400 ==0 :
#         return True
#     else:
#         return False


# print(check_yoon('아'))


total = [f'{x}' for x in range(1,100) if x % 3 == 0 and x % 5 == 0]
ditto = '''Woo woo woo woo ooh
Woo woo woo woo
Stay in the middle
Like you a little
Don't want no riddle
말해줘 say it back
Oh say it ditto
아침은 너무 멀어
So say it ditto
훌쩍 커버렸어
함께한 기억처럼
널 보는 내 마음은
어느새 여름 지나 가을
기다렸지 all this time
Do you want somebody
Like I want somebody
날 보고 웃었지만
Do you think about me now yeah
All the time yeah
All the time
I got no time to lose
내 길었던 하루
난 보고 싶어
Ra-ta-ta-ta 울린 심장 (Ra-ta-ta-ta)
I got nothing to lose
널 좋아한다고 wooah wooah wooah
Ra-ta-ta-ta 울린 심장 (Ra-ta-ta-ta)
But I don't want to
Stay in the middle
Like you a little
Don't want no riddle
말해줘 say it back
Oh say it ditto
아침은 너무 멀어
So say it ditto
I don't want to
Walk in this 미로
다 아는 건 아니어도
바라던 대로
말해줘 Say it back
Oh say it ditto
I want you so, want you
So say it ditto
Not just anybody
너를 상상했지
항상 닿아있던
처음 느낌 그대로 난
기다렸지 all this time
I got nothing to lose
널 좋아한다고 wooah wooah wooah
Ra-ta-ta-ta 울린 심장 (Ra-ta-ta-ta)
But I don't want to
Stay in the middle
Like you a little
Don't want no riddle
말해줘 say it back
Oh say it ditto
아침은 너무 멀어
So say it ditto
I don't want to
Walk in this 미로
다 아는 건 아니어도
바라던 대로
말해줘 Say it back
Oh say it ditto
I want you so, want you
So say it ditto
Woo woo woo woo ooh
Woo woo woo woo'''


from collections import Counter
word_count = {}
for i in ditto.lower().split():
    if i not in word_count:
        word_count[i] = 1
    else:
        word_count[i] += 1
ditto_counter = Counter(ditto.lower().split())
print(ditto_counter)
print(len(ditto_counter), len(word_count))
print(len(word_count))


ditto_desc = sorted(word_count.items(), key=lambda x: -x[1])
print(ditto_desc)


import os
os.getcwd()