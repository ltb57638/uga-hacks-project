from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
import csv


def filterData(dates):
    with open('Scraped_data_news_output.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        compList = list(reader)
        for i in compList:
            print(i)
#     analyzer = SentimentIntensityAnalyzer()
#     for sentence in sentences:
#         vs = analyzer.polarity_scores(sentence)
#         print("{:-<65} {}".format(sentence, str(vs)))
filterData("here")
