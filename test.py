"""
Haosen Li
Elliot Liu
This file contains functions used for testing various classes and functions.
"""
from reddit_sort import RedditSort
import data_visualizer as dv
import reddit_parser as rp
import data_parser as dp

STOCK_TICKERS = ['nyse_stock.txt', 'nasdaq_stock.txt']
CHECK_TICKERS = {'you', 'a', 'it', 'is', 'on', 'ago', 'for', 'are', 'so',
                 'be', 'me', 'all', 'go', 'up', 'nice', 'man', 'good',
                 'well', 'hope', 'out', 'iq', 'leg', 'now', 'can', 'huge',
                 'pets', 'am', 'by', 'has', 'see', 'back', 'or', 'open',
                 'one', 'else', 'love', 'new', 'it', 'he', 'any', 'next',
                 'lmao', 'life', 'work', 'pump', 'play', 'old', 'low', 'wow',
                 'big', 'cash', 'run', 'joe', 'go', 'u', 'best', 'well',
                 'tell', 'bill', 'two', 'fly', 'very', 'move', 'turn', 'so'}


def test_stock_data(stock):
    """
    Tests the Stock_Data class with the given
    Stock_Data object.
    """
    data = []
    # data.append(stock.get_curr_price('GME'))
    # data.append(stock.get_hist_price('GME', '1hour'))
    # data.append(stock.get_hist_price('GME', 'daily'))
    data.append(stock.get_hist_price('GME', 'period', '2021-08-01',
                                     '2021-08-13'))

    for stock_data in data:
        print(stock_data)
        print()


def test_reddit_sort(praw_keys):
    """
    Tests the RedditSort class
    """
    print('Testing RedditSort...')
    r_sort = RedditSort('wallstreetbets', praw_keys)
    submissions = r_sort.get_submissions(200)
    # filtered_submissions = rp.filter_submissions(submissions)

    # print(rp.daily_mentions(filtered_submissions,
    #       dp.parse_symbol(STOCK_TICKERS), CHECK_TICKERS))

    print(rp.submissions_df(submissions))

    # comments = r_sort.get_comments(submissions)
    # filtered_comments = r_sort.get_comments(filtered_submissions)

    # stock_mentions = dp.stock_freq(filtered_comments,
    #                                dp.parse_symbol(STOCK_TICKERS),
    #                                CHECK_TICKERS)
    # print(stock_mentions)
    # with pd.option_context('display.max_rows', None,
    #                        'display.max_columns', None):
    #     print(stock_mentions)
    # print(dp.word_freq(comments))


def test_data_visualizer(praw_keys):
    """
    tests the data_visualizer functions
    """
    r_sort = RedditSort('wallstreetbets', praw_keys)
    submissions = r_sort.get_submissions(None)
    filtered_submissions = rp.filter_submissions(submissions)
    df = rp.daily_mentions(filtered_submissions,
                           dp.parse_symbol(STOCK_TICKERS), CHECK_TICKERS)
    # df = rp.submissions_df(submissions)

    dv.daily_stock(df, 'august', 2021)
    # dv.subreddit_activity(df, 'August')


def main():
    # load_dotenv()
    # retrieve credentials for APIs
    # cred = dp.get_credentials()
    # api_key = cred.pop('api_key')
    # praw_keys = cred

    # StockData tests
    # stock = StockData(api_key)
    # test_stock_data(stock)

    # RedditSort tests
    # test_reddit_sort(praw_keys)

    # data visualizer test
    # test_data_visualizer(praw_keys)

    # symbol parse test
    # print(dp.parse_symbol(STOCK_TICKERS))
    pass


if __name__ == '__main__':
    main()