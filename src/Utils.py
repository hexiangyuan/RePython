import random


def random_user_agent():
    uas = [
        "Dalvik/2.1.0 (Linux; U; Android 8.1.0; EML-AL00 Build/HUAWEIEML-AL00)",
        "User Agent:Mozilla/5.0 (Linux; Android 4.4.4; SAMSUNG-SM-N900A Build/tt) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
        "Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "User-Agent:Mozilla/5.0(iPhone;U;CPUiPhoneOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.",
        "User-Agent:Mozilla/5.0(Linux;U;Android2.3.7;en-us;NexusOneBuild/FRF91)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
        "User-Agent:Opera/9.80(Android2.3.4;Linux;OperaMobi/build-1107180945;U;en-GB)Presto/2.8.149Version/11.10",
        "Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G9350 Build/NRD90M)"
    ]
    index = random.randint(0, len(uas))
    return uas[index]


filter_key_worlds = [
    "下载",
    "交流群",
    "官方",
    "网易",
]


def filter_new(new_item):
    for i in filter_key_worlds:
        if i in new_item.title_string:
            return True
    return False


sources = [{"id": 1, "name": "网易新闻"}]


def get_source_by_id(source_id):
    for i in sources:
        if source_id == i['id']:
            return i['name']

    return ""


# toutiao ssq nba dlt cba jingcai news world china
lottery_types = [{
    "id": 1,
    "value": "toutiao",
    "name": "热门头条"
}, {
    "id": 2,
    "value": "nba",
    "name": "篮球NBA"
}, {
    "id": 3,
    "value": "cba",
    "name": "篮球CBA"
}, {
    "id": 4,
    "value": "world",
    "name": "国际足球"
}, {
    "id": 5,
    "value": "china",
    "name": "中国足球"
}, {
    "id": 6,
    "value": "dlt",
    "name": "大乐透"
}, {
    "id": 7,
    "value": "news",
    "name": "彩市行情"
}, {
    "id": 8,
    "value": "ssq",
    "name": "双色球"
}]

lottery_new_banners = [{
    "title":
    "中国彩票行业每周动态",
    "img":
    "http://om6hh53na.bkt.clouddn.com/Screen%20Shot%202018-07-24%20at%2010.39.37%20AM.png",
    "link":
    "http://zxwap.caipiao.163.com/hangye/article/18/0716/15/DMRK087Q000597U8.html"
}, {
    "title":
    "辽宁彩民揽七乐彩1134222元",
    "img":
    "http://zxwap.caipiao.163.com/hangye/article/18/0723/15/DNDJPF9J000597U8.html",
    "link":"http://zxwap.caipiao.163.com/hangye/article/18/0723/15/DNDJPF9J000597U8.html"
}, {
    "title":
    "财政部:5月全国彩票销406亿",
    "img":
    "http://img6.cache.netease.com/sports/2015/1/9/20150109104322ac429.jpg",
    "link":
    "http://zxwap.caipiao.163.com/hangye/article/18/0630/07/DLHJHNC0000597U8.html"
}, {
    "title":
    "湖人旧将:杜兰特快来湖人吧",
    "img":
    "http://img3.cache.netease.com/sports/2016/6/5/20160605075602bad21.jpg",
    "link":
    "http://zxwap.caipiao.163.com/nba/article/16/0605/07/BOPHTAKQ00051CA1.html"
}]


def get_lottery_type_by_value(value):
    for i in lottery_types:
        if value == i["value"]:
            return i["id"]
    return 1
