from flask import Flask

from src.Utils import get_source_by_id
from src.dbmodel.NewDBHelper import NewDBHelper
from bson.json_util import dumps

app = Flask(__name__)


@app.route("/lottery_new/get_news_types", methods=["GET", "POST"])
def get_lottery_new_types():
    response = {
        "code": 200,
        "data": [{
            "id": 1,
            "name": "热门头条"
        }, {
            "id": 2,
            "name": "足球"
        }, {
            "id": 3,
            "name": "足球"
        }, {
            "id": 4,
            "name": "足球"
        }, {
            "id": 5,
            "name": "足球"
        }]
    }
    return dumps(response, ensure_ascii=False)


@app.route("/lottery_new/get_news_list", methods=["GET", "POST"])
def get_news_list():
    db_helper = NewDBHelper()
    result = db_helper.find_news(0)
    data = []
    for i in result:
        new = {
            "title": i["title"],
            "desc": i["description"],
            "img": i["img"],
            "link": i["link"],
            "time": i["time"],
            "view_count": i["view_count"],
            "source": get_source_by_id(i["new_source"])
        }
        data.append(new)

    response = {
        "code": 200,
        "data": data
    }
    return dumps(response, ensure_ascii=False)


if __name__ == '__main__':
    app.run()
