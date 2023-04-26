import requests
from bs4 import BeautifulSoup
from datetime import datetime
from webapp.models import db, News

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_python_news_without_database():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        result_news = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published =news.find('time').text
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except(ValueError):
                published = datetime.now()
       # print(f"{title = }")
       # print(f"{url = }")
       # print(f"{published = }")

            result_news.append({
                "title": title, 
                "url": url, 
                "published": published
            })
        return result_news
    return False


def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        result_news = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published =news.find('time').text
            try:
                published = datetime.strptime(published, '%B %d, %Y')
            except(ValueError):
                published = datetime.now()
            print(f"2.{published =}")
            save_news(title, url, published)


# сохранение в базу данных
def save_news(title, url, published):
    #проверка, есть ли считанный url уже в базе данных 
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()


if __name__ == "__main__":

    #    with open("python-org-news.html", "w", encoding="utf8") as f:
    #        f.write(html)
        news = get_python_news()
        print(news)