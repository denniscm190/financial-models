from models.montecarlo import montecarlo
from plot import *
from request_data import request_data

# Change URL to request other product
historical_df, product = request_data(
    'https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1410912000&period2=1609027200'
    '&interval=1d&events=history&includeAdjustedClose=true')

# Compute model
estimated_df, estimated_prices = montecarlo(data=historical_df)

# Plot historical daily pct change
historical_plot(data=historical_df['Pct change'], ylabel='Percentage change',
                title=product, grid=True)

# Plot historical histogram
histogram(data=historical_df['Close'], bins=40, color='tab:blue', ylabel='Ticks', xlabel='Price',
          title=product + ' - Histogram since ' + historical_df.iloc[0].name, grid=True)

# Plot Monte Carlo simulations
plot(data=estimated_df, ylabel='Price', xlabel='Day', title=product + ' - Monte Carlo simulation', grid=True)

# Plot Monte Carlo histogram
histogram(data=estimated_prices, bins=40, color='tab:green', ylabel='Ticks', xlabel='Price',
          title=product + ' - Histogram from Monte Carlo simulation', grid=True)
