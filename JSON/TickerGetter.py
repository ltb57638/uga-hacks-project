import yfinance as yf
import string
import os
import csv
import collections
import re
spamreader = ''
def getTicker(content):
    content = re.sub(r'[^\w\s]','',content)
    articleContent = content.split()
    articleContent = [x.strip(' ') for x in articleContent]
    with open('constituents.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        compList = list(reader)
        counter = collections.Counter(articleContent)
        ticker = ''
        lowestIndex = 0
        for i in compList:
            for t in articleContent:
                #print(i[1] + ' ' + t)
                if (i[1] == t and lowestIndex <= compList.index(i)):
                    #print(i[1] == t)
                    lowestIndex = compList.index(i)
        if (lowestIndex == 0):
            return ''
        return (compList[lowestIndex][0])
