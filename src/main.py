from flask import Flask
import requests
import bs4

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
    turl = 'http://zxwap.caipiao.163.com/toutiao?loadMoreTimes=0'
    tHtml = get_html(turl)
    if tHtml is not None:
        s = bs4.BeautifulSoup(tHtml, 'lxml')
        li = s.find_all('li', 'newsItem')
        for child in li:
            img_src = child.find('img').get('src')
            h2_text = child.find('h2').string
            p_test = child.find("p").string
            time = child.find('i', "mark2")
            link = child.find("a", "newsLink clearfix ").get("href")
            print(img_src)
            print(h2_text)
            print(p_test)
            if time is not None:
                print(time.string)
            else:
                print('')
            print(link)


if __name__ == '__main__':
    # app.run(debug=True)
    # r = requests.get("http://www.baidu.com")
    # print(r.text)
    get_toutiao_news()
