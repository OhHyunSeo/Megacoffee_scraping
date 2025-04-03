# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 04:22:02 2025

@author: tuesv
"""
import pandas as pd
import folium
import json

seoul_sgg_stat = pd.read_excel("./starbucks_location/files/seoul_sgg_stat.xlsx",
                               thousands= ',')
seoul_sgg_stat.head()
'''
   시군구코드  시군구명         위도          경도  스타벅스_매장수  주민등록인구    종사자수   사업체수
0  11320   도봉구  37.665861  127.031767         2  329300   74314  18894
1  11380   은평구  37.617612  126.922700         8  485842   90049  24873
2  11230  동대문구  37.583801  127.050700         8  358679  140748  31878
3  11590   동작구  37.496504  126.944307        11  404617  112564  19916
4  11545   금천구  37.460097  126.900155        11  249641  234012  32472
'''

# 서울시 시군구 행정 게계 지도 파일
sgg_geojson_file_path = './starbucks_location/maps/seoul_sgg.geojson'

seoul_sgg_geo = json.load(open(sgg_geojson_file_path, encoding="utf-8"))

seoul_sgg_geo['features'][0]['properties']
'''
{'SIG_CD': '11320',
 'SIG_KOR_NM': '도봉구',
 'SIG_ENG_NM': 'Dobong-gu',
 'ESRI_PK': 0,
 'SHAPE_AREA': 0.00210990544544,
 'SHAPE_LEN': 0.239901251347}
'''

# folium 지도 생성
starbucks_bubble = folium.Map(location=[37.573050, 126.979189],
                              tiles = 'CartoDB positron',
                              zoom_start=11)

starbucks_bubble.save("starbucks_bubble.html")

# 서울시 시군구 경계 지도 그리기
# folium.GeoJson(GeoJson객체, style_function=함수)

def style_function(feature):
    return {
            'opacity' : 0.7,
            'weight' : 1,
            'color' : 'black',
            'fillOpacity' : 0,
            'dashArray' : '5, 5'
            }

folium.GeoJson(seoul_sgg_geo, style_function=style_function).add_to(starbucks_bubble)

starbucks_bubble.save("starbucks_bubble_bound.html")

# 서울시 시군별 스타벅스 평균 매장 수 계산
starbucks_mean = seoul_sgg_stat['스타벅스_매장수'].mean()

# 버블 지도로 시각화
for idx in seoul_sgg_stat.index:
    lat = seoul_sgg_stat.loc[idx, '위도']
    lng = seoul_sgg_stat.loc[idx, '경도']
    count = seoul_sgg_stat.loc[idx, '스타벅스_매장수']
    
    if count > starbucks_mean:
        fillColor = 'red'
        
    else:
        fillColor = "blue"
        
    folium.CircleMarker(
        location = [lat, lng],
        color = '#FFFF00',
        fill_color = fillColor,
        fill_opacity = 0.7,
        weight = 1.5,
        radius = count/2).add_to(starbucks_bubble)
    
starbucks_bubble.save('starbucks_bubble_mean.html')

# 서울시 시군구별 스타벅스 매장 수를 단계구분도로 시각화
# 서울시 시군구 행정 게계 지도 파일
sgg_geojson_file_path = './starbucks_location/maps/seoul_sgg.geojson'
seoul_sgg_geo = json.load(open(sgg_geojson_file_path, encoding="utf-8"))

# folium 지도 생성
starbucks_choropleth = folium.Map(location=[37.573050, 126.979189],
                              tiles = 'CartoDB dark_matter',
                              zoom_start=11)

folium.Choropleth(geo_data = seoul_sgg_geo, 
                  data = seoul_sgg_stat,
                  columns=['시군구명', '스타벅스_매장수'],
                  fill_color= 'YlGn',
                  fill_opacity= 0.7,
                  line_opacity=0.5,
                  key_on = 'properties.SIG_KOR_NM').add_to(starbucks_choropleth)

starbucks_choropleth.save('starbucks_choropleth.html')
































