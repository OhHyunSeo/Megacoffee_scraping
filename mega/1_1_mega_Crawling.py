#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:13:13 2025

@author: oh
과제
스타벅스 -> 메가커피로 전환

매장수와 한국인 인구수 비교
매장수와 외국인 인구수 비교
매장수와 업종별 종사자수 비교
-> 업종별 : 상위 5개 업종
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

'''
driver = webdriver.Chrome()
url = 'https://www.mega-mgccoffee.com/store/find/'
driver.get(url)

# 1. webdriver로 '지역'버튼 요소를 찾아 클릭
local_btn = 'body > div.wrap > div.cont_wrap.find_wrap > div > div.cont_box.find01 > div.map_search_wrap > div > div.cont_text_wrap.map_search_tab_wrap > div > ul > li:nth-child(2)'
driver.find_element('css selector', local_btn).click()

# 서울찾기
seoul_btn = "#store_area_search_list > li:nth-child(1)"
driver.find_element('css selector', seoul_btn).click()

# ------------샘플-----------------
# 강남구 클릭 (강남구가 리스트에서 2번째 요소)
gangnam_btn = "#store_area_search_list_result > li:nth-child(2)"
driver.find_element('css selector', gangnam_btn).click()


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 강남구 매장 리스트 저장
gangnam_stores = []

# 매장명 요소 찾기 (일반화된 XPath 사용)
mega_soup_list = soup.select('div.map_point_info_wrap')
len(mega_soup_list)



# 출력
print(f"강남구 매장 수: {len(gangnam_stores)}개")
print(gangnam_stores)

#map > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(3)
#map > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(1) > img:nth-child(1)
#map > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(1) > img:nth-child(2)
#map > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(2) > img
#map > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(63)
store_list = []

for i in range(2,27):
    area_btn = f"#store_area_search_list_result > li:nth-child({i})"
    
    driver.find_element('css selector', area_btn).click()
    time.sleep(3)
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

# 강남구
#store_area_search_list_result > li:nth-child(2)
# 강동구
#store_area_search_list_result > li:nth-child(3)

# 중랑구
#store_area_search_list_result > li:nth-child(26)


# BeautifulSoup으로 HTML 파싱
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# select()를 이용하여 원하는 html 태그를 모두 찾아오기
mega_soup_list = soup.select('li.store_area_search_list')
len(mega_soup_list) # 632


'''

# 서울특별시 주소입력으로 찾아오기
from  selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = 'https://www.mega-mgccoffee.com/store/find/'
driver.get(url)

# 1. webdriver로 '지역'버튼 요소를 찾아 클릭
local_btn = 'body > div.wrap > div.cont_wrap.find_wrap > div > div.cont_box.find01 > div.map_search_wrap > div > div.cont_text_wrap.map_search_tab_wrap > div > ul > li:nth-child(2)'
driver.find_element('css selector', local_btn).click()

# 검색창 입력 클릭
search_box = driver.find_element(By.XPATH, '//*[@id="store_search"]')
search_box.send_keys("서울특별시")
search_box.send_keys(Keys.ENTER)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 매장명 요소 찾기 (일반화된 XPath 사용)
mega_soup_list = soup.select('div.cont_text')
len(mega_soup_list) #475

mega_soup_list[458] # 14번 인덱스부터 시작 ~ 458번 인덱스 까지
'''
<div class="cont_text">
<div class="cont_text_inner">
<b>419사거리점</b>
</div>
<div class="cont_text_inner cont_text_info">
							서울특별시 강북구 삼양로 510, 1층 (수유동)							02-900-1288						</div>
</div>
'''

mega_store = mega_soup_list[14]
mega_store.columns

name = mega_store.select_one('div.cont_text_inner > b').text.strip()
# '강북시장점'

# 기본값 설정
info_text = soup.select('.cont_text_info')[0].text.strip()

# 주소와 전화번호 분리 (전화번호는 항상 마지막 11자리라고 가정)
address = info_text[:-11].strip()
# '서울특별시 강북구 삼양로 510, 1층 (수유동)'
tel = info_text[-11:].strip()
# '02-900-1288'

# 메가커피 데이터프레임 생성
import re

mega_list = []

for item in mega_soup_list[14:459]:
    name = item.select_one('div.cont_text_inner > b').text.strip() 
    info_text = item.select_one('.cont_text_info').text.strip()
    # 주소와 전화번호 분리 (정규 표현식 활용)
    phone_match = re.search(r'\d{2,3}-\d{3,4}-\d{4}', info_text)
    tel = phone_match.group() if phone_match else "없음"  # 전화번호가 없을 경우 대비
    address = info_text.replace(tel, "").strip()  # 전화번호 부분 제거 후 주소만 남김
    
    mega_list.append([name, address, tel])

# starbucks_list => DataFrame

columns = ['매장명', '주소', '전화번호']
seoul_mega_df = pd.DataFrame(mega_list, columns= columns)

seoul_mega_df.head()
seoul_mega_df.tail()

# 데이터 프레임 요약정보
seoul_mega_df.info()

# 저장

seoul_mega_df.to_excel("./mega/seoul_mega_df.xlsx",index = False)

