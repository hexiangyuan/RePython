from pymongo import MongoClient


class NewDBHelper:

    def __init__(self):
        client = MongoClient('127.0.0.1', 27017)
        database = 'test_new'
        db = client[database]
        self.newdb = db.lottery_news

    def insert_news(self, new_item_array):
        new_list = []
        for item in new_item_array:
            new_item = {
                "type": item.type_id,
                "title": item.title_string,
                "description": item.description_string,
                "img": item.img_string,
                "link": item.link_string,
                "time": item.time_string,
                "view_count": item.view_count_int,
                "new_source": item.new_source_int}
            new_list.append(new_item)

        print(new_list)
        result = self.newdb.insert_many(new_list)
        print(result)

    def find_news(self, filter_limit, page_index):
        skip = 20 * page_index
        find_result = self.newdb.find(filter_limit).limit(20).skip(skip)
        return find_result

    def delete_all(self):
        result = self.newdb.delete_many({})
        print("删除数据")
