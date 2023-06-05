import streamlit as st
import numpy as np
import pandas as pd

st.title('오늘 뭘 먹을지 고민된다면? 😋')
st.divider()

with st.form("taste_form"):
   questions = {
        "오늘은 밀가루! 🌾 vs 오늘은 쌀! 🍚 vs 저탄수 🥲": ["밀가루", "쌀", "저탄수"]
    }
# 질문에 대한 응답을 저장할 딕셔너리
    responses = {}
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

# 질문과 선택지 설정
questions = {
    "오늘은 밀가루! 🌾 vs 오늘은 쌀! 🍚 vs 저탄수 🥲": ["밀가루", "쌀", "저탄수"]
}


# 질문에 대한 응답을 저장할 딕셔너리
responses = {}

# 질문에 대한 응답을 받음
for question, choices in questions.items():
    answer = st.selectbox(question, choices)
    responses[question] = answer

# 결과 출력
st.write("설문조사 결과:")
for question, answer in responses.items():
    st.write(f"- {question}: {answer}")
