import streamlit as st
import pandas as pd

def main():
    st.title('데이터프레임 편집기')

    # 초기 데이터프레임 생성
    initial_df = pd.DataFrame({'컬럼1': [1, 2, 3], '컬럼2': ['A', '', ' ']})

    # 데이터프레임 편집기를 통해 데이터프레임 편집
    edited_df = st.data_editor(initial_df, num_rows='dynamic')

    # 데이터프레임의 빈 문자열 및 공백 문자 확인하여 저장 여부 결정
    if has_empty_or_whitespace(edited_df):
        st.warning('빈 문자열 또는 공백 문자로만 이루어진 데이터는 저장할 수 없습니다.')
    else:
        if st.button('저장'):
            save_df_to_file(edited_df)
            st.success('데이터프레임이 저장되었습니다.')
    
    file_path = 'normalVerifiedRestaurants.csv'  # CSV 파일 경로

    # CSV 파일 로드
    df = pd.read_csv(file_path)

    testfd = pd.read_csv(file_path)
    # None 값 또는 공백 확인
    if df.isnull().values.any():
        st.write('CSV 파일에 None 값이 포함되어 있습니다.')
    elif (df == '').values.any():
        st.write('CSV 파일에 공백이 포함되어 있습니다.')
    else:
        st.write('CSV 파일에 None 값 또는 공백이 포함되어 있지 않습니다.')

def has_empty_or_whitespace(df):
    # 데이터프레임의 각 셀에 대해 빈 문자열 또는 공백 문자로만 이루어진지 확인하는 로직을 구현합니다.
    return df.apply(lambda x: (x.astype(str).str.isspace() | x.astype(str).str.strip().eq('')).any()).any()

def save_df_to_file(df):
    # 여기에 데이터프레임을 파일로 저장하는 로직을 추가합니다.
    # 예를 들어, CSV 파일로 저장하는 방법은 다음과 같습니다.
    df.to_csv('편집된_데이터.csv', index=False)

if __name__ == '__main__':
    main()
