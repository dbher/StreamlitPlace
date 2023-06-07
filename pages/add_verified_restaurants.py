import streamlit as st
import numpy as np
import pandas as pd

st.header('검증된 맛집을 추가해주세요')

costRange = st.radio(label='1만원 이하 가격일까요 아니면 2만원 이하 가격일까요 ❓', options=['1만원 이하', '2만원 이하'])
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

def on_button_click(name, menu) :
    if (name or menu != '') :
        st.balloons()
        st.success('식당 추가가 완료되었습니다 🥳')
    else :
        st.error('아직 작성되지 않은 부분이 있습니다. 모든 입력란을 작성해주세요 🙏')

if costRange == '1만원 이하':
    nomalName = st.text_input('식당 이름을 입력해주세요 ❗️', placeholder = '식당 명')
    nomalMenu = st.text_input('어떤 메뉴가 맛있나요 ❓', placeholder = '추천 메뉴')
    nomalDistance = st.radio(label='회사랑 어느 정도로 떨어져있나요 ❓', options=['5분 컷', '10분 컷', '15분 이상 🥲'])
    if st.button("작성 완료"):
        on_button_click(nomalName, nomalMenu)

else:
    specialName = st.text_input('식당 이름을 입력해주세요 ❗️', placeholder = '식당 명')
    specialMenu = st.text_input('어떤 메뉴가 맛있나요 ❓', placeholder = '추천 메뉴')
    specialDistance = st.radio(label='회사랑 어느 정도로 떨어져있나요 ❓', options=['5분 컷', '10분 컷', '15분 이상 🥲'])
