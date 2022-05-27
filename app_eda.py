import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

df = pd.read_csv('data/GPUs.csv')
img = Image.open('data/GPU.jpg')
img_mask = np.array(img)
gpu_names = ' '.join(i for i in df['productName'].astype(str))
stopwords = set(STOPWORDS)
wc = WordCloud(background_color='white', mask= img_mask, stopwords= stopwords).generate(gpu_names)

def run_eda() :
    st.title('탐색적 데이터 분석')

    radio_menu = ['전체 데이터 보기', '통계치']
    selected = st.radio('선택하세요.', radio_menu)

    if selected == radio_menu[0] :
        st.dataframe(df)
    elif selected == radio_menu[1] :
        st.dataframe(df.describe())

    col_list = df.columns[ 2 :]
    selected_col = st.selectbox('컬럼별 최대값, 최소값', col_list)

    if selected_col :

        df_max = df.loc[df[selected_col] == df[selected_col].max() , ]
        df_min = df.loc[df[selected_col] == df[selected_col].min() , ]
        st.dataframe(df_max)
        st.dataframe(df_min) 

    if st.button('워드클라우드 보기') :
        plt.figure(figsize= (10, 6))
        plt.imshow(wc)
        plt.tight_layout(pad=0)
        plt.axis('off')
        plt.show()
        st.pyplot()
        if st.button('닫기') :
            st.text(' ')

    