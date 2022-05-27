import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/GPUs.csv')

def run_eda() :
    st.title('년도별 그래픽카드 성능 증가율')
    
    if st.button('전체 데이터 보기') :
        st.dataframe(df)
        if st.button('닫기') :
            st.text('')

    menu = df['releaseYear'].unique().tolist()

    st.multiselect('년도를 골라주세요(최소2개)', menu)

    