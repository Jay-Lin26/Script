import requests
from utils.common import ranInt


class SwaggerApi(object):

    def __init__(self):

        __url = "https://app-doc.test.55haitao.com/code/api_v3.1.json"
        self.result = requests.get(url=__url).json()

        # 域名
        self.domain = "http://app.test.55haitao.com"

        # 所有接口信息
        self.api_info = self.result["paths"]

        # 接口名称列表
        self.urls = list(self.result["paths"])

        # 请求header参数
        self.header = {
            "v": "v3.1",
            "token": "c032a1b5ff24292124f5e4b292e9a9c9"
        }

    def __getApiInfo(self, path: str):
        """
        :param: path 接口名称
        :return: method 请求方式 -> str
        :return: param 请求参数 -> list
        :return: success_response_code 响应码 -> int
        """

        # 汇总信息
        __info = self.api_info[path]

        # 接口方法 get/post/......
        __method = list(__info.keys())[0]

        # 接口参数
        # 首先；获取requestBody里面的值，
        # 如果没有；则取parameters里面的值，
        # 如果没有；就把param设为空
        try:
            __param = list(__info[__method]["requestBody"]["content"]["application/x-www-form-urlencoded"]
                         ["schema"]["properties"].keys())
        except KeyError:

            try:
                # 原始参数
                original_param = __info[__method]["parameters"]
                __param = []
                for i in range(len(original_param)):
                    __param.append(original_param[i]["name"])

            except KeyError:
                __param = ""

        # 响应状态码 成功信息
        __success_response_code = list(__info[__method]["responses"].keys())[0]

        # 请求方法   参数   成功状态码
        return __method, __param

    def run(self):
        # for k in self.urls:
        k = "/message/get_history_message"

        # 通过接口名称获取 请求方法、请求参数
        method, param = self.__getApiInfo(k)
        # 初始化参数 -> 字典
        params = {}

        # 循环遍历参数组装成字典格式
        for i in range(len(param)):
            params[param[i]] = ranInt()

        print(params)
        # 通过method区分不同的请求方法
        if method == "post":
            response = requests.post(url=self.domain + k, headers=self.header, params=params).json()
            print(response)

        elif method == "get":
            response = requests.get(url=self.domain + k, headers=self.header, params=params).json()
            print(response)

        elif method == "delete":
            response = requests.delete(url=self.domain + k, headers=self.header, params=params).json()
            print(response)

        elif method == "put":
            response = requests.put(url=self.domain + k, headers=self.header, params=params).json()
            print(response)
