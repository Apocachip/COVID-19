import streamlit as st
import pandas as pd
import numpy as np

def run_compare() :
    df = pd.read_csv('data/GPU.csv')

    m_columns = df['manufacturer'].unique()
    col_menu1 = m_columns.tolist()

    col1, col2 = st.columns(2)

    choice_manufacturer = col1.selectbox('제조사 선택1', col_menu1)

    if choice_manufacturer :
        col1.text(choice_manufacturer + '을/를 선택하셨습니다.')
        
        name_menu1 = df.loc[df['manufacturer'].str.lower() == choice_manufacturer.lower()]['productName']
        
        choice_graphic_card = col1.selectbox('그래픽카드 선택', name_menu1)

        if choice_graphic_card :
            now_product = df.loc[df['manufacturer'].str.lower() == choice_manufacturer.lower()]

            product_choice = now_product.loc[now_product['productName'].str.lower() == choice_graphic_card.lower()]
            
            st.text('그래픽카드 1')

            st.dataframe(product_choice)
        
        choice_manufacturer2 = col2.selectbox('제조사 선택2', col_menu1)

        if choice_manufacturer2 :
            col2.text(choice_manufacturer2 + '을/를 선택하셨습니다.')

        name_menu2 = df.loc[df['manufacturer'].str.lower() == choice_manufacturer2.lower()]['productName']

        choice_graphic_card2 = col2.selectbox('그래픽카드 선택2', name_menu2)

        if choice_graphic_card2 :
            now_product2 = df.loc[df['manufacturer'].str.lower() == choice_manufacturer2.lower()]

            product_choice2 = now_product2.loc[now_product2['productName'].str.lower() == choice_graphic_card2.lower()]

            st.text('그래픽카드 2')

            st.dataframe(product_choice2)
            
# 그래픽카드 이름으로 검색기능
# 그래픽카드 출시일로 검색기능
# 선택1 과 선택2의 성능을 비교하며 선택1 또는 선택2가 높은것은 무엇이며
# 얼마나 차이나고, 같은 년도에 출시한 다른 그래픽카드의 평균과 비교하여
# 선택1 또는 선택2가 평균보다 높은지 낮은지를 나타내주는 것        

# def run_compare() :
#     df = pd.read_csv('data/GPU.csv')

#     m_columns = df['manufacturer'].unique()
#     col_menu1 = m_columns.tolist()
    
#     choice_manufacturer = st.selectbox('제조사 선택', col_menu1)

#     if choice_manufacturer :
#         st.text(choice_manufacturer + '을/를 선택하셨습니다.')

#         name_menu1 = df.loc[df['manufacturer'].str.lower() == choice_manufacturer.lower()]['productName']
        
#         choice_graphic_card = st.selectbox('그래픽카드 선택', name_menu1)

#         if choice_graphic_card :
#             now_product = df.loc[df['manufacturer'].str.lower() == choice_manufacturer.lower()]

#             product_choice = now_product.loc[now_product['productName'].str.lower() == choice_graphic_card.lower()]

#             st.dataframe(product_choice)

#     choice_manufacturer2 = st.selectbox('제조사2 선택', col_menu1)

#     if choice_manufacturer2 :
#         st.text(choice_manufacturer2 + '을/를 선택하셨습니다.')

#         name_menu2 = df.loc[df['manufacturer'].str.lower() == choice_manufacturer2.lower()]['productName']

#         choice_graphic_card2 = st.selectbox('그래픽카드 선택2', name_menu2)

#         if choice_graphic_card2 :
#             now_product2 = df.loc[df['manufacturer'].str.lower() == choice_manufacturer2.lower()]

#             product_choice2 = now_product2.loc[now_product2['productName'].str.lower() == choice_graphic_card2.lower()]

#             st.dataframe(product_choice2)

