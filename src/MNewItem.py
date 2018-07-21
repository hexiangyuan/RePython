# 新闻的item模型
class MNewItem(object):
    def __init__(self,
                 type_id,
                 title_string,
                 description_string,
                 img_string,
                 link_string,
                 view_count_int,
                 time_string,
                 new_source_int):
        self.type_id = type_id
        self.title_string = title_string
        self.description_string = description_string
        self.img_string = img_string
        self.time_string = time_string
        self.link_string = link_string
        self.view_count_int = view_count_int
        self.new_source_int = new_source_int
