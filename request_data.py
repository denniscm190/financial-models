import pandas as pd
import re


def request_data(url):
    product = re.search('v7/finance/download/(.*)\?period', url).group(1)
    df = pd.read_csv(url)
    df = df.set_index('Date')  # Set column Date as index
    df = df['2017'::]  # Select range
    df['Pct change'] = df['Close'].pct_change()

    return df, product
