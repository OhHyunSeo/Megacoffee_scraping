#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 23:38:21 2025

@author: oh
"""

import pandas as pd

seoul_mega = pd.read_excel("./mega/seoul_mega_df.xlsx", header = 0)


seoul_mega.columns
# 메가 주소 정보에서 시군구명 추출
sgg_names = []

for address in seoul_mega['주소']:
    sgg = address.split()[1]
    sgg_names.append(sgg)

seoul_mega['시군구명'] = sgg_names

# 엑셀로 저장
seoul_mega.to_excel("./mega/seoul_mega_location.xlsx", index = False)
