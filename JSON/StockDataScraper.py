import yfinance as yf
import os
import csv
spamreader = ''
with open('constituents.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    compList = list(reader)
    print(compList[1][1])
    for i in compList:
        #define the ticker symbol
        tickerSymbol = 'MSFT'

        #get data on this ticker
        tickerData = yf.Ticker(tickerSymbol)

        #get the historical prices for this ticker
        tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

        #see your data
        tickerDf
        #print(data)
        filename = str(i[1]) + '.json'
        FILE = open(filename,"w")
        FILE.writelines(data)
        FILE.close()