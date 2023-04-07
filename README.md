# Natural Language Processing on Stocks' Earnings Call Transcripts: An Investment Strategy Backtest Based on S&P Global Papers

# Introduction:
This article explores the use of natural language processing (NLP) on stocks' earnings call transcripts, based on S&P Global papers. The goal is to create an investment strategy that outperforms the market. The article focuses on two papers: "Natural Language Processing – Part II: Stock Selection" and "Natural Language Processing – Part III: Feature Engineering."

# Background:
The first paper suggests that sentiment scores can be created using the Loughran and McDonald Sentiment Word Lists. An investment strategy is then created by selecting the top 20% quintile of transcript scores over a four-month lookback period. The long-only strategy yields a 2.35% monthly average return, while the long-short strategy yields a 4.14% monthly average return.

The second paper suggests using descriptor tags along with positive or negative keywords within each transcript sentence. Again, the investment strategy is to take the top 20% quintile of transcript scores over a four-month lookback period. The long-only strategy yields a 4.24% monthly average return, while the long-short strategy yields a 9.16% monthly average return.

# Results:
This article presents a backtest of the two strategies on S&P500 stocks from Apr 2012 - Aug 2022. A buy-and-hold strategy would have generated a 4.07x return over the investment strategy period. However, the results of the backtest show worse performance than suggested in the papers. The long-only strategy slightly outperforms the buy-and-hold strategy, but not significantly. The long-short strategy fails to generate a profit.

# Programs:
The repository includes two PDFs which are the two papers, an article folder containing all the earnings call transcripts, a stock_price folder containing Yahoo Finance stock prices for each ticker, and four Python programs: SP500 Download Prices.py, Download Transcript Links.py, Download Transcript Text.py, and NLP Backtest.py.

In conclusion, while the use of NLP on earnings call transcripts shows promise for creating an investment strategy, the results presented in the S&P Global papers may not be entirely accurate. Readers are encouraged to review and test the strategies presented themselves.

# Additional Information:
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
