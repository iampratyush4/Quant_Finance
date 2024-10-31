import yfinance as yf

def fetch_stock_data(stock_ticker):
    # Fetch stock data
    stock = yf.Ticker(stock_ticker)
    
    # Basic information
    info = stock.info
    print(f"Company: {info.get('longName')}")
    print(f"Sector: {info.get('sector')}")
    print(f"Industry: {info.get('industry')}")
    print(f"Market Cap: ₹{info.get('marketCap') / 1e7:.2f} Cr")
    
    # Historical data for the last 10 years
    historical_data = stock.history(period='10y', interval='1mo')
    print("\nSample Historical Data (Last 5 entries):")
    print(historical_data.tail(5))
    
    # Fetch revenue and earnings data
    financials = stock.financials
    print("\nRecent Financials (Revenue):")
    print(financials.loc['Total Revenue'])
    
    # Retrieve Net Income from the income statement
    income_statement = stock.income_stmt
    if 'Net Income' in income_statement.index:
        print("\nAnnual Net Income:")
        print(income_statement.loc['Net Income'])
    else:
        print("\nAnnual Net Income data not available.")

# Example usage
fetch_stock_data('TCS.NS')  # For TCS on NSE
