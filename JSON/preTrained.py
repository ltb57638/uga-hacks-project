from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
import csv
import yfinance as yf
import pandas
import uuid


import datetime
def filterData(dates):
    with open('Scraped_data_news_output.csv', newline='') as csvfile:
        
        # data = yf.download('AAPL','2016-01-04','2016-01-06') 
        
        # print(data['2016-01-04','Open'])
        # print(data['2016-01-05','Close'])
        
        reader = csv.reader(csvfile, delimiter='|')
        compList = list(reader)
        for i in dates:
            index = dates.index(i)
            #define the ticker symbol
            tickerSymbol = dates[index][0]
            #get data on this ticker
            tickerData = yf.Ticker(tickerSymbol)
            #get the historical prices for this ticker
            tickerDf = yf.download(dates[index][0], start=dates[index][1], end=dates[index][2])
            tickDict = tickerDf.to_dict()
            print(tickerDf)
            openPrice = tickDict['Open'][dates[index][1]]
            closePrice = tickDict['Close'][dates[index][2] - datetime.timedelta(days=1)]
            #print(tickerDf.at[dates[index][1].date, str(dates[index][0])])
            #see your data
            analyzer = SentimentIntensityAnalyzer()
            #print(compList[index][0])
            vs = analyzer.polarity_scores(compList[index][0])
            
            negValue = vs['neg']
            posValue = vs['pos']
            if (negValue > posValue and openPrice < closePrice):
                unique_filename = 'negative/' + str(uuid.uuid4())
                f = open(unique_filename, "a")
                f.write(compList[i])
                f.close()
            elif (posValue > negValue and openPrice > closePrice):
                unique_filename = 'positive/' + str(uuid.uuid4())
                f = open(unique_filename, "a")
                f.write(compList[i])
                f.close()
            
            

