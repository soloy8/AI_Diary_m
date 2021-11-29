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

    st.write(
    """
    광운대 산업심리학과 이상희 교수팀 연구논문
    '대학생들의 정서에 따른 컴포트 푸드의 차이 : 성차를 중심으로(2014)'
    
    
    행복할 때 찾는 음식은?
    남학생 1위 고기, 2위 술
    여학생 1위 치킨, 2위 피자, 스파게티
    
    즐거울 때 찾는 음식은?
    남학생 1위 술, 2위 치킨
    여학생 1위 치킨, 2위 아이스크림
    
    슬플 때 찾는 음식은? 
    남학생 1위 술, 2위 초콜릿
    여학생 1위 초콜릿, 2위 술 
    
    화날 때 찾는 음식은?
    남학생 1위 술, 2위 매운음식
    여학생 1위 매운음식, 2위 초콜릿
    
    '맨날 술이야, 맨날 술이야'
    남자 대학생들이 슬플때나 화날때 첫번째로 주로 술을 택한 것은
    술을 통해 관계가 형성되는 한국 사회의 특성이 반영된 결과로도 해석될 수 있습니다. 
    
    매운 음식의 경우 기분이 가라앉았을 때 먹으면 
    몸에서 열이 식으면서 스트레스가 일시적으로 경감될 수 있다고 합니다~"""
    )


if __name__ == "__main__":
    write()