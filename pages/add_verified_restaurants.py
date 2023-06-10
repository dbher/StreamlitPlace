import streamlit as st
import numpy as np
import pandas as pd
import time
from streamlit_extras.switch_page_button import switch_page
from google.oauth2 import service_account
# from gsheetsdb import connect
from shillelagh.backends.apsw.db import connect

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

st.header('검증된 맛집을 추가해주세요')
st.info('행을 잘못 추가한 경우, 제일 앞의 체크박스를 누르고 del키를 누르면 해당 행이 삭제됩니다')

def finish_button_click(df) :
    if (df.isnul) :
        st.balloons()
        st.success('식당 추가가 완료되었습니다 🥳 메인 홈페이지로 이동합니다')
        time.sleep(2.5)
        switch_page("main_page")
    else :
        st.error('아직 작성되지 않은 부분이 있습니다. 모든 입력란을 작성해주세요 🙏')

normalVerifiedRestaurantsdf = pd.DataFrame(columns=['식당 명','추천 메뉴', '거리', '별점', '한 줄 코멘트'])

modifiedNormalVerifiedRestaurantsdf = st.data_editor(
    normalVerifiedRestaurantsdf,
    column_config = {
        '식당 명': '식당 명',
        '추천 메뉴': '추천 메뉴',
        '거리': st.column_config.NumberColumn(
            '거리',
            help = '회사에서 도보 기준으로 얼마나 걸리나요? (분 만 입력해주세요)',
            min_value = 0,
            max_value = 15,
            step = 5,
            format = '%d 분 이상',
            required = True
        ),
        '별점': st.column_config.NumberColumn(
            "Your rating",
            help="How much do you like this command (1-5)?",
            min_value=1,
            max_value=5,
            step=1,
            format="%d ⭐",
            required = True
        )
    },
    num_rows='dynamic',

    
)

st.write('test')
st.write(pd.isnull(modifiedNormalVerifiedRestaurantsdf))

if st.button("작성 완료"):
    finish_button_click(modifiedNormalVerifiedRestaurantsdf)

# costRange = st.radio(label='1만원 이하 가격일까요 아니면 2만원 이하 가격일까요 ❓', options=['1만원 이하', '2만원 이하'])
# st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

# def on_button_click(name, menu) :
#     if (name or menu != '') :
#         st.balloons()
#         st.success('식당 추가가 완료되었습니다 🥳 메인 홈페이지로 이동합니다')
#         time.sleep(2.5)
#         switch_page("main_page")
#     else :
#         st.error('아직 작성되지 않은 부분이 있습니다. 모든 입력란을 작성해주세요 🙏')

# if costRange == '1만원 이하':
#     normalName = st.text_input('식당 이름을 입력해주세요 ❗️', placeholder = '식당 명')
#     normalMenu = st.text_input('어떤 메뉴가 맛있나요 ❓', placeholder = '추천 메뉴')
#     normalDistance = st.radio(label='회사랑 어느 정도로 떨어져있나요 ❓', options=['5분 컷', '10분 컷', '15분 이상 🥲'])
#     if st.button("작성 완료"):
#         on_button_click(normalName, normalMenu)

# else:
#     specialName = st.text_input('식당 이름을 입력해주세요 ❗️', placeholder = '식당 명')
#     specialMenu = st.text_input('어떤 메뉴가 맛있나요 ❓', placeholder = '추천 메뉴')
#     specialDistance = st.radio(label='회사랑 어느 정도로 떨어져있나요 ❓', options=['5분 컷', '10분 컷', '15분 이상 🥲'])
