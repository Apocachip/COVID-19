import streamlit as st
import pandas as pd
import numpy as np
from app_about import run_about
from app_compare import run_compare
from app_specs import run_specs

def main() :
    menu = ['Home', 'Compare', 'About']

    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        run_specs()
    if choice == menu[1] :
        run_compare()
    if choice == menu[2] :
        run_about()
if __name__ == '__main__' :
    main()
