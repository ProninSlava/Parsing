import requests
import bs4
from pprint import pprint

BASE_URL = 'https://habr.com'
URL = BASE_URL + '/ru/all/'
KEYWORDS = ['процессоры', 'python', 'физика']

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
req = requests.get(URL, headers=headers).text
soup = bs4.BeautifulSoup(req, features='html.parser')


articles = soup.find_all("article")

for article in articles:
    hubs = article.find_all(class_="tm-article-snippet__hubs-item")
    hubs = [hub.text.replace("*", "").strip().lower() for hub in hubs]
    a = set(hubs).intersection(set(KEYWORDS))
    # print(a)
    if len(a) > 0:
        href = article.find(class_="tm-article-snippet__title-link").attrs['href']
        title = article.find(class_="tm-article-snippet__title tm-article-snippet__title_h2").text
        date = article.find("time").attrs['title']
        print()
        print(f'   {date}'
              f' : "{title}"'
              f' -  {BASE_URL + href}')








