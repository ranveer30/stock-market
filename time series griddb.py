
import pandas as pd




googf = pd.read_csv("GOOG.csv")


import plotly.graph_objects as go
fig = go.Figure(data=go.Ohlc(x=googf['Date'],
                    open=googf['Open'],
                    high=googf['High'],
                    low=googf['Low'],
                    close=googf['Close']))
fig.show()


googf[["Close"]].plot()



googf[["Volume"]].plot()

googf=googf.ewm(alpha=0.65).mean()

googf['Volume'].plot()

googf['SMA5'] = googf.Close.rolling(5).mean()
googf['SMA20'] = googf.Close.rolling(20).mean()
googf['SMA50'] = googf.Close.rolling(50).mean()


fig = go.Figure(data=[go.Ohlc(x=googf['Date'],
                    open=googf['Open'],
                    high=googf['High'],
                    low=googf['Low'],
                    close=googf['Close'], name = "OHLC"),
                      go.Scatter(x=googf.Date, y=googf.SMA5, line=dict(color='orange', width=1), name="SMA5"),
                      go.Scatter(x=googf.Date, y=googf.SMA20, line=dict(color='green', width=1), name="SMA20"),
                     go.Scatter(x=googf.Date, y=googf.SMA50, line=dict(color='blue', width=1), name="SMA50")])
fig.show()

googf = pd.read_csv("GOOG.csv")

googf['EMA5'] = googf.Close.ewm(span=5, adjust=False).mean()
googf['EMA20'] = googf.Close.ewm(span=20, adjust=False).mean()
googf['EMA50'] = googf.Close.ewm(span=50, adjust=False).mean()


fig = go.Figure(data=[go.Ohlc(x=googf['Date'],
                    open=googf['Open'],
                    high=googf['High'],
                    low=googf['Low'],
                    close=googf['Close'], name = "OHLC"),
                      go.Scatter(x=googf.Date, y=googf.EMA5, line=dict(color='orange', width=1), name="EMA5"),
                       go.Scatter(x=googf.Date, y=googf.EMA20, line=dict(color='green', width=1), name="EMA20"),
                     go.Scatter(x=googf.Date, y=googf.EMA50, line=dict(color='blue', width=1), name="EMA50")])
fig.show()

