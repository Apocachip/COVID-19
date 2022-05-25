import streamlit as st
import pandas as pd
import numpy as np
from app_about import run_about
from app_eda import run_eda
from app_home import run_home


def main() :
    menu = ['Home', 'EDA', 'About']

    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        run_home()
    if choice == menu[1] :
        run_eda()
    if choice == menu[2] :
        run_about()
if __name__ == '__main__' :
    main()
