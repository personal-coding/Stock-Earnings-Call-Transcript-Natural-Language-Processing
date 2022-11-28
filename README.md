# Stock Earnings Call Transcript Natural Language Processing

Investment strategy based on the results of the papers [**Natural Language Processing – Part II: Stock Selection**](https://github.com/ScrapeWithYuri/Stock-Earnings-Call-Transcript-Natural-Language-Processing/blob/main/NLP-II-Paper-S%26P-Global.pdf) and [**Natural Language Processing – Part III: Feature Engineering**](https://github.com/ScrapeWithYuri/Stock-Earnings-Call-Transcript-Natural-Language-Processing/blob/main/NLP-III-Paper-S%26P-Global.pdf) from S&P Global.

# Background

S&P Global released two papers using natural language processing on stocks' earnings call transcripts, which created an outperforming investment strategy backtest.

 - The Part II paper suggested that sentiment scores could be created using the Loughran and McDonald Sentiment Word Lists. Using the net positive score (the number of positive words minus the number of negative words divided by the total number of words in the transcript), an investment strategy was created. The investment strategy takes the top 20% quintile of transcript scores over a four-month lookback period. The stocks chosen are equal weighted and are rebalanced at month-end. The paper suggested that a long-only strategy yielded a 2.35% monthly average return, while a long-short strategy yielded a 4.14% monthly average return.
 - The Part III paper suggested that scores could be created using descriptor tags (i.e. revenue, earnings, profitability) along with positive or negative keywords within each transcript sentence. Using the net positive score (the number of positive descriptor tag sentences minus the number of negative descriptor tag sentences divided by the total number of sentences in the transcript), an investment strategy was created. The investment strategy is to take the top 20% quintile of transcript scores over a four-month lookback period. The stocks chosen are equal weighted and are rebalanced at month-end. The paper suggested that a long-only strategy yielded a 4.24% monthly average return, while a long-short strategy yielded a 9.16% monthly average return.
 
My tests focus on S&P500 stocks from Apr 2012 - Aug 2022. I did not factor in stocks that had moved in or out of the S&P500 over the investment strategy period. Simply, I only looked at stocks that were present in the S&P500 as of Sep 2022. If the indicators were truly indicative of market outperformance, I did not believe that small stock selection differences in the S&P500 over time would yield a significantly different result.

# Results

Over the investment strategy period, a buy-and-hold strategy would have generated a 4.07x return (again, based on stocks that were presently in the S&P500 as of Sep 2022 and not factoring in stocks that moved in or out of the index over time).

My results show much worse results than suggested in the papers. The long-only strategy slightly outperforms the buy-and-hold strategy, but not significantly. The long-short strategy fails to generate a profit, as the short side of the trades eats away at all of the long trades' profits.

I am surpised that the short trades results were significantly different than the papers' results. Perhaps I incorrectly programmed the back test, although I heavily reviewed the back test programming logic.

 - NLP II long-only back test

| Return  | Long Hit Rate | Short Hit Rate |
| ------------- | ------------- | ------------- |
| 4.36x  | 59.1%  | N/A  |

 - NLP II long-short back test

| Return  | Long Hit Rate | Short Hit Rate |
| ------------- | ------------- | ------------- |
| 0.98x  | 59.1%  | 42.0%  |

 - NLP III long-only back test (revenue topic + directionally positive)

| Return  | Long Hit Rate | Short Hit Rate |
| ------------- | ------------- | ------------- |
| 4.10x  | 59.1%  | N/A  |

 - NLP III long-short back test (revenue topic + directionally positive)

| Return  | Long Hit Rate | Short Hit Rate |
| ------------- | ------------- | ------------- |
| 0.99x  | 59.1%  | 42.2%  |
 

# Programs

There are several programs in this repository:

 - Two PDFs which are the two papers
 - [article folder](https://github.com/ScrapeWithYuri/Stock-Earnings-Call-Transcript-Natural-Language-Processing/tree/main/article) - contains all of the earnings call transcripts
 - [stock_price folder](https://github.com/ScrapeWithYuri/Stock-Earnings-Call-Transcript-Natural-Language-Processing/tree/main/stock_price) - contains Yahoo Finance stock prices for each ticker
 - [SP500 Download Prices.py](https://github.com/ScrapeWithYuri/Stock-Earnings-Call-Transcript-Natural-Language-Processing/blob/main/SP500%20Download%20Prices.py) - downloads stock price data from Yahoo Finance
 - [Download Transcript Links.py](https://github.com/ScrapeWithYuri/Stock-Earnings-Call-Transcript-Natural-Language-Processing/blob/main/Download%20Transcript%20Links.py) - downloads SeekingAlpha earnings call transcript links
 - [Download Transcript Text.py](https://github.com/ScrapeWithYuri/Stock-Earnings-Call-Transcript-Natural-Language-Processing/blob/main/Download%20Transcript%20Text.py) - downloads SeekingAlpha earnings call transcript text
 - [NLP II - Sentiment Score.py](https://github.com/ScrapeWithYuri/Stock-Earnings-Call-Transcript-Natural-Language-Processing/blob/main/NLP%20II%20-%20Sentiment%20Score.py) creates net positive sentiment scores based on the Loughran and McDonald Sentiment Word Lists from each earnings call transcript text
 - [NLP II - Backtest.py](https://github.com/ScrapeWithYuri/Stock-Earnings-Call-Transcript-Natural-Language-Processing/blob/main/NLP%20III%20-%20Backtest.py) - creates a stock back test based on the net positive sentiment scores
 - [NLP III - Topic Positive Direction Score.py](https://github.com/ScrapeWithYuri/Stock-Earnings-Call-Transcript-Natural-Language-Processing/blob/main/NLP%20III%20-%20Topic%20Positive%20Direction%20Score.py) - creates scores based on sentences that contain a topic (revenue, earnings, profitability) plus net positive words from each earnings call transcript text
 - [NLP III - Guidance and Topic Score.py](https://github.com/ScrapeWithYuri/Stock-Earnings-Call-Transcript-Natural-Language-Processing/blob/main/NLP%20III%20-%20Guidance%20and%20Topic%20Score.py) - creates scores based on sentences that contain a topic (revenue, earnings, profitability) plus a guidance word from each earnings call transcript text
 - [NLP III - Backtest.py](https://github.com/ScrapeWithYuri/Stock-Earnings-Call-Transcript-Natural-Language-Processing/blob/main/NLP%20III%20-%20Backtest.py) - creates a stock back test based on the score created by *NLP III - Topic Positive Direction Score.py* or *NLP III - Guidance and Topic Score.py*
