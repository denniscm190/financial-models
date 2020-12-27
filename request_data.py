import pandas as pd


def request_data(url):
    df = pd.read_csv(url)
    df = df.set_index('Date')  # Set column Date as index
    df = df['2017'::]  # Select range
    df['Pct change'] = df['Close'].pct_change()

    return df
