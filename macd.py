# -*- coding: utf-8 -*-
"""
MACD Graph in Python
"""

from iexfinance import get_historical_data
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

## You can adjust your dates here ##
start = datetime(2018, 1, 2)
end = datetime(2018, 6, 27)

## You can change your stock symbol here ##
stock = 'SPY'

df = pd.DataFrame(get_historical_data(stock, start, end, output_format='pandas'))
dates = df.index.values.tolist()

close_26_ewma = df['close'].ewm(span=26, min_periods=0, adjust=True, ignore_na=True).mean()
close_12_ewma = df['close'].ewm(span=12, min_periods=0, adjust=True, ignore_na=True).mean()
df['26ema'] = close_26_ewma
df['12ema'] = close_12_ewma

df['MACD'] = (df['12ema'] - df['26ema'])

plt.figure(figsize=(7, 12))
plt.subplot(2, 1, 1)
plt.plot(df['close'])
plt.xticks(dates[::10], rotation=45)
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(df['MACD'])
plt.xticks(dates[::10], rotation=45)
plt.grid(True)