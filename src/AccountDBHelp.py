from pymongo import MongoClient
from user import User


class AccountDBHelp:
    def __init__(self):
        client = MongoClient('127.0.0.1', 27017)
        database = 'test_new'
        db = client[database]
        self.account_collection = db.account

    def insert_user(self, user: User):
        user = {
            "name": user.name,
            "password": user.password,
            "user_id": str(user.id)
        }
        return self.account_collection.insert(user)