import time
import tweepy
import sqlite3
import pandas as pd

import matplotlib.pyplot as plt

consumer_key="5X8FhSn5xW8fsM0Ellmec8yXw"
consumer_secret="qzdBAvIM1DSyMwKCkFaT6hOHC6gz0ZqiSxM6c8NZi1ROz6EVCr"
access_token="3055207272-Ga25uXvPwayWwbxbwryRxqsNQNS685HteVirOZr"
access_token_secret="05DDeGdw33G10zereIEs08CdxOkeItQXuXxcN02K25pgF"
bearer_token="AAAAAAAAAAAAAAAAAAAAAA0giAEAAAAAAPJN9TbE40IoMRw6%2FjbtA8UWFzQ%3DUXdg0CNIn9kwrnNOBkka8NyMeGFAtigkEIBQnWOthD1wfB5iyE"


def get_recent_tweets_count(query: str, interval: str='hour')-> pd.DataFrame:
    """
    Get recent tweets count for a given query string.

    Args:
        query: A query string to get recent tweets for.
        interval: options are - 'minute', `hour` or `day` 
    
    Returns:
        resulting dataframe of recent tweet counts.
    """
    client = tweepy.Client(bearer_token)

    response = client.get_recent_tweets_count(query, granularity=interval)

    columns = ['start', 'end', 'tweet_count']

    data = [[row['start'], row['end'], row['tweet_count']] for i, row in enumerate(response.data)]

    df = pd.DataFrame(data, columns=columns)

    return df
    

def save_dataframe(df: pd.DataFrame, search_query: str, database: str='tweet_counts.db')-> int:
    """
    Stores the dataframe in the given filename.
    """
    tablename = "{}_{}".format(search_query, time.strftime('%d.%m.%Y_%H.%M.%S'))
    
    with sqlite3.connect(database) as conn:
        out = df.to_sql(tablename, con=conn)
    
    if out is None:
        raise
    
    return out


characters = (
    'Deamon', 'Rhaenyra', 'Targaryen', 'Viserys',
    'Alicent', 'Aegon', 'Aemond', 'Otto', 
    'Ser Criston Cole', 
)

if __name__ == '__main__':
    query = '#HouseOfDragons'

    df = get_recent_tweets_count(query)
    
    
    print()
    new_rows = save_dataframe(df, query)
    if not not new_rows:
        print('Successfully added', new_rows, 'new rows to database.')
    print()

    for query in characters:
        df = get_recent_tweets_count(query)

        save_dataframe(df, query)
    print()

