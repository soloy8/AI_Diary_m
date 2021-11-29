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
    
    #차트 들여쓰기 안하니까 오류난다.
# chart1 부분
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    st.area_chart(chart_data)


#char2
    chart2_data = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
    columns_2 = alt.Chart(chart2_data).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.altair_chart(columns_2, use_container_width=True)





if __name__ == "__main__":
    write()