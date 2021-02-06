import requests
from bs4 import BeautifulSoup

def add_plus(keywords):
	keywords = keywords.split()
	keyword_edited = ""
	for i in keywords:
		keyword_edited += i + "+"
	keyword_edited = keyword_edited[:-1]
	return keyword_edited

class KeywordScraper:
        def __init__(self, keyword):
                self.keyword = keyword
                plusified_keyword = add_plus(keyword)
                self.keywords_scraped = []
                self.search_string = "https://www.google.com/search?q=" + plusified_keyword

        def scrape_SERP(self):
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
                content = requests.get(self.search_string, headers=headers).text
                soup = BeautifulSoup(content, "html.parser")
                related_keyword_section = soup.find("div", {"class":"card-section"})
                keywords_cols = related_keyword_section.find_all("div", {"class":"brs_col"})
                print(keywords_cols[0])
                for col in keywords_cols:
                        list_of_keywords = col.find_all("p", {"class":"nVcaUb"})
                        for i in list_of_keywords:
                                self.keywords_scraped.append(i.find("a").text)
        def write_to_file(self):
                for keyword in self.keywords_scraped:
                        with open("scraped keywords.txt", "a") as f:
                                f.write(keyword + "\n")
                print("keywords related to " + self.keyword + " scraped successfully")


s = KeywordScraper("Best gaming pc")
s.scrape_SERP()
s.write_to_file()