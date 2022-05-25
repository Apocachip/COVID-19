from re import L
import streamlit as st
from PIL import Image

def run_home() :
    st.title('NVIDIA & AMD 그래픽카드 비교 앱')
    st.text('글카가 금 값이네...')
    
    img = Image.open('data/goldbar.jpg')

    st.image(img)