# import required libraries
from .fetch import get_stocks, get_tickers
import yfinance as yf
import pandas as pd

def process_data():
    # get the stocks and tickers for the s&p500
    tickers = get_tickers()
    stocks = get_stocks()
    stocks.set_index('Symbol', inplace=True)

    # list that stores each ticker until its put in a panda
    data_list = []

    # loop through all of the tickers
    for ticker in tickers[:10]:
        # make sure to only process the valid tickers
        try:
            # get the history and sort it, newest on top
            symbol = yf.Ticker(ticker)
            history = symbol.history(period='1mo')
            history.sort_index(ascending=False, inplace=True)

            # get the open and close for the day
            open_day = history.loc[history.index[0], 'Open'].round(2)
            close_day = history.loc[history.index[0], 'Close'].round(2)

            # get the day change
            day_change = -(open_day - close_day).round(2)
            percent_day_change = ((day_change / open_day) * 100).round(2)

            # get the open a month ago
            open_month = history.loc[history.index[-1], 'Open'].round(2)

            # get the month change
            month_change = -(open_month - close_day).round(2)
            percent_month_change = ((month_change / open_month) * 100).round(2)

            ticker_data = {
                'Ticker' : ticker,
                'Day Change' : day_change,
                'Percent Day Change' : percent_day_change,
                'Month Change' : month_change,
                'Percent Month Change' : percent_month_change,
                'Location' : stocks.loc[str(ticker), 'Headquarters Location'],
                'Sector' : stocks.loc[str(ticker), 'GICS Sector']
            }

            data_list.append(ticker_data)

        # error checks
        except KeyError as ke:
            print(f'key error for {ticker}: {ke}')

        except Exception as e:
            print(f'error for {ticker}: {e}')

    processed = pd.DataFrame(data_list)

    return processed

# function that separates each stock into a dataframs by the sector
def by_sector():
    # processed data
    processed = process_data()
    
    # get the unique sectors
    uniques = processed['Sector'].unique()

    # list that will hold data frames for each sector
    sectors = []

    # iterate through the sectors and make data frames for each one
    for sector in uniques:
        try:
            temp = processed.loc[processed['Sector'] == sector]
            sectors.append(temp)
        except Exception as e:
            print(f'error {e}')

    return uniques, sectors
