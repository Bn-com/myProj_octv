# -*- coding: utf-8 -*-
import json
import collections

def convert(data):
    """转换unicode到str"""
    if isinstance(data, basestring):
        return (data).encode("utf-8")
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data





def write_json_file(file_path, size=4, bg=[], logo=[], datas={}):
    json_data = {
u"CHR_ID":"c001002",
u"空间大小":2,

u"背景组":[{"id":1,"type":u"背景","位置":[0,0],"url":"source/png/bg.png"}],
u"标志组":[{"id":1,"type":u"标志","位置":[0,0],"url":"source/png/logo.png"}],
u"数据组":{"Master":  {u"可否选择":True,u"图片类型":"master",u"位置":[0,0,0], u"缩放": 1, u"透明度": 1}}
}
    json_data[u"空间大小"]=size
    json_data[u"背景组"]=bg
    json_data[u"标志组"]=logo
    json_data[u"数据组"]=datas

    with open(file_path, "w") as f:
        json.dump(convert(json_data), f, indent=4,  ensure_ascii=False)



if __name__ == '__main__':
    # write_json_file(file_path="xxxx.json", size=5)

    with open("xxxx.json", "r") as f:
        json_data = json.loads(f.read().decode("utf-8"))
    with open("yyyy.json", "w") as f:
        json.dump(convert(json_data), f, indent=4, ensure_ascii=False, )
    pass