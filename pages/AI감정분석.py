"""This page is for searching and viewing the list of awesome resources"""
import logging
import streamlit as st

import awesome_streamlit as ast
from awesome_streamlit.core.services import resources

#차트용 pandas, numpy import
import pandas as pd
import numpy as np
import altair as alt
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write():
    #위 구문 안쓰면 오류임
    st.write("""
    ### AI감성 분석 그래프 \n
    #### 👀지난 일기의 감정을 한눈에 살펴보세요
    """)
#    st.title('AI감성 분석 그래프')
#    st.header('👀지난 일기의 감정을 한눈에 살펴보세요')
    #차트 들여쓰기 안하니까 오류난다.
    
# 데이터 불러오기
    diary_data = pd.read_excel('data/diary_log.xlsx')
    diary_data['date']       = diary_data['date'].dt.date 
    diary_data.set_index('date',inplace=True)


# 표1 - diary 기록 불러오기     
    if st.checkbox("지난 일기 기록 보기📚"):
        
        # st.dataframe(diary_data.head())
        st.write("지난 일기 기록을 살펴 볼 수 있습니다.")
        st.table(diary_data)

# chart1 - 감성 분포표
    emotion_data = diary_data.copy()
    emotion_data['Count'] = 1
    emotion_df=pd.DataFrame(emotion_data.groupby(['emotion'], sort=False)['Count'].count().rename_axis(["Type of Emotion"]).nlargest(7))
    
    if st.checkbox('지난 감정별 분포 기록 보기🔢'):
        st.write('기록된 감정 분포 순위입니다.(높은순)')
        st.table(emotion_df)

# chart1-2 - 감정 분포 그래프
    if st.checkbox('지난 감정별 분포 그래프 보기📈'):
        st.write('기록된 감정 분포 그래프를 한눈에 살펴 볼 수 있습니다.')
        st.bar_chart(emotion_df)


if __name__ == "__main__":
    write()