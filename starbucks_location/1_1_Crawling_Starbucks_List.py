# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 04:22:02 2025

@author: tuesv

1.1 크롤링을 이용한 서울시 스타벅스 매장 목록 데이터 생성
    (1_1_Crawling_Starbucks_List)
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
url = 'https://www.istarbucks.co.kr/store/store_map.do?disp=locale'
driver.get(url)

# 1. webdriver로 '서울'버튼 요소를 찾아 클릭
seoul_btn = '#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a'


# 2. driver.find_element()
#   'css selector
#   seoul_btn
# 3. click()

driver.find_element('css selector', seoul_btn).click()

# 전체 버튼 요소 찾아 클릭
all_btn = '#mCSB_2_container > ul > li:nth-child(1) > a'
driver.find_element('css selector', all_btn).click()

# BeautifulSoup으로 HTML 파싱
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# select()를 이용하여 원하는 html 태그를 모두 찾아오기
starbucks_soup_list = soup.select('li.quickResultLstCon')
len(starbucks_soup_list) # 632

starbucks_soup_list[7]
'''
<li class="quickResultLstCon" data-code="3762" data-hlytag="null" data-index="0" data-lat="37.501087" data-long="127.043069" data-name="역삼아레나빌딩" data-storecd="1509" style="background:#fff"> <strong data-my_siren_order_store_yn="N" data-name="역삼아레나빌딩" data-store="1509" data-yn="N">역삼아레나빌딩  </strong> <p class="result_details">서울특별시 강남구 언주로 425 (역삼동)<br/>1522-3232</p> <i class="pin_general">리저브 매장 2번</i></li>
'''

# 스타벅스 매장 정보 샘플 확인
starbucks_store = starbucks_soup_list[0]

name = starbucks_store.select('strong')[0].text.strip()
# Out[27]: '역삼아레나빌딩'
lat = starbucks_store['data-lat'].strip()
# Out[28]: '37.501087'
lng = starbucks_store['data-long'].strip()
# Out[29]: '127.043069'
store_type = starbucks_store.select('i')[0]['class'][0][4:]
# Out[30]: 'general'
address = str(starbucks_store.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]
# Out[31]: '서울특별시 강남구 언주로 425 (역삼동)'
tel = str(starbucks_store.select('p.result_details')[0]).split('<br/>')[1].split('<')[0]
# Out[32]: '1522-3232'

'''
store_type = starbucks_store.select('i')[0]['class'][0][4:]

starbucks_store.select('i')[0]['class']
=> "pin_general"

starbucks_store.select('i')[0]['class'][0][4:]
=> 'general'

address = str(starbucks_store.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]
-> 왜 split이 두번인지 : 
    
str(starbucks_store.select('p.result_details')[0])
# '<p class="result_details">서울특별시 강남구 언주로 425 (역삼동)<br/>1522-3232</p>'
'''

# 서울시 스타벅스 매장 목록 데이터
# 매장명, 위도, 경도, 주소, 전화번호

starbucks_list = []

for item in starbucks_soup_list:
    name = item.select('strong')[0].text.strip()
    lat = item['data-lat'].strip()
    lng = item['data-long'].strip()
    store_type = item.select('i')[0]['class'][0][4:]
    address = str(item.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]
    tel = str(item.select('p.result_details')[0]).split('<br/>')[1].split('<')[0]

    starbucks_list.append([name, lat, lng, store_type, address, tel])

# starbucks_list => DataFrame

columns = ['매장명', '위도', '경도', '매장타임', '주소', '전화번호']
seoul_starbucks_df = pd.DataFrame(starbucks_list, columns= columns)


seoul_starbucks_df.head()
# 데이터 프레임 요약정보
seoul_starbucks_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 632 entries, 0 to 631
Data columns (total 6 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   매장명     632 non-null    object
 1   위도      632 non-null    object
 2   경도      632 non-null    object
 3   매장타임    632 non-null    object
 4   주소      632 non-null    object
 5   전화번호    632 non-null    object
dtypes: object(6)
memory usage: 29.8+ KB
'''
# 액셀로 저장
seoul_starbucks_df.to_excel("./starbucks_location/files/seoul_starbucks_list2.xlsx",index = False)












