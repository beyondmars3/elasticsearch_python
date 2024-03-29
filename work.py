# -*- coding: utf-8 -*-

"""
elasticsearch demo
"""

from elasticsearch import Elasticsearch


def create_template():
    """

    :return:
    """

    data = {
        "index_patterns": ["novel*"],
        "settings": {
            "number_of_shards": 1
        },
        "mappings": {
            "_source": {
                "enabled": True
            },
            "properties": {
                "title": {
                    "type": "keyword"
                },
                "author": {
                    "type": "keyword"
                },
                "content": {
                    "type": "text"
                },
                "created_at": {
                    "type": "date",
                    "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis",
                }
            }
        }
    }

    # res = es.indices.put_template(name="novel_template_one", body=data, order=2)
    res = es.indices.delete_template(name="novel_template")

    # {u'acknowledged': True}
    return res


def create_index():
    """

    :return:
    """
    res = es.indices.create(index="novel")
    # res = es.indices.delete(index="novel")

    print(res)


def create_document():
    """

    :return:
    """

    data = {
        "title": "追风筝的人",
        "author": "胡赛尼",
        "created_at": "2019-09-23 00:00:00",
        "content": """谨以此书献给哈里斯和法拉，他们为我启蒙。献给所有阿富汗的孩子。

我成为今天的我，是在1975年某个阴云密布的寒冷冬日，那年我十二岁。我清楚地记得当时自己趴在一堵坍塌的泥墙后面，窥视着那条小巷，旁边是结冰的小溪。许多年过去了，人们说陈年旧事可以被埋葬，然而我终于明白这是错的，因为往事会自行爬上来。回首前尘，我意识到在过去二十六年里，自己始终在窥视着那荒芜的小径。

今年夏季的某天，朋友拉辛汗从巴基斯坦打来电话，要我回去探望他。我站在厨房里，听筒贴在耳朵上，我知道电话线连着的，并不只是拉辛汗，还有我过去那些未曾赎还的罪行。挂了电话，我离开家门，到金门公园北边的斯普瑞柯湖边散步。晌午的骄阳照在波光粼粼的水面上，数十艘轻舟在和风的吹拂中漂行。我抬起头，望见两只红色的风筝，带着长长的蓝色尾巴，在天空中冉冉升起。它们舞动着，飞越公园西边的树林，飞越风车，并排飘浮着，如同一双眼睛俯视着旧金山，这个我现在当成家园的城市。突然间，哈桑的声音在我脑中响起：为你，千千万万遍。哈桑，那个兔唇的哈桑，那个追风筝的人。

我在公园里柳树下的长凳坐下，想着拉辛汗在电话中说的那些事情，再三思量。那儿有再次成为好人的路。我抬眼看看那比翼齐飞的风筝。我忆起哈桑。我缅怀爸爸。我想到阿里。我思念喀布尔。我想起曾经的生活，想起1975年那个改变了一切的冬天。那造就了今天的我。""",
    }

    res = es.index(index="novel", body=data)
    # res = es.delete(index="novel", id="pBc0G24BFCGcMFqJSPca")

    print(res)


def get_document():
    """

    :return:
    """

    """
    term 精确查询,不使用分词器
    match query知道分词器的存在，会对filed进行分词操作，然后在查询  
    """
    data = {
        "query": {
            "term": {"content": "kimchy"}
        }
    }

    res = es.search(index='novel', body=data)

    print(res)


if __name__ == '__main__':
    """ __main__ """

    es = Elasticsearch(["192.168.56.129:9200"], maxsize=25)

    get_document()
