from flask import Flask

from src.dbmodel.NewDBHelper import NewDBHelper
from bson.json_util import dumps

app = Flask(__name__)


@app.route("/getnewlist/<type>/", methods=["GET", "POST"])
def hello_flask(type):
    db_helper = NewDBHelper()
    result = db_helper.find_news(0)
    json = dumps(result)
    print(json)
    return json


if __name__ == '__main__':
    app.run()
