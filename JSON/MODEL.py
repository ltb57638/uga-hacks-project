from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
import csv
import yfinance as yf

def filterData(dates):
    with open('Scraped_data_news_output.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        compList = list(reader)
        for i in dates:
            index = compList.index(i[0])
            #define the ticker symbol
            tickerSymbol = dates[index][0]
            #get data on this ticker
            tickerData = yf.Ticker(tickerSymbol)
            #get the historical prices for this ticker
            tickerDf = tickerData.history(period='2d', start=dates[index][1], end=dates[index][2])
            #see your data
            tickerDf
            analyzer = SentimentIntensityAnalyzer()
            vs = analyzer.polarity_scores(compList[index][0])
            print("{:-<65} {}".format(compList[index][0], str(vs)))
            

