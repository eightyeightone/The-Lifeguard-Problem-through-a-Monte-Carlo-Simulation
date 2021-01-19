#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Friday 15 January 2021.
Finished on January 2021. Report to accompany on GitHub (thirythreezero).

@author: h.

References:

"""
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DatetimeIndex as dt
from pandas_datareader import data as wb
from scipy.stats import norm
from datetime import datetime, timedelta
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
# Ticker and time horizon.
stock_ticker = 'TSLA' #SPLV aswell
start_date = '2020-01-01'
end_date = str(datetime.now().strftime('%Y-%m-%d')) # 24hr time conversion of .now().
end_date = '2020-12-31'
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
def clean_stock_data(stock_data, col):
    days = pd.date_range(start=start_date, end=end_date) # Non-trading day.
    cleaned_data = stock_data[col].reindex(days) # Adjusted close (col), etc.
    cleaned_data = cleaned_data.dropna() # Filling all nan values.
    return cleaned_data
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
def vis_stock_data(stock_data, ticker):
    stock_data.info()
    print(f'{ticker} Head: \n {stock_data.head()}')
    print(f'\n{ticker} Tail: \n {stock_data.tail()}')
    return None
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
def pull_stock_data(ticker):
    stock_data = wb.DataReader(ticker, 'yahoo', start_date, end_date)
    #vis_stock_data(stock_data, ticker)
    adj_close = clean_stock_data(stock_data, 'Adj Close')
    return adj_close
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
def stock_data_sample(ticker):
    """
    Here I'll isolate the data so I'm only looking at 80%, the other 20% will
    be used for analysis, i.e. how close was the MCS to the true value?
    """
    total_stock_data = pull_stock_data(ticker)

    eighty_PCT = math.floor((len(total_stock_data) * 0.80))
    twenty_PCT = math.ceil(len(total_stock_data) * 0.20)

    eightyPCT_stock_data = total_stock_data[:eighty_PCT]
    twentyPCT_stock_data = total_stock_data[-twenty_PCT-1:]

    plt.figure(22)
    plt.plot(total_stock_data, 'k', label='100% of Data', linewidth=12)
    plt.plot(eightyPCT_stock_data, 'r', label='In-Sample (80%)')
    plt.plot(twentyPCT_stock_data, 'b', label='Out-of-Sample (20%)')

    plt.title(f'{ticker}: Price Data - Training Splits for Monte Carlo Simulation')
    plt.xlabel('Date (Y-M-D)')
    plt.ylabel('Adjusted Close Price (AUD$)')
    plt.legend()
    plt.grid()

    plt.show()

    return eightyPCT_stock_data, twentyPCT_stock_data, total_stock_data
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
def plot_MCS_stock(ticker):
    data = stock_data_sample(ticker)
    eightyPCT_stock_data = data[0]
    twentyPCT_stock_data = data[1]

    total = data[2]
    total = eightyPCT_stock_data

    log_returns = np.log(1 + total.pct_change())

    drift = log_returns.mean(); # mu (expected return)
    sigma = log_returns.std(); #voltatility, standard deviation

    #sigma = (log_returns.var()/ math.sqrt(math.pi))
    T = 1.0; M = 252; dt = T/M;# derivative of time
    I = 10; # Number of MCS Simulations

    shock = sigma * np.random.standard_normal((M + 1, I)); # shock

    S_t = total.iloc[-1]; # actual stock price when t-1

    F_t = S_t * np.exp(np.cumsum((drift - (0.5 * sigma ** 2) * dt)
    + (math.sqrt(dt) * shock), axis=0))

    start_MCS_date = total.index[-1]

    F_t = pd.DataFrame(F_t, index=pd.date_range(start_MCS_date, periods=M+1))


    plt.figure(44)
    plt.plot(eightyPCT_stock_data, 'r', label='In-Sample (80%)')
    plt.plot(twentyPCT_stock_data, 'b', label='Out-of-Sample (20%)')
    plt.plot(F_t)

    plt.title(f'{ticker}: Price Data - Training Splits for Monte Carlo Simulation')
    plt.xlabel('Date (Y-M-D)')
    plt.ylabel('Adjusted Close Price (AUD$)')
    plt.legend()
    plt.grid()

    plt.show()

    histogram_data = []
    for i in list(range(I)):
        histogram_data.append(total)

    plt.figure(55)
    plt.hist(histogram_data, bins=50)
    plt.show()

    return F_t
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
def MCS_results(ticker):
    F_t = plot_MCS_stock(ticker)
    plt.hist(F_t)
    plt.show()





    return None
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#stock_data_sample(stock_ticker)
plot_MCS_stock(stock_ticker)
#MCS_results(stock_ticker)
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
