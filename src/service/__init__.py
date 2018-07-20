from flask import Flask, request

from src.Utils import get_source_by_id, lottery_types
from src.dbmodel.NewDBHelper import NewDBHelper
from bson.json_util import dumps

app = Flask(__name__)


@app.route("/lottery_new/get_news_types", methods=["GET", "POST"])
def get_lottery_new_types():
    response = {
        "code": 200,
        "data": lottery_types
    }
    return dumps(response, ensure_ascii=False)


@app.route("/lottery_new/get_news_list", methods=["GET", "POST"])
def get_news_list():
    type_id = request.args.get('type')
    page_index = request.args.get('page_index')
    db_helper = NewDBHelper()
    result = db_helper.find_news({"type": int(type_id)}, int(page_index))
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
