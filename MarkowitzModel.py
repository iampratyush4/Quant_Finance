# it is a portfolio optimisation model 
# also known as mordern portfolio theory
# it assists in selection of most efficient portfolio by considering various possible portfolios bsed on expectued return (mean) and risk(variance)
# main idea is diversification
# it has  same approch  as black scholes model

# Assumptions of markowitch model
            # 1- returns are normalised
            # 2- investors are risk averse(more risk more return)

# we dont want to include stocks with more corellation . thus want to include uncorellated stocks

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import scipy.optimize as optimization

# stocks to hanle
stocks =['AAPL','WMT','TSLA','GE','AMZN','DB']
total_trading_Days=252

start_date='2012-01-01'
end_date='2017-01-01'

def download_data():
    stock_data={}
    for stock in stocks:
        ticker =yf.Ticker(stock)
        stock_data[stock]=ticker.history(start=start_date,end=end_date)['Close']

    return pd.DataFrame(stock_data)

def show_data(data):
    data.plot(figsize=(10,5))
    plt.show()


def calc_return(data):
    log_return= np.log(data/data.shift(1))
    return log_return[1:]

def show_stats(returns):
    print("mean", returns.mean()*total_trading_Days)
    print("covarianvce",returns.cov()*total_trading_Days)
    
if __name__=='__main__':
    dataset=download_data()
    print(dataset)
    returns=calc_return(dataset)
    print(returns)
    show_stats(returns)
    show_data(dataset)

