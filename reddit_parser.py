"""
Haosen Li
Elliot Liu
This file contains functions for Reddit data parsing purposes.
"""
import data_parser as dp
from time import ctime
import pandas as pd
import praw
import re


def stock_freq(comments, tickers, check_tickers):
    """
    Take in a list of comments, a set of stock tickers, and
    a set of tickers that needs to be checked.
    Returns a sorted Pandas DataFrame of the most talked
    about stocks from the given list of comments.
    """
    stock_count = {}
    for comment in comments:
        for word in comment.split():
            if word.lower() in check_tickers:
                if word[0] != '$' and word != word.upper():
                    break
            word = re.sub(r'\W+', '', word.lower())
            if word in tickers:
                word = word.upper()
                if word not in stock_count:
                    stock_count[word] = 0
                stock_count[word] += 1
    stock_df = pd.DataFrame(stock_count.items(),
                            columns=['Stock Ticker', 'Mention Frequency'])
    return stock_df.sort_values('Mention Frequency', ascending=False)


def filter_submissions(submissions):
    """
    Takes in a dictionary of submissions, returns a filtered dictionary
    containing submission objects for "Daily Discussion Thread".
    """
    fil_submissions = {}
    for title, submission in submissions.items():
        if 'daily discussion thread' in title:
            fil_submissions[title] = submission
    return fil_submissions


def daily_mentions(submissions, tickers, check_tickers):
    """
    Takes in a filtered dictionary of submissions, returns a filtered
    Pandas DataFrame containing rows of most talked about stocks.
    """
    submission_dates = []
    for title, submission in submissions.items():
        date = title[28:]
        token = date.split()
        for i in range(0, 3):
            if i == 0:
                month = dp.convert_month(token[i])
            elif i == 1:
                day = int(token[i][:-1])
            else:
                year = int(token[i])
        comments = []
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, praw.models.MoreComments):
                continue
            comments.append(top_level_comment.body)

        stock_df = stock_freq(comments, tickers, check_tickers)
        max_index = stock_df['Mention Frequency'].idxmax()

        stock_mention = stock_df.loc[max_index, 'Stock Ticker']
        mention_freq = stock_df.loc[max_index, 'Mention Frequency']

        submission_dates.append(
            {'date': f'{str(year)}-{str(month)}-{str(day)}',
             'month': month, 'day': day, 'year': year,
             'most mentioned stock': stock_mention,
             'mention frequency': mention_freq
             }
        )
    return pd.DataFrame(submission_dates)


def submissions_df(submissions):
    """
    Takes in a dictionary of submissions, returns a Pandas
    DataFrame containing information on Reddit Submissions.
    """
    data = []
    for title, submission in submissions.items():
        date = ctime(submission.created_utc)
        token = date.split()
        for i in range(0, 5):
            if i == 1:
                month = dp.convert_month(token[i])
            elif i == 2:
                day = int(token[i])
            elif i == 4:
                year = int(token[i])

        upvotes = submission.score
        comments = submission.num_comments

        data.append(
            {'date': f'{str(year)}-{str(month)}',
             'month': month, 'day': day, 'year': year,
             'post title': title, 'submission': submission,
             'upvotes': upvotes, 'comments': comments
             }
        )
    return pd.DataFrame(data)


def word_freq(comments):
    """
    Take in a list of comments. Returns a sorted Pandas DataFrame
    of the most frequently used word from the given list of comments.
    """
    word_count = {}
    for comment in comments:
        for word in comment.split():
            word = re.sub(r'\W+', '', word.lower())
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1
    word_df = pd.DataFrame(word_count.items(),
                           columns=['Word', 'Frequency'])
    return word_df.sort_values('Frequency', ascending=False)