#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:39:56 2025

@author: oh

매장수와 한국인 인구수 비교
매장수와 외국인 인구수 비교
매장수와 업종별 종사자수 비교
-> 업종별 : 상위 5개 업종

report
report2
위 두 파일을 이용하여 구별 거주 한국인 / 외국인 인구수 가공
시군구별 한국인과 외국인수
"""

import pandas as pd

sgg_pop_df = pd.read_csv("./starbucks_location/files/report.txt", sep = '\t', header = 2)
sgg_pop_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 26 entries, 0 to 25
Data columns (total 14 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   기간        26 non-null     object 
 1   자치구       26 non-null     object 
 2   세대        26 non-null     object 
 3   계         26 non-null     object 
 4   남자        26 non-null     object 
 5   여자        26 non-null     object 
 6   계.1       26 non-null     object 
 7   남자.1      26 non-null     object 
 8   여자.1      26 non-null     object 
 9   계.2       26 non-null     object 
 10  남자.2      26 non-null     object 
 11  여자.2      26 non-null     object 
 12  세대당인구     26 non-null     float64
 13  65세이상고령자  26 non-null     object 
dtypes: float64(1), object(13)
memory usage: 3.0+ KB
'''

columns = {
    '기간': 'GIGAN',
    '자치구': 'JACHIGU',
    '계': 'GYE_1',
    '계.1': 'GYE_2',
    '계.2': 'GYE_3',
    '남자': 'NAMJA_1',
    '남자.1': 'NAMJA_2',
    '남자.2': 'NAMJA_3',
    '여자': 'YEOJA_1',
    '여자.1': 'YEOJA_2',
    '여자.2': 'YEOJA_3',
    '세대': 'SEDAE',
    '세대당인구': 'SEDAEDANGINGU',
    '65세이상고령자': 'N_65SEISANGGORYEONGJA'
}
sgg_pop_df.rename(columns = columns, inplace = True)

sgg_pop_df.head()

# 필요없는 데이터 제거 : 첫 번째 데이터 합계
condition = sgg_pop_df['JACHIGU'] != '합계'
sgg_pop_df_selected = sgg_pop_df[condition]



# 필요 컬럼 선택
sgg_pop_df_final = sgg_pop_df_selected[['JACHIGU', 'GYE_2', 'GYE_3']]


sgg_pop_df_final.info()

sgg_pop_df_final.head()

sgg_pop_df_final.rename(columns = {'JACHIGU' : '자치구',
                                   'GYE_2' : '한국인',
                                   'GYE_3' : '외국인'}, inplace = True)


# 저
sgg_pop_df_final.to_excel('./mega/sgg_pop_df_final2.xlsx', index = False)

























































