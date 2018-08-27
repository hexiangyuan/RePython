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
}]

lottery_new_banners = [{
    "title":
    "男子百米苏炳添无悬念夺冠",
    "img":
    "https://pic-bucket.nosdn.127.net/photo/0005/2018-08-26/DQ61OP5C06JC0005NOS.jpg?imageView&thumbnail=750x0&quality=85&type=jpg&interlace=1",
    "link":
    "https://3g.163.com/sports/article/DQ5UD5DP00058782.html"
}, {
    "title":
    "中国加时绝杀韩国夺冠",
    "img":
    "https://cms-bucket.nosdn.127.net/2018/08/26/1d2a73c55fb549ae9f866e65cba386d5.jpeg?imageView&thumbnail=750x0&quality=85&type=jpg&interlace=1",
    "link":"https://3g.163.com/sports/article/DQ5ULNNS0005877V.html?clickfrom=channel2018_sports_index_newslist#child=index&offset=3"
}, {
    "title":
    "国羽亚运会无人进四强",
    "img":
    "https://pic-bucket.nosdn.127.net/photo/0005/2018-08-26/DQ5BOHN40AQ30005NOS.jpg?imageView&thumbnail=75y75&quality=85&type=webp&interlace=1&enlarge=1",
    "link":
    "https://3g.163.com/sports/article/DQ5A4K6P00058782.html?clickfrom=channel2018_sports_index_newslist#child=index&offset=4"
}, {
    "title":
    "湖人旧将:杜兰特快来湖人吧",
    "img":
    "http://om6hh53na.bkt.clouddn.com/dulante.jpg",
    "link":
    "http://zxwap.caipiao.163.com/nba/article/16/0605/07/BOPHTAKQ00051CA1.html"
}]


def get_lottery_type_by_value(value):
    for i in lottery_types:
        if value == i["value"]:
            return i["id"]
    return 1


def generate_gid():
    gids = []
    for number in range(100000, 10000000):
        gids.append(number)
    for gid in gids:
        index0 = random.randint(0, len(gids) - 1)
        index1 = len(gids) - 1
        tmp = gids[index0]
        gids[index0] = gids[index1]
        gids[index1] = tmp
    return gids.pop()