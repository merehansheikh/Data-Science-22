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

def perform_statistical_comparison():
    st.title("Statistical Comparison of White and Black Wins")
    st.write("""
        This section compares various aspects of games won by white and black players. It provides a deeper understanding of 
        player performance and game dynamics.
    """)

    white_wins = df[df['winner'] == 'white']
    black_wins = df[df['winner'] == 'black']

    # Total Games Won (Bar Chart)
    total_games = {'White Wins': len(white_wins), 'Black Wins': len(black_wins)}
    labels = list(total_games.keys())
    values = list(total_games.values())

    # Display numbers and button to show visual
    st.subheader("1. Total Games Won")
    st.write("Total number of games won by each side:")
    st.write(f"**White Wins:** {values[0]}")
    st.write(f"**Black Wins:** {values[1]}")
    if st.button('Show Visual - Total Games Won'):
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.bar(labels, values, color=['lightgray', 'black'])  # Improved color contrast
        ax.set_title('Total Games Won')
        ax.set_ylabel('Number of Games')
        st.pyplot(fig)
        st.write("""
            This bar chart visualizes the number of games won by each player. It provides a quick comparison of overall 
            performance across the two sides.
        """)

    # Distribution of Moves (Box Plot)
    st.subheader("2. Distribution of Moves (Box Plot)")
    if st.button('Show Visual - Distribution of Moves (Box Plot)'):
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.boxplot([white_wins['turns'], black_wins['turns']], labels=['White Wins', 'Black Wins'], notch=True)
        ax.set_title('Distribution of Moves')
        ax.set_ylabel('Number of Moves')
        st.pyplot(fig)
        st.write("""
            This box plot compares the number of moves in games won by white and black players. The box shows the 
            interquartile range (IQR), with the median line and whiskers representing 1.5 times the IQR. Outliers are 
            depicted as individual points.
        """)

    # Distribution of Moves (Histogram)
    st.subheader("3. Distribution of Moves (Histogram)")
    if st.button('Show Visual - Distribution of Moves (Histogram)'):
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(white_wins['turns'], bins=20, alpha=0.5, label='White Wins', color='lightgray')  # Improved color contrast
        ax.hist(black_wins['turns'], bins=20, alpha=0.5, label='Black Wins', color='black')
        ax.set_title('Number of Moves Distribution')
        ax.set_xlabel('Number of Moves')
        ax.set_ylabel('Frequency')
        ax.legend()
        st.pyplot(fig)
        st.write("""
            This histogram shows the distribution of the number of moves across games won by white and black. 
            It provides a clearer view of the frequency of games with varying numbers of moves.
        """)

    # Rating Statistics
    for color in ['white', 'black']:
        winner_df = df[df['winner'] == color]
        opponent_color = 'black' if color == 'white' else 'white'
        ratings = {
            'Min': winner_df[f'{color}_rating'].min(),
            'Max': winner_df[f'{color}_rating'].max(),
            'Avg': winner_df[f'{color}_rating'].mean()
        }

        st.subheader(f"4. {color.capitalize()} Player Ratings when {color.capitalize()} Wins")
        st.write(f"**Min Rating:** {ratings['Min']}")
        st.write(f"**Max Rating:** {ratings['Max']}")
        st.write(f"**Average Rating:** {ratings['Avg']:.2f}")
        if st.button(f'Show Visual - {color.capitalize()} Ratings ({color.capitalize()} Wins)'):
            fig, ax = plt.subplots(figsize=(6, 5))
            ax.bar(ratings.keys(), ratings.values(), color='lightgray' if color == 'white' else 'black')  # Improved color contrast
            ax.set_title(f'{color.capitalize()} Ratings ({color.capitalize()} Wins)')
            ax.set_ylabel('Rating')
            st.pyplot(fig)
            st.write("""
                This bar chart shows the distribution of ratings for the winning player, based on the color of the player 
                and the rating values observed in the games won by that player.
            """)

        opponent_ratings = {
            'Min': winner_df[f'{opponent_color}_rating'].min(),
            'Max': winner_df[f'{opponent_color}_rating'].max(),
            'Avg': winner_df[f'{opponent_color}_rating'].mean()
        }

        st.subheader(f"5. {opponent_color.capitalize()} Player Ratings when {color.capitalize()} Wins")
        st.write(f"**Min Rating:** {opponent_ratings['Min']}")
        st.write(f"**Max Rating:** {opponent_ratings['Max']}")
        st.write(f"**Average Rating:** {opponent_ratings['Avg']:.2f}")
        if st.button(f'Show Visual - {opponent_color.capitalize()} Ratings ({color.capitalize()} Wins)'):
            fig, ax = plt.subplots(figsize=(6, 5))
            ax.bar(opponent_ratings.keys(), opponent_ratings.values(), color='black' if color == 'white' else 'lightgray')  # Improved color contrast
            ax.set_title(f'{opponent_color.capitalize()} Ratings ({color.capitalize()} Wins)')
            ax.set_ylabel('Rating')
            st.pyplot(fig)
            st.write("""
                This chart compares the ratings of the opponent when the current player wins, providing insight into 
                the rating distribution of the defeated player.
            """)

    # Violin Plots (Combined Data)
    combined = pd.concat([white_wins.assign(Result='White Wins'), black_wins.assign(Result='Black Wins')])  # More efficient concatenation
    st.subheader("6. Ratings Distribution by Result (Violin Plot)")
    
    if st.button('Show Visual - White Ratings Distribution by Result'):
        fig, ax = plt.subplots()
        sns.violinplot(x='Result', y='white_rating', data=combined, palette=['lightgray', 'black'], ax=ax)  # Improved color contrast
        ax.set_title('White Ratings Distribution by Result')
        st.pyplot(fig)
        st.write("""
            This violin plot illustrates the distribution of white player ratings, showing the shape, median, 
            and quartiles of the data, separated by whether white won or lost.
        """)

    if st.button('Show Visual - Black Ratings Distribution by Result'):
        fig, ax = plt.subplots()
        sns.violinplot(x='Result', y='black_rating', data=combined, palette=['lightgray', 'black'], ax=ax)  # Improved color contrast
        ax.set_title('Black Ratings Distribution by Result')
        st.pyplot(fig)
        st.write("""
            Similarly, this violin plot shows the distribution of black player ratings, separated by the game result 
            (whether black won or lost). This visualization also combines box plots and density estimation.
        """)

if __name__ == "__main__":
    perform_statistical_comparison()
