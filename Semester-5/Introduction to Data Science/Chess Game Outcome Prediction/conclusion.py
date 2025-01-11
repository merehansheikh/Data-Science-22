import streamlit as st

def write_conclusion():
    st.title("Conclusion")
    st.write("""
        In this analysis, we explored 20,000 chess games, performed EDA, conducted statistical analyses, and built a machine learning model to predict game outcomes.
        The insights gained provide a deeper understanding of chess strategies and player behaviors. 
        Future work could involve analyzing larger datasets, exploring different features, and improving model performance.
    """)
    
    st.subheader("Future Improvements")
    st.write("""
        - **Feature Exploration:** We could further investigate additional features such as player ratings and the impact of different opening strategies.
        - **Model Enhancements:** Trying other machine learning models such as gradient boosting or deep learning could improve accuracy.
        - **Real-time Data Integration:** Integrating real-time data from online chess platforms could provide live predictions during games.
    """)

if __name__ == "__main__":
    write_conclusion()
