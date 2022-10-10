import codecs, sys
import pandas as pd

def write_to_file(file_name, data):
    with codecs.open("./" + file_name, "a", "utf-8") as f:
        f.write(data)

def read_file(file_name):
    data = list()
    line_count = 0
    ticker = ''

    with codecs.open(file_name, encoding='utf-8') as f:
        for line in f:
            line_count += 1

            if ticker == '':
                ticker_from_text = line.rstrip('\r').rstrip('\n')
                if not 'start' in ticker_from_text.lower():
                    ticker = ticker_from_text[ticker_from_text.find("(")+1:ticker_from_text.find(")")]
                    if ':' in ticker:
                        ticker = ticker.split(':')[-1]

            result = line.rstrip('\r').rstrip('\n').lower().split('.')
            data.append(result)

    return data, ticker

revenue_word_list = {'sales', 'revenue', 'top line', 'top bottom line', 'net revenue', 'organic revenue growth',
                     'organic sales growth', 'operational sales'}
earnings_word_list = {'eps', 'earnings', 'earnings per share', 'net income', 'bottom line', 'top bottom line'}
profitability_word_list = {'margin', 'gross margin', 'operating margin', 'return invested capital', 'return capital'}
operating_income_word_list =  {'ebit', 'operating income', 'operating profit', 'operating earning'}
cash_flow_word_list = {'cash flow', 'operating cash flow', 'cash flow operations', 'free cash flow'}
shareholder_return_word_list = {' buyback', 'dividends', 'dividend per share', 'share repurchase', 'repurchased million shares'}
positive_word_list = {'increase', 'increased', 'increases', 'increasing', 'increasingly', 'expand',
                       'expanded', 'expanding', 'expands', 'expansion', 'expansions', 'grow',
                       'grows', 'grew', 'growth', 'growths', 'improve', 'improved', 'improves',
                       'improvement', 'improvements', 'strong', 'stronger', 'strongest', 'strongly'}
negative_word_list = {'decline', 'declined', 'declines', 'declining', 'deteriorate', 'deteriorates',
                      'deteriorated', 'deteriorating', 'compress', 'compressed', 'compresses',
                      'compressing', 'compressible', 'compression', 'reduce', 'reduces', 'reduced',
                      'reducing', 'reduction', 'reductions', 'weak', 'weaker', 'weakest', 'weaken',
                      'weakens', 'weakened', 'weakening', 'weakness', 'weaknesses'}
guidance_word_list = {'full year outlook', 'full year expect', 'guidance', 'outlook', 'forecast',
                      'expect', 'expects', 'expected', 'expecting', 'expectation', 'expectations'}

stock_tickers = pd.read_csv('./earnings_to_search.csv')

write_to_file('./net_topic_postive_score.txt', '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %
    ('article_link', 'ticker', 'date', 'ticker_from_text', 'rev_and_earnings_positive_sentence_score',
    'rev_and_earnings_negative_sentence_score', 'rev_and_earnings_profit_positive_sentence_score',
    'rev_and_earnings_profit_negative_sentence_score', 'rev_positive_sentence_score',
    'rev_negative_sentence_score', 'earnings_positive_sentence_score',
    'earnings_negative_sentence_score'))

