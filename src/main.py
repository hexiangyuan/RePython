from flask import Flask
import requests
import bs4

from src.dbmodel.MNewItem import MNewItem
from src.dbmodel.NewDBHelper import NewDBHelper

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return None


def get_toutiao_news():
    dbhelper = NewDBHelper()
    turl = 'http://zxwap.caipiao.163.com/toutiao?loadMoreTimes=0'
    tHtml = get_html(turl)
    if tHtml is not None:
        s = bs4.BeautifulSoup(tHtml, 'lxml')
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
        dbhelper.insert_news(news)


def filter_new(new_item):
    return "免费下载" in new_item.title_string or "交流群" in new_item.title_string or "官方" in new_item.title_string


if __name__ == '__main__':
    get_toutiao_news()
