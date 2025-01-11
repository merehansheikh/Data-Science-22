import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data (assuming the CSV is accessible locally)
try:
    df = pd.read_csv("games.csv")
except FileNotFoundError:
    st.error("Please ensure 'games.csv' is located in the same directory as this script.")
    st.stop()

def run_exploratory_analysis():

    st.title("Exploratory Data Analysis (EDA) of Chess Games")
    st.write("This section explores various aspects of the chess game dataset to gain insights into the data and understand the distribution of features.")

    # Display the first few rows of data
    st.subheader("Data Preview")
    st.write(df.head())

    # Display column names and data types
    st.subheader("Column Information")
    st.write(df.columns)
    st.write(df.info())

    # Display data shape (number of rows and columns)
    st.subheader("Data Shape")
    st.write(f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns.")

    # Display summary statistics (descriptive statistics)
    st.subheader("Descriptive Statistics")
    st.write(df.describe(include='all'))  # Include all data types

    # Buttons to show visualizations
    st.subheader("Visualization Controls")
    opening_button = st.button("Show Opening Name Distribution")
    winner_button = st.button("Show Winner Distribution")
    rating_button = st.button("Show Rating Distributions")
    turns_button = st.button("Show Turns Distribution")
    ply_button = st.button("Show Opening Ply Distribution")
    rating_diff_button = st.button("Show Rating Difference vs. Winner")

    # Show Opening Name Distribution
    if opening_button:
        st.write("This section analyzes the most frequent opening moves played in the dataset.")
        opening_counts = df['opening_name'].value_counts()
        n = 20  # Number of top openings to visualize

        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=opening_counts.head(n).index, y=opening_counts.head(n).values, ax=ax)

        plt.xticks(rotation=90)
        plt.xlabel("Opening Name")
        plt.ylabel("Number of Games")
        plt.title(f"Top {n} Most Played Openings")
        plt.tight_layout()

        st.pyplot(fig)
        st.write("The bar chart above shows the frequency of different opening names in the dataset. Some openings are more popular than others.")

    # Show Winner Distribution
    if winner_button:
        st.write("This chart shows the distribution of game outcomes (white wins, black wins, and draws).")
        winner_counts = df['winner'].value_counts()

        fig, ax = plt.subplots()
        sns.countplot(x='winner', data=df, ax=ax)

        plt.title("Distribution of Game Winners")
        plt.xlabel("Winner")
        plt.ylabel("Number of Games")
        st.pyplot(fig)

    # Show Rating Distributions
    if rating_button:
        st.write("These histograms show the distribution of white and black player ratings. This helps understand the rating range of players in the dataset.")
        fig, axes = plt.subplots(1, 2, figsize=(12, 6)) 
        sns.histplot(df['white_rating'], kde=True, ax=axes[0])
        axes[0].set_title("White Rating Distribution")
        sns.histplot(df['black_rating'], kde=True, ax=axes[1])
        axes[1].set_title("Black Rating Distribution")
        st.pyplot(fig)

    # Show Turns Distribution
    if turns_button:
        st.write("This histogram shows the distribution of the number of turns played in each game. It gives an idea of typical game lengths.")
        fig, ax = plt.subplots()
        sns.histplot(df['turns'], kde=True, ax=ax)
        plt.title("Distribution of Number of Turns")
        plt.xlabel("Number of Turns")
        plt.ylabel("Number of Games")
        st.pyplot(fig)

    # Show Opening Ply Distribution
    if ply_button:
        st.write("This histogram shows the distribution of the number of plies in the opening phase. It indicates how long the opening phase typically lasts.")
        fig, ax = plt.subplots()
        sns.histplot(df['opening_ply'], kde=True, ax=ax)
        plt.title("Distribution of Opening Ply")
        plt.xlabel("Opening Ply")
        plt.ylabel("Number of Games")
        st.pyplot(fig)

    # Show Rating Difference vs. Winner (Boxplot)
    if rating_diff_button:
        df['rating_diff'] = df['white_rating'] - df['black_rating'] # Feature Engineering
        st.write("This boxplot explores the relationship between the rating difference and the game outcome. It can reveal if a larger rating difference correlates with a higher likelihood of winning.")
        
        fig, ax = plt.subplots()
        sns.boxplot(x='winner', y='rating_diff', data=df, ax=ax)
        plt.title("Rating Difference vs. Winner")
        plt.xlabel("Winner")
        plt.ylabel("Rating Difference (White - Black)")
        st.pyplot(fig)

        df.drop('rating_diff', axis=1, inplace=True)  # Dropping the temporary column

if __name__ == "__main__":
    run_exploratory_analysis()
