import pandas as pd
import yfinance as yf
from lightweight_charts import Chart
    
if __name__ == '__main__':
    chart = Chart(inner_width=0.5, inner_height=0.5)

    chart2 = chart.create_subchart(position='right', width=0.5, height=0.5)
    chart3 = chart2.create_subchart(position='left', width=0.5, height=0.5)
    chart4 = chart3.create_subchart(position='right', width=0.5, height=0.5)

    chart.watermark('period=5y, interval= 3mo')
    chart2.watermark('period= 5y, interval= 1d')
    chart3.watermark('period= 5y, interval= 1wk')
    chart4.watermark('period= 5y, interval= 1mo')

    msft = yf.Ticker("MSFT")
    df = msft.history(period="5y", interval='3mo')

    nvda = yf.Ticker("MSFT")
    df2 = nvda.history(period="5y", interval='1d')

    aapl = yf.Ticker("MSFT")
    df3 = aapl.history(period="5y", interval='1wk')

    goog = yf.Ticker("MSFT")
    df4 = goog.history(period="5y", interval='1mo')

    # this library expects lowercase columns for date, open, high, low, close, volume
    df = df.reset_index()
    df.columns = df.columns.str.lower()
    df2 = df2.reset_index()
    df2.columns = df2.columns.str.lower()
    df3 = df3.reset_index()
    df3.columns = df3.columns.str.lower()
    df4 = df4.reset_index()
    df4.columns = df4.columns.str.lower()

    chart.set(df)
    chart2.set(df2)
    chart3.set(df3)
    chart4.set(df4)

    chart.show(block=True)