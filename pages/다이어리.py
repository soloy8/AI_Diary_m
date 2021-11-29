"""Home page shown when the user enters the application"""
import streamlit as st
import awesome_streamlit as ast
import numpy as np
from webpage.web_predict import *





#하단은 이전 제작파 코드 
# pylint: disable=line-too-long
def write():

    ##Show image 이거 주석이고 문법 아님.
    from PIL import Image
#    img = st.markdown("!(https://ibb.co/VV3SgK1.png)")
    # Image.open("files/example_cat.jpg")  # 원래 jpeg, jpg가능 확인.
#    st.image(img, width=700, caption="Image example: Diary")  # 400잡으면 전체 400축소됨.
    st.image('https://i.ibb.co/BLwZy1p/example-cat.png', width=700, caption="Image example: Diary") # 400잡으면 전체 400축소됨.

# 사진에 병합.
#    st.title('끄적이는 일기 속에서')
#    st.title('네 노래가 느껴진거야♬')
#    st.write("일기를 작성하시면 AI가 일기 속의 숨겨진 노래를 찾아내 감정을 채워드립니다.")

    import time
    import datetime
    from datetime import datetime, date, time

    st.date_input('날짜 선택')
    # the_time = st.time_input("시간을 입력하세요.", datetime.time()) error?


    # 날씨 파트
    # Necessary libraries
    import requests  # pip install requests
    import os
    import json
    
    col1, col2, col3 = st.columns(3)
    # 기존 날씨 파트
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")

    # 실시간 날씨 파트

    # 텍스트 한줄 쓰는 부분.
    # sentence = st.text_input('여기에 일기를 입력하세요!')
    # 텍스트 여러줄 쓰는 부분.
    

    input_data = st.text_area("오늘의 일기를 작성하세요!")

    # 여기서 input_data를 감정분석 프로그램에 넘겨주고 그 인수를 받아와야 한다. - 해결!

    Push_listen_button = st.button("일기 작성")
    if Push_listen_button:
        result,link = predict(input_data)
        st.success(result)
        ast.shared.components.video_youtube(src=link)