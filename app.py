import streamlit as st
import pandas as pd
import numpy as np


def main() :
    st.title('코로나 예측')

    country_df = pd.read_csv('data/country_wise_latest.csv')

    if st.checkbox('기본 데이터프레임 보기'):
        st.dataframe(country_df)










if __name__ == '__main__' :
    main()
