# import required libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import certifi

# url for the list of s&p500 stocks
url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
 
def get_stocks():
    # get the raw html, make sure the correct certificate is being used
    response = requests.get(url, verify=certifi.where())
    # parse through the html
    soup = BeautifulSoup(response.text, 'html.parser')
    # get the s&p500 table
    table = soup.find('table', {'id': 'constituents'})
    # store the table into a panda dataframe
    sp500 = pd.read_html(str(table))[0]

    # return the stocks
    return sp500

def get_tickers():
    # get the stocks
    sp500 = get_stocks()
    # get the tickers
    tickers = sp500['Symbol'].tolist()

    # return the tickers
    return tickers
