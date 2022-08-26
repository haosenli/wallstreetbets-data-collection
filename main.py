"""
Haosen Li
Elliot Liu
CSE 163 Final Project

This file contains the main function for running an analysis
on the WallStreetBets Subreddit.
"""
from reddit_sort import RedditSort
from stock_data import StockData
from dotenv import load_dotenv
import data_visualizer as dv
import reddit_parser as rp
import data_parser as dp

# Due to a limitation in the PRAW API, this program cannot
# request more than 1000 Reddit submissions at a time.
# Therefore, please enter the current month.
CURRENT_MONTH = 'June'
SUBMISSION_LIMIT = None

STOCK_TICKERS = ['nyse_stock.txt', 'nasdaq_stock.txt']
CHECK_TICKERS = {'you', 'a', 'it', 'is', 'on', 'ago', 'for', 'are', 'so',
                 'be', 'me', 'all', 'go', 'up', 'nice', 'man', 'good',
                 'well', 'hope', 'out', 'iq', 'leg', 'now', 'can', 'huge',
                 'pets', 'am', 'by', 'has', 'see', 'back', 'or', 'open',
                 'one', 'else', 'love', 'new', 'it', 'he', 'any', 'next',
                 'lmao', 'life', 'work', 'pump', 'play', 'old', 'low', 'wow',
                 'big', 'cash', 'run', 'joe', 'go', 'u', 'best', 'well',
                 'tell', 'bill', 'two', 'fly', 'very', 'move', 'turn', 'so'}


def main():
    load_dotenv()
    cred = dp.get_credentials()
    api_key = cred.pop('api_key')
    praw_keys = cred

    print('This program is now analyzing ' +
          'the Reddit Discussion Board WallStreetBets!')

    print('   Processing Reddit submissions...')
    r_sort = RedditSort('wallstreetbets', praw_keys)
    submissions = r_sort.get_submissions(SUBMISSION_LIMIT)
    filtered_submissions = rp.filter_submissions(submissions)
    print('   Finished processing Reddit submissions...')

    print('   Creating plots...')
    df1 = rp.daily_mentions(filtered_submissions,
                            dp.parse_symbol(STOCK_TICKERS), CHECK_TICKERS)
    df2 = rp.submissions_df(submissions)

    dv.daily_stock(df1, CURRENT_MONTH, 2021)
    dv.subreddit_activity(df2, CURRENT_MONTH)
    print('   Finished creating plots...')

    # ***Comment/Uncomment the following lines for a stock's price history***

    # ticker = 'SOFI'
    # start_date = '2021-08-01'
    # end_date = '2021-08-20'
    # print(f'   Retrieving information on {ticker}...')
    # get_historical_price(ticker, start_date, end_date, api_key)
    # print(f'   Finished retrieving information on {ticker}...')

    # ***Comment/Uncomment the following lines to see what is the most commonly
    # used word in WallStreetBets, just for fun.***
    # (WARNING: EXTREMELY LONG COMPUTE TIMES)

    # print('   Getting comments...')
    # comments = r_sort.get_comments(submissions)
    # print('   Finished getting comments...')
    # print('   Finding most commonly used words...')
    # print(rp.word_freq(comments))
    # print('   Finished finding most commonly used words...')


def get_historical_price(ticker, start, end, api_key):
    """
    Returns a Pandas DataFrame from the given stock ticker, start date,
    end date, and api key. The dates should be in 'yyyy-mm-dd' format.
    """
    stock = StockData(api_key)
    print(stock.get_hist_price(ticker, 'period', start, end))


if __name__ == '__main__':
    main()