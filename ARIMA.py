import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error

# Load the data
def load_data(file_path, date_column, value_column):
    data = pd.read_csv(file_path, parse_dates=[date_column], index_col=date_column)
    return data[value_column]

# Check stationarity using ADF test
def check_stationarity(series):
    result = adfuller(series)
    print(f"ADF Statistic: {result[0]}")
    print(f"p-value: {result[1]}")
    if result[1] > 0.05:
        print("The series is not stationary. Differencing is required.")
        return False
    else:
        print("The series is stationary.")
        return True

# Fit ARIMA model
def fit_arima(series, order):
    model = ARIMA(series, order=order)
    model_fit = model.fit()
    print(model_fit.summary())
    return model_fit

# Forecast and plot
def forecast_and_plot(series, model_fit, steps):
    forecast = model_fit.forecast(steps=steps)
    plt.figure(figsize=(10, 6))
    plt.plot(series, label='Original')
    plt.plot(pd.date_range(series.index[-1], periods=steps+1, freq='D')[1:], forecast, label='Forecast', color='red')
    plt.legend()
    plt.show()
    return forecast

# Evaluate model
def evaluate_model(series, model_fit):
    predicted = model_fit.fittedvalues
    actual = series.diff().dropna()
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    print(f"RMSE: {rmse}")

# Main function
def main():
    file_path = input("Enter the file path for your CSV data: ")
    date_column = input("Enter the name of the date column: ")
    value_column = input("Enter the name of the value column: ")
    steps = int(input("Enter the number of steps to forecast: "))

    time_series = load_data(file_path, date_column, value_column)

    # Plot the time series
    time_series.plot(figsize=(10, 6))
    plt.title('Time Series')
    plt.show()

    # Check stationarity
    is_stationary = check_stationarity(time_series)

    # Make the series stationary if needed
    if not is_stationary:
        time_series = time_series.diff().dropna()

    # ARIMA parameters
    p = int(input("Enter the AR (p) value: "))
    d = int(input("Enter the I (d) value: "))
    q = int(input("Enter the MA (q) value: "))

    # Fit ARIMA model
    model_fit = fit_arima(time_series, (p, d, q))

    # Evaluate model
    evaluate_model(time_series, model_fit)

    # Forecast and plot
    forecast = forecast_and_plot(time_series, model_fit, steps)
    print("Forecasted values:")
    print(forecast)

if __name__ == "__main__":
    main()
