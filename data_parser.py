"""
Haosen Li
Elliot Liu
This file contains functions for general data parsing purposes.
"""
import re
import os


def get_credentials():
    """
    Returns a dictionary of credentials from an .env file.
    """
    api_key = os.environ.get('api_key')
    praw_client_id = os.environ.get('praw_client_id')
    praw_client_secret = os.environ.get('praw_client_secret')
    praw_user_agent = os.environ.get('praw_user_agent')
    praw_username = os.environ.get('praw_username')
    praw_password = os.environ.get('praw_password')

    return {'api_key': api_key, 'praw_client_id': praw_client_id,
            'praw_client_secret': praw_client_secret,
            'praw_user_agent': praw_user_agent,
            'praw_username': praw_username, 'praw_password': praw_password}


def convert_month(month):
    """
    Takes in a str month, returns an int representing the month.
    If the given month does not match, returns None
    """
    month = month.lower()
    months = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
              'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9,
              'october': 10, 'november': 11, 'december': 12}

    for mon in months.keys():
        if month in mon:
            return months[mon]
    return None


def parse_symbol(files):
    """
    Takes in a list of str directories containing information on
    stock tickers and company names. Returns a normalized set
    of all stock tickers.
    """
    stock_list = set()
    for file in files:
        with open(file) as f:
            for line in f.readlines():
                ticker = re.sub(r'\W+', '', line.split()[0].lower())
                stock_list.add(ticker)
    return stock_list