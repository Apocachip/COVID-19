import streamlit as st
import pandas as pd
import numpy as np

def run_compare() :
    st.subheader('비교하기')

    df = pd.read_csv('data/GPU.csv')

    m_columns = df['manufacturer'].unique()
    menu = m_columns.tolist()
    
    choice_manufacturer = st.selectbox('제조사 선택', menu)


    if choice_manufacturer :
        st.text(choice_manufacturer + '을/를 선택하셨습니다.')

        menu2 = df.loc[df['manufacturer'].str.contains(choice_manufacturer)]['productName']
        
        choice_graphic_card = st.selectbox('그래픽카드 선택', menu2)

        if choice_graphic_card :
            now_product = df.loc[df['manufacturer'].str.contains(choice_manufacturer)]

            product_choice = now_product.loc[now_product['productName'].str.contains(choice_graphic_card)]

            st.dataframe(product_choice)

            choice_manufacturer2 = st.selectbox('제조사2 선택', menu)

    if choice_manufacturer2 :
        st.text(choice_manufacturer2 + '을/를 선택하셨습니다')

        menu3 = df.loc[df['manufacturer'].str.contains(choice_manufacturer2)]['productName']

        choice_graphic_card2 = st.selectbox('그래픽카드 선택2', menu3)

        if choice_graphic_card2 :
            now_product2 = df.loc[df['manufacturer'].str.contains(choice_manufacturer2)]

            product_choice2 = now_product2.loc[now_product2['productName'].str.contains(choice_graphic_card2)]

            st.dataframe(product_choice2)

    # st.text('선택1 과 선택2의 성능을 비교하며 선택1 또는 선택2가 높은것은 무엇이며,')
    # st.text('얼마나 차이나고, 같은 년도에 출시한 다른 그래픽카드의 평균과 비교하여')
    # st.text('선택1 또는 선택2가 평균보다 높은지 낮은지를 나타내주는 것') 