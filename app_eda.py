import matplotlib
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda() :
    df = pd.read_csv('data/gpu_specs_v6.csv')

    if st.button('기본 데이터프레임 보기'):
        st.dataframe(df)
        if st.button('그만보기') :
            st.write(' ')

    choice_list = st.multiselect('선택한 컬럼만 보기', df.columns)

    if choice_list :
        st.dataframe(df[choice_list])
