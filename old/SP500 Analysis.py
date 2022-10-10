import pandas as pd

data = pd.read_csv('./SP500 Earnings.csv')
data.Date = pd.to_datetime(data.Date)
data['Open Start'] = '-'
data['Open End'] = '-'
threshold = .05
days_between = 30
count = 0
total_diff = 0
days_to_add = 1

def p2f(x):
    return float(x.strip('%'))/100

for index, row in data.iterrows():
    ticker = row['Ticker']
    date_str = row['Date']
    surprise = row['Surprise %']

    if surprise != '-':
        if p2f(surprise) >= threshold:
            second_data = pd.read_csv('./stock_price/' + ticker + '.csv')
            second_data.Date = pd.to_datetime(second_data.Date)
            matched_result = second_data[second_data['Date'] == date_str]
            matched_result = matched_result.index.to_list()

            if len(matched_result) > 0:
                matched_result = matched_result[0]

                try:
                    data['Open Start'][index] = second_data['Open'][matched_result + days_to_add]
                    data['Open End'][index] = second_data['Open'][matched_result + days_to_add + days_between]

                    open_on_match = second_data['Open'][matched_result + days_to_add]
                    open_days_later = second_data['Open'][matched_result + days_to_add + days_between]
                    diff = open_days_later / open_on_match - 1

                    total_diff += diff
                    count += 1

                    print(total_diff / count)
                except:
                    pass

            del second_data

data.to_csv('./Output.csv')