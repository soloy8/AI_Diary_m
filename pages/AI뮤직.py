"""This page is for searching and viewing the list of awesome resources"""
import logging
import streamlit as st

import awesome_streamlit as ast
from awesome_streamlit.core.services import resources

#차트용 pandas, numpy import
import pandas as pd
import numpy as np


def write():
    #위 구문 안쓰면 오류임
    st.write("유튜브 링크를 통해 동영상을 재생할 경우 다운로드 및 확장자 수정이 필요없어 간편합니다.")
    st.write("감정분류 리스트 내에서 랜덤함수로 노래 한곡 뽑아도 무방할 것으로 추정됨")
    st.write("""유튜브 원 주소중 watch?v= 뒤의 주소만 embed/ 뒤에 넣어야 웹 페이지에서 정상적으로 작동합니다.  \n 재생용 소스코드 ast.shared.components.video_youtube(src="https://www.youtube.com/embed/fYdoCdmoNAU" # \n youtube 원 주소 https://www.youtube.com/watch?v=fYdoCdmoNAU 
    )""")

    ast.shared.components.video_youtube(
        src="https://www.youtube.com/embed/fYdoCdmoNAU" # youtube 주소 중 watch?v= 뒤의 주소만 embed/ 뒤에 넣어야 정상적 작동.
    )


    ## Show videos 저작권 문제로 유튜브 링크로 변경.
    #vid_file = open("files/BTS (방탄소년단) 'ON' Official MV.mp4", "rb").read()
    #st.video(vid_file, start_time=2)

    ## Play audio file.
    #audio_file = open("files/loop_w_bass.mp3", "rb").read()
    #st.audio(audio_file, format='audio/mp3', start_time=10)








if __name__ == "__main__":
    write()