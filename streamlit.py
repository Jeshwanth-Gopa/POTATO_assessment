import streamlit as st
import plotly.express as px
import pandas as pd
from queries import load_data, filter_by_term, tweets_per_day, unique_users, avg_likes, tweet_times_of_day, top_user

# Set up the Streamlit page
st.title('Twitter Search Analysis')
st.write("Search through a dataset of tweets and see interesting statistics and visualizations.")

# File uploader for the TSV file
file_path = r'C:\Users\Dell\assessment\data.tsv'

# Input for the search term
search_term = st.text_input("Enter a word to query:")

if file_path is not None and search_term:
    # Step 1: Load the data
    df = load_data(file_path)

    # Step 2: Filter data based on the search term
    search_df = filter_by_term(search_term, df)

    # Step 3: Display basic statistics in text
    st.header(f"Statistics for the term: {search_term}")
    
    num_unique_users = unique_users(search_df)
    avg_likes_value = avg_likes(search_df)
    top_tweet_user = top_user(search_df)
    
    st.write(f"**Number of unique users**: {num_unique_users}")
    st.write(f"**Average likes per tweet**: {avg_likes_value:.2f}")
    st.write(f"**Top user by number of tweets**: {top_tweet_user}")

    # Step 4: Create plots for more complex queries

    # Tweets per day plot
    tweets_by_day = tweets_per_day(search_df)
    st.subheader("Tweets per day")
    st.line_chart(tweets_by_day)

    # Tweet times of day plot
    tweet_times = tweet_times_of_day(search_df)
    st.subheader("Times of day tweets were posted")
    
    # Convert tweet_times (Pandas Series) to DataFrame for Plotly
    tweet_times_df = pd.DataFrame({
        'Hour': tweet_times.index,
        'Number of Tweets': tweet_times.values
    })

    # Create the Plotly bar chart
    fig = px.bar(
        tweet_times_df, 
        x='Hour', 
        y='Number of Tweets', 
        labels={'Hour': 'Hour of the Day (0-24)', 'Number of Tweets': 'Number of Tweets'}, 
        title=f"Tweet Frequency by Hour of Day for '{search_term}'"
    )

    # Ensure the x-axis shows all hours from 0 to 24
    fig.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1),
        xaxis_range=[0, 24]  # Ensure the axis covers from 0 to 24
    )

    # Show the interactive Plotly chart
    st.plotly_chart(fig)
