import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

df = pd.read_csv('data/GPU.csv')
img = Image.open('data/GPU.jpg')
img_mask = np.array(img)
gpu_names = ' '.join(i for i in df['productName'].astype(str))
stopwords = set(STOPWORDS)
wc = WordCloud(background_color='white', mask= img_mask, stopwords= stopwords).generate(gpu_names)

def run_eda() :
    st.title('탐색적 데이터 분석')
    st.subheader('(Exploratory Data Analysis)')

    radio_menu = ['전체 데이터 보기', '통계치']
    selected = st.radio('선택하세요.', radio_menu)

    if selected == radio_menu[0] :
        st.dataframe(df)
    elif selected == radio_menu[1] :
        st.dataframe(df.describe())

    select_menu = ['연도별 GPU출시(최신순)', '연도별 GPU출시(많은순)']
    select_box = st.selectbox('선택하여 보기', select_menu)

    if select_box == select_menu[0] :
        df['releaseYear'].value_counts().sort_index(ascending=False).plot.bar()
        plt.title('2005 - 2023 Released GPU')
        plt.xlabel('Year')
        plt.ylabel('GPUs Count')
        plt.show()
        st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)

    elif select_box == select_menu[1] :
        df['releaseYear'].value_counts().plot.bar()
        plt.title('2005 - 2023 Released GPU')
        plt.xlabel('Year')
        plt.ylabel('GPUs Count')
        plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
        
    if st.button('워드클라우드') :
        fig = plt.figure(figsize=(10, 6))
        plt.imshow(wc)
        plt.tight_layout(pad=0)
        plt.axis('off')
        plt.show()
        st.pyplot(fig)
        if st.button('닫기') :
            st.text(' ')
    if st.button('사용한 이미지') :
        st.image(img)
        if st.button('닫기') :
            st.text('')

    