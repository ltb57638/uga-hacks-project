import feedparser as fp
import json
import newspaper
from newspaper import Article
from time import mktime
import datetime
import csv
import TickerGetter
import preTrained
def GetContent():
    interate = 0
    LIMIT = 10
    articles_array = []
    data = {}
    data['newspapers'] = {}
    dates = []
    urls = []
    with open('sample2.json') as data_file:
        for line in data_file:
            urls.append(json.loads(line))

    try:
        f = csv.writer(open('Scraped_data_news_output.csv', 'w', encoding='utf-8'))
        date_list = csv.writer(open('dates.csv', 'w', encoding='utf-8'))
    except Exception as e:
        print(e)
        
    count = 1
    # Iterate through each news company
    for value in urls:
        if 'rss' in value:
            d = fp.parse(value['rss'])
            #print("Downloading articles from ", company)
            newsPaper = {
                "rss": value['rss'],
                "link": value['link'],
                "articles": []
            }
            for entry in d.entries:
                # Check if publish date is provided, if no the article is skipped.
                # This is done to keep consistency in the data and to keep the script from crashing.
                if hasattr(entry, 'published'):
                    if count > LIMIT:
                        break
                    article = {}
                    article['link'] = entry.link
                    date = entry.published_parsed
                    article['published'] = datetime.fromtimestamp(mktime(date)).isoformat()
                    try:
                        content = Article(entry.link)
                        content.download()
                        content.parse()
                    except Exception as e:
                        # If the download for some reason fails (ex. 404) the script will continue downloading
                        # the next article.
                        print(e)
                        print("continuing...")
                        continue
                    newsPaper['articles'].append(article)
                    articles_array.append(article)
                    #print(count, "articles downloaded from", company, ", url: ", entry.link)
                    count = count + 1
        else:
            # This is the fallback method if a RSS-feed link is not provided.
            # It uses the python newspaper library to extract articles
            # print("Building site for ", company)
            #print(value["link"])
            # paper = newspaper.build(value['link'], memoize_articles=False)
            # newsPaper = {
            #     "link": value['link'],
            #     "articles": []
            # }
            # noneTypeCount = 0
            # for content in paper.articles:
            #     if count > LIMIT:
            #         break
            #     try:
            #         content.download()
            #         content.parse()
            #     except Exception as e:
            #         print(e)
            #         print("continuing...")
            #         continue
                # Again, for consistency, if there is no found publish date the article will be skipped.

                # article = {}
                # article['title'] = content.title
                # article['authors'] = content.authors
                # article['text'] = content.text
                # article['top_image'] =  content.top_image
                # article['movies'] = content.movies
                # article['link'] = content.url
                # article['published'] = content.publish_date
                # newsPaper['articles'].append(article)
                # articles_array.append(article)
                # count = count + 1
                #noneTypeCount = 0
            try:
                url = value["link"]
                article = Article(url)
                article.download()
                article.parse()
                try:
                    print(interate)
                    interate = interate + 1
                    if (len(article.text.split()) > 50):
                        newContent = ' '.join(article.text.split()[:50])
                        currentDate = datetime.datetime.strptime(value["date"], '%Y-%m-%d')
                        tick = TickerGetter.getTicker(newContent)
                        if (tick != ''):
                            newList = [TickerGetter.getTicker(newContent), currentDate - datetime.timedelta(days=1), currentDate + datetime.timedelta(days=1)]
                            dates.append(newList)
                            date_list.writerow([newList])
                            f.writerow([newContent, '|'])
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
                continue
        count = 1
    return dates
    # data['newspapers'][urls] = newsPaper
# try:
#     f = csv.writer(open('Scraped_data_news_output.csv', 'w', encoding='utf-8'))
#     f.writerow(['Title', 'Authors','Text','Image','Videos','Link','Published_Date'])
    #print(article)
    # for artist_name in articles_array:
        # title = artist_name['title']
        # authors=artist_name['authors']
        # text = article.text
        # image=artist_name['top_image']
        # video=artist_name['movies']
        # link=artist_name['link']
        # publish_date=artist_name['published']
        # Add each artist’s name and associated link to a row
        # f.writerow([text])
# except Exception as e: print(e)