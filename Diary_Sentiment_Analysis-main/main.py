#-*-coding:utf-8-*-

#다층 페이지 구성을 위하여, 원본 폴더인 diary를 side바 기능만 남긴 main.py로 변경하고, src파일의 Home 파일에 diary를 이전함.

#AI감정분석으로 이전.
#import pandas as pd
#import numpy as np


#import구문.
import streamlit as st


#sidebar용 page import

import awesome_streamlit as ast
#src import를 못해서 추가시킴.

#scr의 각 페이지 import
import pages.다이어리
import pages.AI감정분석
import pages.AI뮤직
import pages.AI푸드
import pages.AI여행
import pages.달력
import pages.제작진행부분




#test part


#사이드바
#사이드바 PAGES 정의
PAGES = {
    "다이어리": pages.다이어리,
    "AI감정분석": pages.AI감정분석,
    "AI뮤직": pages.AI뮤직,
    "AI푸드": pages.AI푸드,
    "AI여행": pages.AI여행,
    "달력": pages.달력,
    "제작진행부분": pages.제작진행부분,

}

st.sidebar.header("어디로 갈까요...")
#임시중지 add_selectbox = st.sidebar.selectbox("왼쪽 사이드바 Select Box", ("일기장", "AI가 분석한 당신의 감정", "감정을 채워줄 노래"))
# 사이드바 분기
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]

#스피너 여기서 들어가서 한번 더 넣으면 이중임.
with st.spinner(f"Loading {selection} ..."):
    ast.shared.components.write_page(page)
st.sidebar.title("Contribute")
st.sidebar.write("회전하는 기여자 명판 제작 고려중.")


#사이드바 종료

#본문 ->src pages의 home 파일로 이전.

#st.balloons()
#풍선 상태요소.

# test data