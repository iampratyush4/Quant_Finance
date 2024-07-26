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
NUM_PORTFOLIOS=10000


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

def show_mean_variance(returns,weights):
    portfolio_return= np.sum(returns.mean()*weights)*total_trading_Days
    portfolio_volatility=np.sqrt(np.dot(weights.T,np.dot(returns.cov()*total_trading_Days,weights)))
    print("expected portfolio mean(return):", portfolio_return)
    print("expected portfolio volatility(standard deviation):",portfolio_volatility)

def show_portfolios(returns, volatilities):
    plt.figure(figsize=(10, 6))
    plt.scatter(volatilities, returns, c=returns / volatilities, marker='o')
    plt.grid(True)
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')
    plt.colorbar(label='Sharpe Ratio')
    plt.show()


def generate_portfolios(returns):
    portfolio_means = []
    portfolio_risks = []
    portfolio_weights = []

    for _ in range(NUM_PORTFOLIOS):
        w = np.random.random(len(stocks))
        w /= np.sum(w)
        portfolio_weights.append(w)
        portfolio_means.append(np.sum(returns.mean() * w) * total_trading_Days)
        portfolio_risks.append(np.sqrt(np.dot(w.T, np.dot(returns.cov()
                                                          * total_trading_Days, w))))

    return np.array(portfolio_weights), np.array(portfolio_means), np.array(portfolio_risks)
        
    
if __name__=='__main__':
      
        dataset = download_data()

        show_data(dataset)
        log_daily_returns = calc_return(dataset)
        # show_statistics(log_daily_returns)

        pweights, means, risks = generate_portfolios(log_daily_returns)
        show_portfolios(means, risks)



