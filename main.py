import requests
import bs4

BASE_URL = 'https://habr.com'
URL = BASE_URL + '/ru/all/'
KEYWORDS = ['python', 'физика']

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
req = requests.get(URL, headers=headers).text
soup = bs4.BeautifulSoup(req, features='html.parser')


articles = soup.find_all("article")

for article in articles:
    hubs = article.find_all(class_="tm-article-snippet__hubs-item")
    hubs = [hub.text.strip() for hub in hubs]
    for hub in hubs:
        hub_ = hub.replace("*", "").strip().lower()
        # print(hub_)
        if hub_ in KEYWORDS:
            href = article.find(class_="tm-article-snippet__title-link").attrs['href']
            title = article.find(class_="tm-article-snippet__title tm-article-snippet__title_h2").text
            date = article.find("time").attrs['title']
            print()
            otvet =  (f'{date} : {title} - {BASE_URL + href}')
            print(otvet)





