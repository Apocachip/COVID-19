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

    if st.button('워드클라우드 보기') :
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

    