for index, row in stock_tickers.iterrows():
    article_link = row['article']
    ticker = row['ticker']
    date = row['date']

    try:
        text_data, ticker_from_text = read_file('.%s.txt' % article_link)
        sentence_count = 0
        revenue_sentence_count = 0
        earnings_sentence_count = 0
        rev_and_earnings_sentence_count = 0
        rev_and_earnings_profit_sentence_count = 0

        rev_positive_sentence_count = 0
        rev_negative_sentence_count = 0

        earnings_positive_sentence_count = 0
        earnings_negative_sentence_count = 0

        rev_and_earnings_positive_sentence_count = 0
        rev_and_earnings_profit_positive_sentence_count = 0

        rev_and_earnings_negative_sentence_count = 0
        rev_and_earnings_profit_negative_sentence_count = 0

        start = False
        end = False

        if len(text_data) > 0:
            for text in text_data:
                for sentence in text:
                    if not start:
                        if sentence == 'unknown speaker' or \
                                sentence == 'operator' or 'good' in sentence or \
                                'hello' in sentence or 'thank' in sentence or \
                                'welcome' in sentence:
                            start = True

                    if sentence == 'question-and-answer session':
                        end = True
                        break

                    if start and not end:
                        sentence_count += 1

                        revenue_count = 1 if any(word.strip() in sentence for word in revenue_word_list) else 0
                        earnings_count = 1 if any(word.strip() in sentence for word in earnings_word_list) else 0
                        profitability_count = 1 if any(word.strip() in sentence for word in profitability_word_list) else 0
                        #operating_income_count = 1 if any(word.strip() in sentence for word in operating_income_word_list) else 0
                        #cash_flow_count = 1 if any(word.strip() in sentence for word in cash_flow_word_list) else 0
                        #shareholder_return_count = 1 if any(word.strip() in sentence for word in shareholder_return_word_list) else 0
                        positive_count = 1 if any(word.strip() in sentence for word in positive_word_list) else 0
                        negative_count = 1 if any(word.strip() in sentence for word in negative_word_list) else 0
                        guidance_count = 1 if any(word.strip() in sentence for word in guidance_word_list) else 0

                        if revenue_count > 0:
                            revenue_sentence_count += 1

                        if earnings_count > 0:
                            earnings_sentence_count += 1

                        if revenue_count > 0 and earnings_count > 0:
                            rev_and_earnings_sentence_count += 1

                            if profitability_count > 0:
                                rev_and_earnings_profit_sentence_count += 1

                        net_positive_count = positive_count - negative_count

                        #print(revenue_count, earnings_count, profitability_count, net_positive_count, guidance_count)

                        if net_positive_count > 0:
                            if revenue_count > 0:
                                rev_positive_sentence_count += 1

                            if earnings_count > 0:
                                earnings_positive_sentence_count += 1

                            # if sum([revenue_count, earnings_count, profitability_count, operating_income_count, cash_flow_count, shareholder_return_count]) >= 2:
                            if revenue_count > 0 and earnings_count > 0:
                                rev_and_earnings_positive_sentence_count += 1

                                if profitability_count > 0:
                                    rev_and_earnings_profit_positive_sentence_count += 1

                        elif net_positive_count < 0:
                            if revenue_count > 0:
                                rev_negative_sentence_count += 1

                            if earnings_count > 0:
                                earnings_negative_sentence_count += 1

                            #if sum([revenue_count, earnings_count, profitability_count, operating_income_count, cash_flow_count, shareholder_return_count]) >= 2:
                            if revenue_count > 0 and earnings_count > 0:
                                rev_and_earnings_negative_sentence_count += 1

                                if profitability_count > 0:
                                    rev_and_earnings_profit_negative_sentence_count += 1

            if revenue_sentence_count == 0: revenue_sentence_count = 1
            if earnings_sentence_count == 0: earnings_sentence_count = 1
            if rev_and_earnings_sentence_count == 0: rev_and_earnings_sentence_count = 1
            if rev_and_earnings_profit_sentence_count == 0: rev_and_earnings_profit_sentence_count = 1

            rev_positive_sentence_score = rev_positive_sentence_count / sentence_count #revenue_sentence_count
            rev_negative_sentence_score = rev_negative_sentence_count / sentence_count #revenue_sentence_count

            earnings_positive_sentence_score = earnings_positive_sentence_count / sentence_count #earnings_sentence_count
            earnings_negative_sentence_score = earnings_negative_sentence_count / sentence_count #earnings_sentence_count

            rev_and_earnings_positive_sentence_score = rev_and_earnings_positive_sentence_count / sentence_count #rev_and_earnings_sentence_count
            rev_and_earnings_profit_positive_sentence_score = rev_and_earnings_profit_positive_sentence_count / sentence_count #rev_and_earnings_sentence_count

            rev_and_earnings_negative_sentence_score = rev_and_earnings_negative_sentence_count / sentence_count #rev_and_earnings_profit_sentence_count
            rev_and_earnings_profit_negative_sentence_score = rev_and_earnings_profit_negative_sentence_count / sentence_count #rev_and_earnings_profit_sentence_count

            write_to_file('./net_topic_postive_score.txt', '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %
                          (article_link, ticker, date, ticker_from_text, rev_and_earnings_positive_sentence_score,
                           rev_and_earnings_negative_sentence_score, rev_and_earnings_profit_positive_sentence_score,
                           rev_and_earnings_profit_negative_sentence_score, rev_positive_sentence_score,
                           rev_negative_sentence_score, earnings_positive_sentence_score,
                           earnings_negative_sentence_score))
    except Exception as e:
        print(e)