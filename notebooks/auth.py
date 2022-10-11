import os
import tweepy
from dotenv import load_dotenv


def authorize(filepath: str)-> tweepy.OAuth1UserHandler:
    """
    Return the `tweepy` authorization handler.
    """
    load_dotenv('../.env')
    
    consumer_key=os.getenv('CONSUMER_KEY')
    consumer_secret=os.getenv("CONSUMER_SECRET")
    access_token=os.getenv("ACCESS_TOKEN")
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    bearer_token=os.getenv("BEARER_TOKEN")
    
    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret,
        access_token, access_token_secret
    )
    
    return auth