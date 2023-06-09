import streamlit as st
import numpy as np
import pandas as pd
from openpyxl import Workbook

st.set_page_config(page_title="관악구 맛집 지도", page_icon="🍴")
st.title('관악구 맛집 지도 🍽️')

with st.sidebar:
    st.text_input("식당 이름 검색 🔍")

rawVisitedPlacesdf = pd.read_excel("./visitedRestaurant.xlsx", skiprows = 1)
sortedVisitedPlacesdf = rawVisitedPlacesdf.sort_values(by = '업체명', ascending = False)
sortedVisitedPlacesdf['업체명'] = sortedVisitedPlacesdf['업체명'].str.replace(pat=' ', repl = '')
removedWhiteSpaceVisitedPlacesdf = sortedVisitedPlacesdf.copy()
removedWhiteSpaceVisitedPlacesdf.insert(2, '방문 횟수', 1)
nonCleanedVisitedPlacesdf = removedWhiteSpaceVisitedPlacesdf
nonCleanedVisitedPlacesdf = nonCleanedVisitedPlacesdf.reset_index(drop=True)
for count in range(len(nonCleanedVisitedPlacesdf) - 1) :
    if nonCleanedVisitedPlacesdf['업체명'][count + 1] in nonCleanedVisitedPlacesdf['업체명'][count] :
        nonCleanedVisitedPlacesdf['업체명'][count + 1] = nonCleanedVisitedPlacesdf['업체명'][count]
nonCleanedVisitedPlacesdf = nonCleanedVisitedPlacesdf.sort_values(by = '업체명',ascending = True)
nonCleanedVisitedPlacesdf = nonCleanedVisitedPlacesdf.reset_index(drop=True)
dfLen = len(nonCleanedVisitedPlacesdf) - 1
for count in range(dfLen) :
    if nonCleanedVisitedPlacesdf['업체명'][count + 1] == nonCleanedVisitedPlacesdf['업체명'][count] :
        nonCleanedVisitedPlacesdf['사용금액'][count + 1] += nonCleanedVisitedPlacesdf['사용금액'][count]
        nonCleanedVisitedPlacesdf['방문 횟수'][count + 1] += nonCleanedVisitedPlacesdf['방문 횟수'][count]
nonCleanedVisitedPlacesdf = nonCleanedVisitedPlacesdf.sort_values(by = '업체명',ascending = False)
nonCleanedVisitedPlacesdf = nonCleanedVisitedPlacesdf.reset_index(drop=True)
visitedPlacesdf = nonCleanedVisitedPlacesdf.drop_duplicates(['업체명'])
visitedPlacesdf = visitedPlacesdf.sort_values(by = '업체명',ascending = True)
cleanedVisitedPlacesdf = visitedPlacesdf.reset_index(drop=True)

tab1, tab2, tab3 = st.tabs(['검증된 맛집 모음', '식당 방문 이력','모범음식점 모음'])


with tab1:
    st.subheader('검증된 맛집 리스트 ✅')

    with st.expander('월수목금 기준 (₩10000)'):
        # normalVerifiedRestaurantsdf = pd.DataFrame(columns=['식당 명','추천 메뉴', '거리', '삭제'])
        # st.write(normalVerifiedRestaurantsdf)
        normalVerifiedRestaurantsdf = pd.DataFrame(columns=['식당 명','추천 메뉴', '거리', '삭제'])
        
        testdf = pd.DataFrame({
            '식당 명': ['테스트1', '테스트2', '테스트3'],
            '추천 메뉴': ['메뉴1', '메뉴2', '메뉴3'],
            '거리': ['5분', '10분', '15분']
        })
        st.dataframe(testdf)


    with st.expander('화요일 기준 (₩20000)'):
        specialVerifiedRestaurantsdf = pd.DataFrame(columns=['식당 명','추천 메뉴', '거리', '삭제'])
        st.write(specialVerifiedRestaurantsdf)
    
with tab2:
    # st.header('월수목금 기준 (10000₩)')
    st.subheader('가장 많이 방문한 식당 Top 5 👣')
    st.write((cleanedVisitedPlacesdf.sort_values(by = '방문 횟수', ascending = False).reset_index(drop=True))[0:5])
    st.subheader('가장 많이 결제한 식당 Top 5 🤑')
    st.write((cleanedVisitedPlacesdf.sort_values(by = '사용금액', ascending = False).reset_index(drop=True))[0:5])
    
    with st.expander('방문했던 식당 리스트 ✍️'):
        st.write(cleanedVisitedPlacesdf)

with tab3:

    st.subheader('23년도 6월 2일 기준 서울시 관악구 모범음식점 리스트')
    
    fullModelRestaurantdf = pd.read_excel("./modelRestaurant.xls")
    select_near_place = st.radio (
        '어떤 지역의 식당을 보여드릴까요?',
        ('회사 근처', '신림', '봉천', '그냥 먼 곳')
    )
    modelRestaurantdf = fullModelRestaurantdf.drop(columns=
    [
        "시군구코드",
        "지정년도",
        "지정번호",
        "신청일자",
        "지정일자",
        "취소일자",
        "불가일자",
        "소재지지번",
        "허가(신고)번호",
        "행정동명",
        "급수시설구분"
    ])
    
    if select_near_place == '회사 근처':
        tmpdf = modelRestaurantdf[
            (modelRestaurantdf['소재지도로명'].str.contains('봉천로')) |
            (modelRestaurantdf['소재지도로명'].str.contains('쑥고개로')) |
            (modelRestaurantdf['소재지도로명'].str.contains('관악로')) |
            (modelRestaurantdf['소재지도로명'].str.contains('남부순환로'))
        ]
    elif select_near_place == '신림':
        tmpdf = modelRestaurantdf[modelRestaurantdf['소재지도로명'].str.contains('신림')]
    elif select_near_place == '봉천' :
        tmpdf = modelRestaurantdf[modelRestaurantdf['소재지도로명'].str.contains('봉천')]
    elif select_near_place == 0 :
        tmpdf = modelRestaurantdf
    else :
        tmpdf = modelRestaurantdf[
           ~(modelRestaurantdf['소재지도로명'].str.contains('봉천로') |
            modelRestaurantdf['소재지도로명'].str.contains('쑥고개로') |
            modelRestaurantdf['소재지도로명'].str.contains('관악로') |
            modelRestaurantdf['소재지도로명'].str.contains('남부순환로') |
            modelRestaurantdf['소재지도로명'].str.contains('신림') |
            modelRestaurantdf['소재지도로명'].str.contains('봉천'))
        ]

    
    st.write(tmpdf)