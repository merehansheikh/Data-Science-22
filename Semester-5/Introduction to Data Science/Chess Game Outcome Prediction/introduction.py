import streamlit as st

def write_introduction():
    st.title("Chess Game Outcome Prediction")
    st.write("""
        This app explores the prediction of chess game outcomes using a dataset of online chess games. 
        The dataset contains information about 20k games played on lichess.org, a popular online chess server.
        The primary goal of this analysis is to predict the winner of a chess game (white, black, or draw) based on available game features.
    """)

    st.subheader("Dataset Overview")
    st.write("""
        The dataset includes features such as:
        * `turns`: The total number of moves played in the game.
        * `opening_ply`: The number of plies (half-moves) in the opening phase of the game.
        * `game_duration`: The total time elapsed during the game.
        Other features originally included in the dataset, such as player ratings, opening names, ECO codes, and increment codes, were excluded from the final model to explore predictive power using only basic game statistics.
    """)

    st.subheader("Analysis and Modeling")
    st.write("""
        The analysis involved several preprocessing steps:
        * **Feature Engineering:** Creating new features like `game_duration` from timestamps.
        * **Missing Value Imputation:** Handling missing values in numerical features by imputing with the mean.
        * **Outlier Handling:** Using the Interquartile Range (IQR) method with clipping to manage outliers in numerical data.
        * **Feature Scaling:** Standardizing numerical features using StandardScaler to have zero mean and unit variance.
        * **Data Splitting:** Dividing the data into training and testing sets to train and evaluate the model's performance on unseen data.

        A Random Forest Classifier model was chosen for this multi-class classification problem. The model's performance was evaluated using accuracy, precision, recall, F1-score, and a confusion matrix. Learning curves were also generated to assess the model's learning behavior and identify potential overfitting.
    """)

    st.subheader("Key Findings and Insights")
    st.write("""
        The analysis revealed that the number of turns and game duration are moderately strong predictors of the game outcome.
        Further analysis could explore the impact of different hyperparameter settings or the inclusion of other features.
    """)

    st.subheader("App Usage")
    st.write("""
        This Streamlit app allows you to:
        * View the model's performance metrics (classification report, confusion matrix).
        * Visualize feature importances to understand which features are most influential in predicting the winner.
        * Explore the learning curves to understand how the model learns with increasing amounts of data.
    """)

    st.write("This application was created by Gemini.")

# Example usage in your Streamlit app:
write_introduction()
