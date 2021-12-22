import requests

from Libs.host import *
from cj_store_id import *
from src.utils.dingtalk import DingTalk


class CjCheck:
    def __init__(self):
        """
        @:param not_allow_stores  不支持插件的商家(针对Cj联盟)
        """
        self.not_allow_stores = store_id
        self.msg = DingTalk()

    def stores(self):
        """
        @:param url 接口域名+路由
        @:param headers 请求头
        @:param params 路由参数
        @:param result 接口数据
        """
        url = HOST_MAX_PRO + "/plugin/storeList?page=1&per_page=500&keyword=1&is_plugin=1"
        headers = {
            "v": "v3.1",
            "p": "plugin",
            "language": "2"
        }
        params = {
            "page": 1,
            "per_page": 500,
            "keyword": 1,
            "is_plugin": 1
        }
        result = requests.get(url, headers=headers, params=params).json()
        store_info = result["data"]
        last_id, last_name = [], []
        stores = {}
        for i in range(len(store_info)):
            sid = store_info[i]["id"]
            name = store_info[i]["name"]
            last_id.append(sid)
            stores[sid] = name
        for j in self.not_allow_stores:
            if int(j) in last_id:
                content = "警告：cj商家: {}({}) 出现在插件接口中！！"
                self.msg.execution("Maxrebates", content.format(stores[j], j))
        print(stores)


if __name__ == '__main__':
    CjCheck().stores()