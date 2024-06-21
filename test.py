import yfinance as yf
import pandas as pd
import matplotlib as plt
from datetime import date, datetime, timedelta

name = "bhgjhgvjh"

def basic_info(ticker):
#get current date
    today= date.today()
    one_year_ago= today- timedelta(days=365)
    print(ticker)
    # Get all the stock numbers
    stock_num=yf.download(ticker,one_year_ago,today)
    

    last_price=stock_num["Adj Close"].iloc[-1].round(2)
    print(last_price)
    
    #stock text-written data
    stock_info= yf.Ticker(ticker)
    company_name =stock_info.info['longName']

    print(
    f"---------------------------------------------------\n"
    f"|                   Stock Information            |\n"
    f"---------------------------------------------------\n"
    f"| Company Name:          | {company_name}            |\n"
    f"| Ticker Symbol:         | {ticker}                  |\n"
    f"---------------------------------------------------\n"
    f"|                  Current Market Data           |\n"
    f"---------------------------------------------------\n"
    f"| Current Price:         |                       |\n"
    f"| Change (%):            |                       |\n"
    f"| Volume:                |                       |\n"
    f"---------------------------------------------------\n"
    f"|              Historical Performance            |\n"
    f"---------------------------------------------------\n"
    f"| YTD Performance:       |                       |\n"
    f"| 52-Week High:          |                       |\n"
    f"| 52-Week Low:           |                       |\n"
    f"| Max Value:             |                       |\n"
    f"| Average Value:         |                       |\n"
    f"---------------------------------------------------"
)
    



basic_info(name)