# Twitter Search Analysis

This repository contains a Streamlit app that allows users to search through a dataset of tweets, run various queries, and display the results both in text and through interactive visualizations.

## Files

- `streamlit.py`: The main Streamlit application that provides the user interface.
- `queries.py`: Contains the data loading, filtering, and query functions.
- `__init__.py`: Empty file for package initialization.
- `requirements.txt`: The dependencies needed to run the project.
- `README.md`: Instructions on how to use the project.

## Setup and Usage

### 1. Install dependencies

Ensure you have Python installed. Then install the required Python packages by running:

```bash
pip install -r requirements.txt
```

### 2. Prepare the Dataset

The dataset must be in TSV format, containing columns such as:

- `text`: The tweet content.
- `author_id`: The user ID of the tweet author.
- `created_at`: Timestamp when the tweet was posted.
- `like_count`: Number of likes.
- `retweet_count`, `reply_count`, `quote_count`: Tweet query metrics.

Make sure to provide the path to the dataset in the `streamlit.py` file or upload the dataset using the Streamlit app interface.

### 3. Run the Streamlit App

Launch the Streamlit app with:

```bash
streamlit run streamlit.py
```
This will start the application, and you can access it through your browser.

### 4. Using the App
- Upload or specify the path of the TSV dataset in the app.
- Enter your search term (e.g., "Britney").
- The app will display:
  - **Number of unique users**: Count of users who tweeted the term.
  - **Average likes per tweet**: Average likes on those tweets.
  - **Top user**: The user with the most tweets containing the term.
  - **Tweets per day**: A line chart showing daily tweet counts.
  - **Times of day**: An interactive bar chart of tweet posting hours.

### 5. Key Functions
- `load_data(file_path)`: Loads and processes the dataset.
- `filter_by_term(term, df)`: Filters tweets by the search term.
- `tweets_per_day(df)`: Counts tweets per day.
- `unique_users(df)`: Returns unique user count.
- `avg_likes(df)`: Calculates average likes.
- `tweet_times_of_day(df)`: Shows tweet posting hour distribution.
- `top_user(df)`: Identifies the most active user.

### 6. Example
To run a query from the terminal, modify the `file_path` and `search_term` in `query.py`, and execute the script.

```python
from queries import run_queries

file_path = '/pathtoyour/data.tsv'
search_term = 'music'

run_queries(file_path, search_term)
```
This will display statistics and insights about tweets containing the term "music".
