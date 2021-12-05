"""This page is for searching and viewing the list of awesome resources"""
import logging
import streamlit as st

import awesome_streamlit as ast
from awesome_streamlit.core.services import resources


def write():

    st.title('남은 제작 진행 사항.')

    st.write(
    """
        8조의 노력과 헌신으로 많은 부분들이 해결되었습니다. \n
    """)

    st.write(
        """
    1. 캘린더 및 데이터 저장기능 제작하기\n
    2. 로그인기능 제작하기(이지훈님께서 제작해주고 계십니다)\n
    3. 도표 작성\n
    4. AI 뮤직 꾸미기\n
    5. AI푸드 꾸미기?\n
    6. 리소스 제한에 도달\n
    https://discuss.streamlit.io/t/this-app-has-gone-over-its-resource-limits/7334\n
    TTL을 사용하라고..? 하네요..???\n
    
    발표 진행\n
    1. 1차 PPT 김소원님께서 제작 진행해주고 계십니다. (12/7예정)\n
    2. 발표자 선정.\n
 
    모바일 버전과 PC버전 분리.\n
    
    1. 모바일 버전 특이사항. 사이트바 사용이 불편하여 위 아래 스크롤로 전부 통합할 계획입니다. \n 
    2, PC버전 특이사항. \n
    
    \n
    \n
    c.f. 1 git에서 이미지 상대주소 문제로 인하여 url방식의 이미지 첨부를 사용해야 합니다. \n
    c.f. 2 글자크기 테스트\n
    # 1.\n
    ## 2.\n
    ### 3.\n
    #### 4. \n
    """


    )


if __name__ == "__main__":
    write()