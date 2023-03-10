import re
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

wb = Workbook(write_only=True)
ws = wb.create_sheet()
driver = webdriver.Chrome()
login_url = 'https://www.instagram.com/accounts/login/'

#크롤링할 게시물의 url을 적으세요
photo_url = 'https://www.instagram.com/p/CpACrM_Ja7G/'
driver.get(login_url)
time.sleep(3)
id = 'mangang_sav'
pw = 'Kjm40279501!'
id_login = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(id)
pw_login = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(pw)
time.sleep(2)
login_enter = driver.find_element(By.CSS_SELECTOR,'#loginForm > div > div._ab8w._ab94._ab99._ab9f._ab9m._ab9p._abak._abb8._abbq._abb-._abcm > button').click()
time.sleep(20)

driver.get(photo_url)
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="mount_0_0_BB"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div[2]/div/div/ul/div/li/div/div/div[2]')
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

# 댓글 더보기 접근
while True:
    try:
        driver.find_element(By.XPATH,'//*[@id="mount_0_0_BB"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div[2]/div/div/ul/li/div/button').click()
        time.sleep(2)
    except:
        element = driver.find_element(By.CLASS_NAME,'_a9ym')
#mount_0_0_BB > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.xh8yej3.x1gryazu.x10o80wk.x14k21rp.x1porb0y.x17snn68.x6osk4m > section > main > div > div.x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3 > div > div.x78zum5.xdt5ytf.x4h1yfo.x1n2onr6 > div.x1n2onr6.xw2csxc.x1odjw0f.x5yr21d > div > div > ul > li > div > button
#mount_0_0_BB > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.xh8yej3.x1gryazu.x10o80wk.x14k21rp.x1porb0y.x17snn68.x6osk4m > section > main > div > div.x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3 > div > div.x78zum5.xdt5ytf.x4h1yfo.x1n2onr6 > div.x1n2onr6.xw2csxc.x1odjw0f.x5yr21d > div > div > ul > li > div > button