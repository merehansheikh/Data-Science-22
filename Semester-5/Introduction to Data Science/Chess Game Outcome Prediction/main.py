import streamlit as st
from statistical_comparison import perform_statistical_comparison as stats_app
from ml_model import perform_ml_modeling as ml_app
from eda import run_exploratory_analysis as eda_app
from introduction import write_introduction as intro_app
from conclusion import write_conclusion as conclusion_app
#from streamlit_navigation_bar import st_navbar

PAGES = {
    "Introduction": intro_app,
    "EDA": eda_app,
    "Statistical Analysis": stats_app,
    "Machine Learning": ml_app,
    "Conclusion": conclusion_app,
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to:", list(PAGES.keys()))
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()
