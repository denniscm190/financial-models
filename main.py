import numpy as np
import pandas as pd
from request_data import request_data
from plot import *

# Change URL to request other product
historical_df = request_data(
    'https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1410912000&period2=1609027200'
    '&interval=1d&events=history&includeAdjustedClose=true')

# Variables for the simulation
return_std = historical_df['Pct change'].std()  # Compute std of daily pct returns
days = 60
simulations = 1000

# Plot historical daily pct change
historical_plot(data=historical_df['Pct change'], ylabel='Percentage change',
                title='SP500 daily percentage change', grid=True)

# Plot historical histogram
histogram(data=historical_df['Close'], bins=40, color='tab:blue', ylabel='Ticks', xlabel='Price',
          title='SP500 Index - Histogram', grid=True)

estimated_df = pd.DataFrame()  # Empty df for the results
estimated_prices = []

for simulation in range(simulations):
    price = historical_df['Close'][-1]
    simulation_prices = [price]

    for day in range(days):
        price = price * (1 + np.random.normal(0, return_std))
        simulation_prices.append(price)
        estimated_prices.append(price)

    estimated_df['Simulation ' + str(simulation)] = simulation_prices

# Plot Monte Carlo simulations
plot(data=estimated_df, ylabel='Price', xlabel='Day', title='SP500 Index - Monte Carlo simulation', grid=True)

# Plot Monte Carlo histogram
histogram(data=estimated_prices, bins=40, color='tab:green', ylabel='Ticks', xlabel='Price',
          title='SP500 Index - Histogram from Monte Carlo simulation', grid=True)
