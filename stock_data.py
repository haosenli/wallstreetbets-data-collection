"""
Haosen Li
This file contains the StockData class
"""
import requests
import pandas as pd


class StockData:
    """
    This class provides functions for accessing stock data easily.
    """
    def __init__(self, api_key):
        """
        Initializes the Stock_Data object from a given api key str.
        """
        self._api_key = f'apikey={api_key}'

    def get_curr_price(self, ticker):
        """
        Returns the current stock price as a Pandas DataFrame for the given
        stock. If the request cannot be made, returns an error message.
        """
        response = requests.get(f'https://fmpcloud.io/api/v3/quote/'
                                f'{ticker}?{self._api_key}')
        if response.status_code != 200:
            return 'Error: Request cannot be made'

        return pd.DataFrame(response.json())

    def get_hist_price(self, ticker, interval, start=None, end=None):
        """
        Returns the historical stock price as a Pandas DataFrame for the
        given stock and the given interval type. If the given interval is
        'period', then a start and end date in the format YYYY-MM-DD will be
        necessary. If the request cannot be made, returns an error message.

        The available intervals are:
            - '1min', '5min', '15min', '30min', '1hour', 'daily', 'period'
        """
        if interval == 'daily':
            response = requests.get(f'https://fmpcloud.io/api/v3/'
                                    f'historical-price-full/{ticker}'
                                    f'?serietype=line&{self._api_key}')

        elif interval == 'period':
            response = requests.get(f'https://fmpcloud.io/api/v3/'
                                    f'historical-price-full/{ticker}'
                                    f'?from={start}&to={end}&{self._api_key}')

        else:
            response = requests.get(f'https://fmpcloud.io/api/v3/'
                                    f'historical-chart/{interval}/{ticker}?'
                                    f'{self._api_key}')

        if response.status_code != 200:
            return 'Error: Request cannot be made'

        return pd.DataFrame(response.json())