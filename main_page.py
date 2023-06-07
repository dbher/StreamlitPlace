import streamlit as st
import numpy as np
import pandas as pd
import openpyxl
# from ./lib/modifyDataframe import 

# def countDuplicates


st.set_page_config(page_title="관악구 맛집 지도", page_icon="🍴")
st.title('관악구 맛집 지도 🍽️')
# st.divider()

with st.sidebar:
    st.text_input("식당 이름 검색 🔍")

tab1, tab2, tab3 = st.tabs(['검증된 맛집 모음', '식당 방문 이력','모범음식점 모음'])


with tab1:
    st.subheader('검증된 맛집 리스트 ✅')

    with st.expander('월수목금 기준 (10000₩)'):
        nomalVerifiedRestaurantsdf = pd.DataFrame(columns=['식당 명','추천 메뉴', '거리'])
        st.write(nomalVerifiedRestaurantsdf)

    with st.expander('화요일 기준 (20000₩)'):
        specialVerifiedRestaurantsdf = pd.DataFrame(columns=['식당 명','추천 메뉴', '거리'])
        st.write(specialVerifiedRestaurantsdf)


# with tab2:
#     st.header('월수목금 기준 (10000₩)')
#     st.subheader('가장 많이 방문한 식당 Top 5 👣')
#     st.subheader('가장 많이 결제한 식당 Top 5 🤑')
#     with st.expander('방문했던 식당 리스트 ✍️'):
    
#         rawVisitedPlacesdf = pd.read_excel("./visitedRestaurant.xlsx", skiprows=1)
#         visitedPlacesdf = rawVisitedPlacesdf.drop_duplicates(['업체명'])
#         visitedPlacesdf.insert(2, '방문 횟수', 0)
#         for countColumnNum in range(len(visitedPlacesdf)):
#             for nestedCountColumnNum in range(len(rawVisitedPlacesdf)):
#                 if visitedPlacesdf['업체명'][countColumnNum] == rawVisitedPlacesdf['업체명'][nestedCountColumnNum]:
#                     visitedPlacesdf.loc[countColumnNum, '방문 횟수'] += 1
        
#         st.write(visitedPlacesdf.columns)
#         st.dataframe(visitedPlacesdf)
    
with tab2:
    st.header('월수목금 기준 (10000₩)')
    st.subheader('가장 많이 방문한 식당 Top 5 👣')
    st.subheader('가장 많이 결제한 식당 Top 5 🤑')
    with st.expander('방문했던 식당 리스트 ✍️'):
    
        rawVisitedPlacesdf = pd.read_excel("./visitedRestaurant.xlsx", skiprows=1)
        visitedPlacesdf = rawVisitedPlacesdf.drop_duplicates(['업체명'])
        visitedPlacesdf.insert(2, '방문 횟수', 0)
        # for countColumnNum in range(len(visitedPlacesdf)):
        #     for nestedCountColumnNum in range(len(rawVisitedPlacesdf)):
        #         if visitedPlacesdf['업체명'].iloc[countColumnNum] == rawVisitedPlacesdf['업체명'].iloc[nestedCountColumnNum]:
        #             visitedPlacesdf.loc[countColumnNum, '방문 횟수'] += 1
        
        st.write(visitedPlacesdf.columns)
        st.dataframe(visitedPlacesdf)


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
    with st.form("my_form"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
           st.write("slider", slider_val, "checkbox", checkbox_val)

    st.write("Outside the form")