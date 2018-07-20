from pymongo import MongoClient
import datetime

if __name__ == '__main__':
    client = MongoClient('127.0.0.1', 27017)
    DATABASE = 'test-database'
    db = client[DATABASE]
    post = {"author": "ZHANAN",
            "test": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}
    posts = db.inventory
    cursor = posts.find_one({"author":"ZHANAN"})
    print(cursor)
