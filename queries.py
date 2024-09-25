import pandas as pd

def load_data(file_path):
    """
    Load the TSV file into a Pandas DataFrame, keeping only essential columns.
    """
    columns_to_keep = ['text', 'author_id', 'created_at', 'like_count', 'place_id', 
                       'retweet_count', 'reply_count', 'quote_count']
    df = pd.read_csv(file_path, sep='\t', usecols=columns_to_keep)

    df['text'] = df['text'].fillna('')

    df['created_at'] = pd.to_datetime(df['created_at'], utc=True)  
    return df

def filter_by_term(term, df):
    """
    Filter the DataFrame to contain only rows where the search term is in the 'text' column.
    """
    return df[df['text'].str.contains(term, case=False, regex=False)]

# Query Functions
def tweets_per_day(search_df):
    """
    Return a series containing the number of tweets per day containing the term.
    """
    return search_df.groupby(search_df['created_at'].dt.date).size()

def unique_users(search_df):
    """
    Return the count of unique users who posted tweets containing the search term.
    """
    return search_df['author_id'].nunique()

def avg_likes(search_df):
    """
    Return the average number of likes for tweets containing the search term.
    """
    return search_df['like_count'].mean()

def tweet_times_of_day(search_df):
    """
    Analyze what times of day the tweets were posted at.
    Returns the hour of day distribution of the tweets.
    """
    return search_df['created_at'].dt.hour.value_counts().sort_index()

def top_user(search_df):
    """
    Return the user who posted the most tweets containing the term.
    """
    return search_df['author_id'].value_counts().idxmax()

def place_ids(search_df):
    """
    Return a DataFrame of unique place IDs and their count.
    """
    return search_df['place_id'].value_counts()

def run_queries(file_path, search_term):
    """
    Main function that loads the data, 
    ilters by search term 
    and runs all queries.
    """
    # Step 1: Load the data
    df = load_data(file_path)

    # Step 2: Filter the DataFrame for the search term
    search_df = filter_by_term(search_term, df)

    # Step 3: Run queries on the filtered data
    tweets_by_day = tweets_per_day(search_df)
    num_unique_users = unique_users(search_df)
    average_likes = avg_likes(search_df)
    tweet_times = tweet_times_of_day(search_df)
    top_tweet_user = top_user(search_df)
    tweet_place_ids = place_ids(search_df)

    # Step 4: Display Results
    print(f"\nTweets per day:\n{tweets_by_day}")
    print(f"\nNumber of unique users who posted about '{search_term}': {num_unique_users}")
    print(f"\nAverage likes on tweets containing '{search_term}': {average_likes:.2f}")
    print(f"\nTimes of day tweets were posted (by hour):\n{tweet_times}")
    print(f"\nUser with most tweets containing '{search_term}': {top_tweet_user}")
    print(f"\nPlace IDs and their counts for tweets containing '{search_term}':\n{tweet_place_ids}")


file_path = r'C:\Users\Dell\assessment\data.tsv'
search_term = 'Britney' #Just a sample test
run_queries(file_path, search_term)
