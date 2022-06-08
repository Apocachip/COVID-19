import streamlit as st

def run_home() :
    st.title('그래픽카드 비교')
    st.subheader('각 제조사별로 그래픽카드를 비교하여 볼수 있는 앱')

    st.text('productNmae - 해당하는 제조사의 그래픽카드 이름 (제품이름)')
    st.text('releaseYear - 그래픽카드의 출시일 또는 예정일')