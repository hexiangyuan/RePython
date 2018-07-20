from flask import Flask
import requests
import bs4

from src.Utils import random_user_agent, filter_new
from src.dbmodel.MNewItem import MNewItem
from src.dbmodel.NewDBHelper import NewDBHelper

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def get_html(url):
    try:
        ua = random_user_agent()
        print(ua)
        headers = {'user-agent': ua}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return None


def get_hot_news():
    url_text = 'http://zxwap.caipiao.163.com/toutiao?loadMoreTimes=0'
    html_text = get_html(url_text)
    if html_text is not None:
        s = bs4.BeautifulSoup(html_text, 'lxml')
        li = s.find_all('li', 'newsItem')
        news = []
        for child in li:
            img_src = child.find('img').get('src')
            time = child.find('i', "mark2")
            link = child.find("a", "newsLink clearfix ").get("href")
            h2_text = child.find('h2').string
            p_text = child.find("p").string
            if time is None:
                time = ""
            else:
                time = time.string
            item = MNewItem(1, h2_text, p_text, img_src, link, 0, time, 1)
            if not filter_new(item):
                news.append(item)
        insert_news_into_db(news)


def insert_news_into_db(news):
    db_helper = NewDBHelper()
    db_helper.insert_news(news)


if __name__ == '__main__':
    get_hot_news()
