import pandas as pd
from pandas.tseries.offsets import MonthEnd
import sys

#Top quantile
quantile_value = 0.20

portfolio_value = 1000

months_behind = 4

long_hit_rate = 0
long_count = 0
short_hit_rate = 0
short_count = 0

df = pd.read_csv('./loughran_mcdonald_score_final.txt', sep='\t')
df.date = pd.to_datetime(df.date)
df = df.sort_values('date')

topic_name = 'net_pos_score'

df['pos_score'] = df.pos_count / df.word_count
df['net_pos_score'] = (df.pos_count - df.neg_count) / df.word_count

#Rolling four-month windows
for beg in pd.date_range('2012-01-01', '2022-04-30', freq='MS'):
    start_date = beg.strftime("%Y-%m-%d")
    end_date = (beg + MonthEnd(months_behind)).strftime("%Y-%m-%d")
    end_date_one_month_later = (beg + MonthEnd(months_behind + 1)).strftime("%Y-%m-%d")

    mask = (df['date'] >= start_date) & (df['date'] <= end_date)
    data_subset = df.loc[mask]
    data_subset = data_subset.drop_duplicates('ticker_from_text', keep='last')

    data_subset_to_buy = data_subset.loc[data_subset[topic_name] >=
                              data_subset[topic_name].quantile(1 - quantile_value)]

    unique_tickers_to_buy = data_subset_to_buy.ticker_from_text.unique()
    length_of_tickers_to_buy = len(unique_tickers_to_buy)
    #length_of_tickers_to_buy = 0

    data_subset_to_short = data_subset.loc[data_subset[topic_name] <=
                              data_subset[topic_name].quantile(quantile_value)]

    unique_tickers_to_short = data_subset_to_short.ticker_from_text.unique()
    length_of_tickers_to_short = len(unique_tickers_to_short)
    #length_of_tickers_to_short = 0

    invest_in_each_ticker = portfolio_value / (length_of_tickers_to_buy + length_of_tickers_to_short)

    for ticker in unique_tickers_to_buy:
        ticker_data = pd.read_csv('./stock_price/%s.csv' % (ticker.replace('.', '-')))
        #ticker_data.Date = pd.to_datetime(ticker_data.Date)
        starting_open_position = ticker_data[ticker_data.Date > end_date].iloc[0]['Open']
        ending_open_position = ticker_data[ticker_data.Date > end_date_one_month_later].iloc[0]['Open']

        long_count += 1
        if ending_open_position >= starting_open_position:
            long_hit_rate += 1

        portfolio_value += invest_in_each_ticker * (ending_open_position / starting_open_position - 1)

    for ticker in unique_tickers_to_short:
        ticker_data = pd.read_csv('./stock_price/%s.csv' % (ticker.replace('.', '-')))
        #ticker_data.Date = pd.to_datetime(ticker_data.Date)
        starting_open_position = ticker_data[ticker_data.Date > end_date].iloc[0]['Open']
        ending_open_position = ticker_data[ticker_data.Date > end_date_one_month_later].iloc[0]['Open']

        gain_on_short = starting_open_position - ending_open_position

        short_count += 1
        if starting_open_position >= ending_open_position:
            short_hit_rate += 1

        portfolio_value += invest_in_each_ticker * gain_on_short / starting_open_position

    print('%s\t%s\t%s\t%s\t%s\t%s' % (end_date_one_month_later, portfolio_value, long_count,
                                      long_hit_rate, short_count, short_hit_rate))