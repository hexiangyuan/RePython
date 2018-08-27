from flask import Flask, request

from bson.json_util import dumps

from NewDBHelper import NewDBHelper
from AccountDBHelp import AccountDBHelp
from user import User
from Utils import *
from RegexUtils import *
import uuid

app = Flask(__name__)


@app.route("/lottery_new/get_news_types", methods=["GET", "POST"])
def get_lottery_new_types():
    response = {"code": 200, "data": lottery_types}
    return dumps(response, ensure_ascii=False)


@app.route("/lottery_new/get_news_banner", methods=["GET", "POST"])
def get_news_banners():
    response = {"code": 200, "data": lottery_new_banners}
    return dumps(response, ensure_ascii=False)


@app.route("/account/login", methods=["POST"])
def login():
    response = {}
    user_name = request.json.get('userName')
    pass_word = request.json.get('passWord')
    user_db = AccountDBHelp()
    find_result = user_db.account_collection.find_one({"name": user_name})
    if find_result is None:
        response = {"code": 500, "msg": "用户名不存在"}
        return dumps(response, ensure_ascii=False)

    if find_result["password"] == pass_word:
        response = {"code": 200, "data": {"id": find_result["user_id"]}}
    else:
        response = {"code": 500, "msg": "帐号和密码不匹配"}
    return dumps(response, ensure_ascii=False)


@app.route("/account/register", methods=["POST"])
def register():
    response = {}
    user_name = request.json.get('userName')
    pass_word = request.json.get('passWord')
    user_verify = verify_user_name(user_name)
    if not verify_user_name(user_name):
        response = {"code": 500, "msg": "用户名格式错误"}
        return dumps(response, ensure_ascii=False)
    elif not verify_password(pass_word):
        response = {"code": 500, "msg": "密码格式错误"}
        return dumps(response, ensure_ascii=False)
    user_db = AccountDBHelp()
    find_result = user_db.account_collection.find_one({"name": user_name})
    if find_result is not None:
        response = {"code": 500, "msg": "用户名重复"}
        return dumps(response, ensure_ascii=False)
    user_id = uuid.uuid1()
    user = User(user_id.int, user_name, pass_word)
    result = user_db.insert_user(user)
    response = {"code": 200, "data": {"id": str(user_id.int)}}
    return dumps(response, ensure_ascii=False)

@app.route("/lottery_new/user_get_favorate")

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

    response = {"code": 200, "data": data}
    return dumps(response, ensure_ascii=False)


if __name__ == '__main__':
    import sys
    import io

    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    app.run(host='0.0.0.0', port=5000)
