import requests


url = "https://app-doc.test.55haitao.com/code/api_v3.1.json"
result = requests.get(url=url).json()
version = result["info"]
url = result["servers"]

# 接口路由列表
PATHS = list(result["paths"].keys())

# 接口方法 get/post/......
method = list(result["paths"][PATHS[0]].keys())[0]

# 接口参数
param = list(result["paths"][PATHS[0]][method]["requestBody"]["content"]["application/x-www-form-urlencoded"]
             ["schema"]["properties"].keys())

header = {
    "v": "v3.1",
    "token": "c032a1b5ff24292124f5e4b292e9a9c9",
}

response_code = list(result["paths"][PATHS[0]][method]["responses"].keys())