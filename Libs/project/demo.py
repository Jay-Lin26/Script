import requests
import json
a = '{"category":2,"content":"自动发布请勿审核","images":[{"image":"https://55haitao-test.oss-cn-qingdao.aliyuncs.com/bbs/data/attachment/forum/202112/06/image_of1xK_202112061741","is_cover":"1","width":1200,"height":1200,"tags":[]}],"question_id":0,"tags":"70078","title":"16:44自动发布测试"}'
b = eval(a)
image = b["images"]
b["images"] = json.dumps(image)
print(b["images"])
url = "https://appv6.55haitao.com/show/add"
headers = {
    "v": "v3.1",
    "token": "020d787a7e7ccac7756c19e46f9ee626"
}
data = requests.post(url=url, headers=headers, json=b).json()
print(data)