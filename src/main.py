from flask import Flask
import requests
import bs4

from src.Utils import random_user_agent, filter_new, lottery_types, get_lottery_type_by_value
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


def get_163_news(new_type, page_index):
    url_text = 'http://zxwap.caipiao.163.com/' + new_type + '?loadMoreTimes=' + str(page_index)
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
            type_id = get_lottery_type_by_value(new_type)
            if time is None:
                time = ""
            else:
                time = time.string
            item = MNewItem(type_id, h2_text, p_text, img_src, link, 0, time, 1)
            if not filter_new(item):
                news.append(item)
        insert_news_into_db(news)


def insert_news_into_db(news):
    db_helper = NewDBHelper()
    db_helper.insert_news(news)


def spider_lottery_news():
    for type_item in lottery_types:
        for i in range(0, 1):
            get_163_news(type_item["value"], i)


if __name__ == '__main__':
    db = NewDBHelper()
    db.delete_all()
    spider_lottery_news()
