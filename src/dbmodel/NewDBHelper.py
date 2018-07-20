from pymongo import MongoClient


class NewDBHelper:

    def insert_news(self, new_item_array):
        client = MongoClient('127.0.0.1', 27017)
        database = 'test_new'
        db = client[database]
        newdb = db.lottery_news
        new_list = []
        for item in new_item_array:
            new_item = {
                "type": item.type_id,
                "title": item.title_string,
                "description": item.description_string,
                "img": item.img_string,
                "link": item.link_string,
                "view_count": item.view_count_int,
                "new_source": item.new_source_int}
            new_list.append(new_item)

        print(new_list)
        result = newdb.insert_many(new_list)
        print(result)
