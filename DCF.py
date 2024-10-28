import yfinance as yf
import numpy as np

def fetch_financial_data(ticker):
    """
    Fetch financial data using yfinance for a given ticker.
    """
    stock = yf.Ticker(ticker)

    # Fetch financial statements
    income_statement = stock.financials
    balance_sheet = stock.balance_sheet
    cash_flow = stock.cashflow

    # Print the available labels to confirm the data
    print("Income Statement Index Labels:", income_statement.index)
    print("Balance Sheet Index Labels:", balance_sheet.index)
    print("Cash Flow Index Labels:", cash_flow.index)

    return income_statement, balance_sheet, cash_flow

def calculate_dcf(ticker, risk_free_rate=0.02, market_return=0.08, beta=1.2, growth_rate=0.03, years=5):
    """
    Calculate the intrinsic value of a stock using the DCF model.
    """
    # Fetch data
    income_statement, balance_sheet, cash_flow = fetch_financial_data(ticker)
    
    # Step 1: Retrieve key financial metrics
    try:
        revenue = income_statement.loc['Total Revenue'].iloc[-1]
        print("Revenue:", revenue)
    except KeyError:
        raise KeyError("Total Revenue data not found in the income statement.")
    
    try:
        ebit = income_statement.loc['EBIT'].iloc[-1] if 'EBIT' in income_statement.index else income_statement.loc['Operating Income'].iloc[-1]
        print("EBIT:", ebit)
    except KeyError:
        raise KeyError("EBIT or Operating Income data not found in the income statement.")

    try:
        depreciation = cash_flow.loc['Depreciation Amortization Depletion'].iloc[-1] if 'Depreciation Amortization Depletion' in cash_flow.index else cash_flow.loc['Depreciation'].iloc[-1]
        print("Depreciation:", depreciation)
    except KeyError:
        depreciation = 0  # Default to 0 if not available
    print("Depreciation:", depreciation)

    # Step 2: Calculate CapEx and Changes in Working Capital
    try:
        capex = -cash_flow.loc['Capital Expenditure'].iloc[-1]  # Capital Expenditure is usually a negative value
    except KeyError:
        capex = 0  # Default to 0 if not available
    print("CapEx:", capex)

    try:
        current_assets = balance_sheet.loc['Total Current Assets'].iloc[-1]
        current_liabilities = balance_sheet.loc['Total Current Liabilities'].iloc[-1]
        change_in_working_capital = current_assets - current_liabilities
    except KeyError:
        change_in_working_capital = 0  # Default to 0 if not available
    print("Change in Working Capital:", change_in_working_capital)

    # Step 3: Calculate Free Cash Flow (FCF)
    tax_rate = 0.21  # Assuming a 21% tax rate
    fcf = (ebit * (1 - tax_rate)) + depreciation - capex - change_in_working_capital
    print("Free Cash Flow:", fcf)

    # Step 4: Project Free Cash Flow for the next N years using a constant growth rate
    fcf_values = [fcf * (1 + growth_rate) ** i for i in range(1, years + 1)]
    print("Projected FCFs:", fcf_values)

    # Step 5: Calculate Terminal Value using the Gordon Growth Model
    try:
        terminal_value = fcf_values[-1] * (1 + growth_rate) / (0.1 - growth_rate)
    except ZeroDivisionError:
        terminal_value = 0
    print("Terminal Value:", terminal_value)

    # Step 6: Calculate the WACC (simplified version using only cost of equity)
    cost_of_equity = risk_free_rate + beta * (market_return - risk_free_rate)
    wacc = cost_of_equity  # Assuming no debt for simplicity
    print("WACC:", wacc)

    # Step 7: Calculate the Present Value of Free Cash Flows
    discounted_fcf = [fcf_value / ((1 + wacc) ** i) for i, fcf_value in enumerate(fcf_values, 1)]
    print("Discounted FCFs:", discounted_fcf)
    
    # Step 8: Calculate the Present Value of Terminal Value
    pv_terminal_value = terminal_value / ((1 + wacc) ** years)
    print("PV of Terminal Value:", pv_terminal_value)
    
    # Step 9: Calculate Enterprise Value (EV)
    ev = sum(discounted_fcf) + pv_terminal_value
    print("Enterprise Value (EV):", ev)

    # Step 10: Calculate Net Debt
    try:
        net_debt = balance_sheet.loc['Total Debt'].iloc[-1] - balance_sheet.loc['Cash Cash Equivalents And Short Term Investments'].iloc[-1]
    except KeyError:
        net_debt = 0  # Default to 0 if not available
    print("Net Debt:", net_debt)

    # Step 11: Calculate Equity Value and Intrinsic Value per Share
    stock = yf.Ticker(ticker)
    shares_outstanding = stock.info.get('sharesOutstanding', 1)  # Default to 1 if not available
    print("Shares Outstanding:", shares_outstanding)

    equity_value = ev - net_debt
    intrinsic_value_per_share = equity_value / shares_outstanding if shares_outstanding != 0 else 0

    return {
        'Enterprise Value': ev,
        'Equity Value': equity_value,
        'Intrinsic Value per Share': intrinsic_value_per_share
    }

# Example usage
ticker = "META"  # Example with Apple Inc.
dcf_result = calculate_dcf(ticker)
print(dcf_result)
