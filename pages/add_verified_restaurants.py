import streamlit as st
import numpy as np
import pandas as pd
import time
import os
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="맛집 추가하기", page_icon="✏️")

def check_file_exist(fileName):
    if os.path.isfile(fileName):
        return (1);
    else:
        return (0);

def exist_empty_or_whitespace(df):
    return df.apply(lambda x: (x.astype(str).str.isspace() | x.astype(str).str.strip().eq('')).any()).any()


def save_df_to_file(df, type):
    if (type == 'normal'):
        df.to_csv('normalVerifiedRestaurants.csv', index=False)
    else:
        df.to_csv('specialVerifiedRestaurants.csv', index=False)

def finish_button_click(df, type) :
    if (exist_empty_or_whitespace(df)) :
        st.error('아직 작성되지 않은 부분이 있습니다. 모든 입력란을 작성해주세요 🙏')
    else :
        st.balloons()
        save_df_to_file(df, type)
        st.success('식당 추가가 완료되었습니다 🥳 메인 홈페이지로 이동합니다')
        time.sleep(2.5)
        # switch_page("main_page")

st.header('검증된 맛집을 추가해주세요')
st.info('💡 행을 잘못 추가한 경우, 제일 앞의 체크박스를 누르고 del키를 누르면 해당 행이 삭제됩니다')

normalFile = 'normalVerifiedRestaurants.csv'
# normalVerifiedRestaurantsdf = pd.read_csv('normalVerifiedRestaurants.csv')
if check_file_exist(normalFile):
    normalVerifiedRestaurantsdf = pd.read_csv(normalFile)
else :
    normalVerifiedRestaurantsdf = pd.DataFrame(columns=['식당 명','추천 메뉴', '거리', '별점', '한 줄 코멘트'])
    save_df_to_file(normalVerifiedRestaurantsdf)
    normalVerifiedRestaurantsdf = pd.read_csv(normalFile)

modifiedNormalVerifiedRestaurantsdf = st.data_editor(
    normalVerifiedRestaurantsdf,
    column_config = {
        '식당 명': '식당 명',
        '추천 메뉴': '추천 메뉴',
        '거리': st.column_config.NumberColumn(
            '거리',
            help = '회사에서 도보 기준으로 얼마나 걸리나요?',
            min_value = 0,
            max_value = 15,
            step = 5,
            required = True
        ),
        '별점': st.column_config.NumberColumn(
            "Your rating",
            help="이 식당에 별점을 매긴다면 (1-5)?",
            min_value=1,
            max_value=5,
            step=1,
            required = True
        ),
        '한 줄 코멘트': '한 줄 코멘트'
    },
    num_rows='dynamic'
)

if st.button("작성 완료"):
    finish_button_click(modifiedNormalVerifiedRestaurantsdf)
    
specialFile = 'specialVerifiedRestaurants.csv'
