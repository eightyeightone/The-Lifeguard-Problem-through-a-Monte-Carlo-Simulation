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
from pandas_datareader import data as wb
from scipy.stats import norm
from datetime import datetime
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
# Ticker and time horizon.
stock_ticker = 'TSLA'
start_date = '2020-01-01'
end_date = str(datetime.now().strftime('%Y-%m-%d')) # 24hr time conversion of .now().
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
def clean_stock_data(stock_data, col):
    weekdays = pd.date_range(start=start_date, end=end_date) # Non-trading day.
    cleaned_data = stock_data[col].reindex(weekdays) # Adjusted close (col), etc.
    cleaned_data = cleaned_data.fillna(method='ffill') # Filling all nan values.
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
    #plot_bare_stock(adj_close, ticker)
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
    twentyPCT_stock_data = total_stock_data[-twenty_PCT:]

    dates = total_stock_data.index

    '''
    plt.figure(22)
    plt.plot(total_stock_data, 'k', label='100% of Data', linewidth=12)
    plt.plot(eightyPCT_stock_data, 'r', label='In-Sample (80%)')
    plt.plot(twentyPCT_stock_data, 'b', label='Out-of-Sample (20%)')

    plt.xlim(x[0], x[-1])
    plt.ylim(10,1000)
    plt.title(f'{ticker}: Price Data - Training Splits for Monte Carlo Simulation')
    plt.xlabel('Date (Y-M-D)')
    plt.ylabel('Adjusted Close Price (AUD$)')
    plt.legend()
    plt.grid()

    plt.show()
    '''
    return dates, eightyPCT_stock_data, twentyPCT_stock_data, total_stock_data



'''
For the monte carlo simulation, i want to start it from 80% to 100% and then
plot it over the 20% with say 5 MCS
'''



#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
def plot_bare_stock(stock_data, ticker):
    plt.plot(stock_data, 'r', label=ticker)

    plt.title(f'{ticker}: Price Data')
    plt.xlabel('Date (Y-M-D)')
    plt.ylabel('Adjusted Close Price (AUD$)')
    plt.legend()
    plt.grid()
    plt.show()
    return None
















#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
def plot_MCS_stock(ticker):
    data = stock_data_sample(ticker)
    dates = data[0]
    eightyPCT_stock_data = data[1]
    twentyPCT_stock_data = data[2]

    total = data[3]


    time_elapsed = len(dates)

    price_ratio = (total[-1] / total[1])
    inverse_number_of_years = 365.0 / time_elapsed
    cagr = price_ratio ** inverse_number_of_years - 1

    vol = total.pct_change().std()

    number_of_trading_days = len(dates)
    vol = vol * math.sqrt(number_of_trading_days)



    daily_return_percentages = np.random.normal(cagr/number_of_trading_days, vol/math.sqrt(number_of_trading_days),number_of_trading_days)+1

    price_series = [total[-1]]

    for drp in daily_return_percentages:
        price_series.append(price_series[-1] * drp)


    number_of_trials = 100
    for i in range(number_of_trials):
        daily_return_percentages = np.random.normal(cagr/number_of_trading_days, vol/math.sqrt(number_of_trading_days),number_of_trading_days)+1
        price_series = [total[-1]]

        for drp in daily_return_percentages:
            price_series.append(price_series[-1] * drp)

        plt.plot(price_series)

    

    plt.figure(44)
    # plot MCS
    plt.plot(eightyPCT_stock_data, 'r', label='In-Sample (80%)')
    plt.plot(twentyPCT_stock_data, 'b', label='Out-of-Sample (20%)')

    plt.xlim(dates[0], dates[-1])
    plt.ylim(10,1000)
    plt.title(f'{ticker}: Price Data - Training Splits for Monte Carlo Simulation')
    plt.xlabel('Date (Y-M-D)')
    plt.ylabel('Adjusted Close Price (AUD$)')
    plt.legend()
    plt.grid()

    plt.show()

    return None
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#









#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#pull_stock_data(stock_ticker)
stock_data_sample(stock_ticker)
plot_MCS_stock(stock_ticker)
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
































#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
