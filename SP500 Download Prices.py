import yfinance as yf
import pandas as pd
import datetime

data = pd.read_csv('./SP500 Data.csv')
end_date = '2022-09-09'

for index, row in data.iterrows():
    ticker = row['Tickers']
    start_date = datetime.datetime.strptime(row['Min Date'], '%m/%d/%Y').strftime('%Y-%m-%d')

    try:
        # download the stock price
        stock = []
        stock = yf.download(ticker, start=start_date, end=end_date, progress=False)

        # append the individual stock prices
        if len(stock) == 0:
            None
        else:
            stock.to_csv('./stock_price/' + ticker + '.csv')

    except Exception:
        None