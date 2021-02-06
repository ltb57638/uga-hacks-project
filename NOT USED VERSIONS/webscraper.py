from newsapi import NewsApiClient
# Init
api = NewsApiClient(api_key='a4544e833d5f4de08f1a957d87cb9706')
import os
import csv
spamreader = ''
with open('constituents.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    compList = list(reader)
    print(compList[1][1])
    t = 0
    for i in compList:
        data = api.get_everything(i[1], sort_by="relevancy", language="en")
        # Let's create a file and write it to disk.
        print(data)
        filename = str(i[1]) + '.json'
        FILE = open(filename,"w")
        FILE.writelines(data)
        FILE.close()
# An API key; for example: "74f9e72a4bfd4dbaa0cbac8e9a17d34a
# api.get_everything("hurricane OR tornado", sort_by="relevancy", language="en"
# print(api.get_everything(q="hurricane",from_param="2000-00-00",to="2020-12-31"))

# print(results)