import os
import tweepy
from dotenv import load_dotenv


def environment_variables(filepath: str=None):
    """
    Sets the environment variables from the given `.env` file.
    """
    filepath = filepath or '../.env'
    load_dotenv(filepath)
    

def get_api_keys(filepath: str=None)-> tweepy.Client:
    """
    Return the `tweepy` client with the
    `consumer_key`, `consumer_secret`, `access_token` & `access_secret`.
    """
    environment_variables(filepath)
    
    consumer_key=os.getenv('CONSUMER_KEY')
    consumer_secret=os.getenv("CONSUMER_SECRET")
    access_token=os.getenv("ACCESS_TOKEN")
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    
    # You can provide the consumer key and secret with the access token and access
    # token secret to authenticate as a user
    client = tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret
    )
    
    return client

def get_bearer_token_client(filepath: str=None)-> tweepy.Client:
    """
    Return the `bearer_token` client.
    """
    environment_variables(filepath)
    
    bearer_token = os.getenv('BEARER_TOKEN')
    
    # You can authenticate as your app with just your bearer token
    client = tweepy.Client(bearer_token=bearer_token)
    
    return client