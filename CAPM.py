import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

class CAPM:
    def __init__(self,stocks,start_Date,end_Date):
        self.start_Date=start_Date
        self.end_Date=end_Date
        self.data=None
        self.stocks=stocks
