"""This page is for searching and viewing the list of awesome resources"""
import logging
import streamlit as st

import awesome_streamlit as ast
from awesome_streamlit.core.services import resources


def write():

    st.title('호환성 문제 알림.')

    st.write(
    """
    streamlit기반의 파일조차 사소한 오류로 구동 자체가 안되는 경우가 대부분입니다. 때문에 꼭 호환성을 확인해 주셔야 합니다. 제작하실 경우 github에서 branch를 따서 git desk를 통해 push 후 merge하시면 됩니다. 
    접속을 위한 ID PW는 카카오톡 공지사항에 업로드 하였습니다. 호환성 문제로 작업이 많이 급해진점 알려드리게 되어 난처함을 감출 수 없습니다. 항상 노력해주셔서 감사합니다.\n
    \n
    """)

    st.title('시급한 현안')

    st.write(
        """
    1. kobert_hf에 사용되는 모델중 미작동 모델 호환시키기(웹상에서는 import가 아닌 requirement 파일을 통해 구현되게 됩니다.)\n
    
    ###하단 미작동 확인.\n
    mxnet==1.6.0 error2 deep learning module... #1.8 1.7 1.6 1.9 2.0 전부 미작동.\n
    gluonnlp==0.10.0 error3\n
    
    ###하단 작동 확인0.\n
    sentencepiece==0.1.91\n
    transformers==4.8.2\n
    torch==1.10.0\n
    
    ###오락가락...\n
    kobert-tokenizer==0.1\n
`
 \n
    2. Kobery_hf모델 local에서 작동시키기 \n
    3. 노래 추천 코드 웹앱과 호환시키기\n
    4. 캘린더 및 데이터 저장기능 제작하기\n
    5. 로그인기능 제작하기\n
    (3, 4번 쿼리로 서버 데이터 저장해야 할 수도 있습니다) \n
    
    
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