# ☕ Megacoffee & Starbucks Store Analysis

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)

## 🔍 소개

**Megacoffee_scraping** 프로젝트는 서울 지역의 메가커피 및 스타벅스 매장 정보를 수집, 정제, 분석하여  
상권 분석 및 시각화를 수행하는 데이터 분석 프로젝트입니다.  
공공데이터 및 직접 크롤링 데이터를 기반으로 지도 시각화 및 상권별 인구·비즈니스 분석도 함께 진행됩니다.

---

## 🧩 주요 기능

- 🏪 메가커피 & 스타벅스 매장 정보 크롤링 및 시각화
- 🧹 데이터 정제 및 주소 처리
- 📊 상권/인구 기반 분석, 버블차트 & 군집지도 시각화
- 🛒 인기 제품(다나와) 크롤링 및 분석

---

## 📁 프로젝트 구조

```
📁 Megacoffee_scraping-master/
│
├── 📁 best_product/
│   ├── 1_Crawling.py               # 다나와 제품 크롤링
│   ├── 2_Preprocessing.py          # 전처리
│   ├── 3_Product_Analysis.py       # 제품 분석
│   └── files/danawa_crawling_result.xlsx
│
├── 📁 mega/
│   ├── 1_1_mega_Crawling.py        # 메가커피 매장 크롤링
│   ├── 1_2_mega_edit_OpenData.py   # 공공데이터 기반 정제
│   ├── 2_1_address.py              # 주소 전처리
│   ├── seoul_mega_df.xlsx          # 결과 엑셀
│   ├── seoul_mega_location.xlsx
│   └── sgg_pop_df_final2.xlsx
│
├── 📁 starbucks_location/
│   ├── 1_1_Crawling_Starbucks_List.py
│   ├── 1_2_edit_OpenData_Download.py
│   ├── 2_1_address.py
│   ├── 2_2_data.py
│   ├── 3_1_map.py
│   ├── 3_2_location_visualization.py
│   ├── 3_3_analysis.py
│   ├── files/
│   │   ├── seoul_starbucks_list.xlsx 외 다수
│   └── maps/seoul_sgg.geojson
│
├── starbucks_map.html                  # 스타벅스 위치 지도 시각화
├── starbucks_bubble.html              # 버블 차트
├── starbucks_choropleth.html          # 군집 색상 지도
├── starbucks_choropleth_biz.html      # 상권 기반 군집지도
├── starbucks_choropleth_pop.html      # 인구 기반 군집지도
└── descript                            # 간단 설명 메모
```

---

## 🚀 실행 방법

### 1. 환경 설정

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # 필요 시 생성
```

### 2. 주요 실행 스크립트

- 메가커피 데이터 크롤링: `mega/1_1_mega_Crawling.py`
- 스타벅스 매장 분석: `starbucks_location/3_3_analysis.py`
- 시각화 결과 보기: HTML 파일 열기 (`starbucks_map.html`, `starbucks_choropleth.html` 등)

---

## 🗺️ 시각화 예시

- ✅ `starbucks_map.html`: 지도 위 매장 분포
- ✅ `starbucks_bubble.html`: 구별 매장 밀집도
- ✅ `starbucks_choropleth_pop.html`: 인구 기반 컬러맵

---

## 🙌 기여 방법

1. 이 레포지토리를 포크하세요.
2. 브랜치를 생성하세요 (`git checkout -b feature/기능`)
3. 커밋하세요 (`git commit -m "Add 기능"`)
4. 푸시하세요 (`git push origin feature/기능`)
5. Pull Request를 보내주세요.
