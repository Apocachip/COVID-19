import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_compare() :
    df = pd.read_csv('data/GPU_Specs_Mark.csv', index_col=False)

    m_columns = df['manufacturer'].unique()
    col_menu1 = m_columns.tolist()

    col1, col2 = st.columns(2)

    choice_manufacturer = col1.selectbox('제조사 선택1', col_menu1)

    choice_manufacturer2 = col2.selectbox('제조사 선택2', col_menu1)

    if choice_manufacturer :
        col1.text(choice_manufacturer + '을/를 선택하셨습니다.')
        
        name_menu1 = df.loc[df['manufacturer'].str.lower() == choice_manufacturer.lower()]['productName']
        
        choice_graphic_card = col1.selectbox('그래픽카드 선택', name_menu1)

        st.text('단위')
        st.text('memSize : GB, memBusWidth : bits, puClock : MHz, memClock : MHz')

        if choice_graphic_card :
            now_product = df.loc[df['manufacturer'].str.lower() == choice_manufacturer.lower()]

            product_choice = now_product.loc[now_product['productName'].str.lower() == choice_graphic_card.lower()]
            
            final_result1 = product_choice.iloc[ : , 1 : ]

            st.text('그래픽카드 1')

            st.dataframe(final_result1)

    if choice_manufacturer2 :
        col2.text(choice_manufacturer2 + '을/를 선택하셨습니다.')

        name_menu2 = df.loc[df['manufacturer'].str.lower() == choice_manufacturer2.lower()]['productName']

        choice_graphic_card2 = col2.selectbox('그래픽카드 선택2', name_menu2)

        if choice_graphic_card2 :
            now_product2 = df.loc[df['manufacturer'].str.lower() == choice_manufacturer2.lower()]

            product_choice2 = now_product2.loc[now_product2['productName'].str.lower() == choice_graphic_card2.lower()]

            final_result2 = product_choice2.iloc[ : , 1 : ]

            st.text('그래픽카드 2')

            st.dataframe(final_result2)

    # st.text('성능비교')
    # fff = pd.concat([final_result1, final_result2])
    # st.dataframe(fff)

    unique_year = df['releaseYear'].unique()
    year_menu = unique_year.tolist()

    slide_years = st.select_slider('연도별 그래픽카드', year_menu)


    if slide_years :
        year_selected = df.loc[slide_years == df['releaseYear']]

        st.dataframe(year_selected)