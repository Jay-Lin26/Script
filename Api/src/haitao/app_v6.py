import json
import sys
import time

import requests
import xlrd
from xlutils.copy import copy

sys.path.append("C:\\Users\\55haitao\\Desktop\\Script\\Api")

from utils.dingtalk import DingTalk
from utils.common import ranString


class ApiAutoTest:
    def __init__(self, sheet_name: str = "55haitao", environments: str = "pro"):
        """
        @:param sheet_name => ["55haitao", "maxrebates"]
        @:param environments => ["pro", "dev"]
        """
        file_path = "C:\\Users\\55haitao\\Desktop\\api.xlsx"
        try:
            book = xlrd.open_workbook(file_path)
            self.write_book = copy(book)
            self.allSheet = book.sheet_names()
            self.main_sheet = book.sheet_by_name(sheet_name)
            self.write_sheet = self.write_book.get_sheet(0)
            if sheet_name == "55haitao":
                if environments == "pro":
                    self.host = "https://appv6.55haitao.com"
                elif environments == "dev":
                    self.host = "https://app.test.55haitao.com"
                else:
                    print("请输入正确的环境名称！！！")
                    sys.exit()
            elif sheet_name == "maxrebates":
                if environments == "pro":
                    self.host = "https://api.maxrebates.com"
                elif environments == "dev":
                    self.host = "https://api.staging.51huaji.com"
                else:
                    print("请输入正确的环境名称！！！")
                    sys.exit()
            else:
                print("请输入正确的网站名称！！！")
                sys.exit()

            self.website = sheet_name
            self.env = environments
            self.sendMsg = DingTalk()
        except FileNotFoundError:
            print("%s is not found" % file_path)
            sys.exit()

    def run(self):
        rows = self.main_sheet.nrows
        # 不同设备所使用的header参数'p'不同;
        platform = ["web", "wap", "iOS", "BaiduApplet"]

        for i in range(1, rows):
            now_time = time.strftime("%Y-%m-%d-%H-%M-%S")
            method = self.main_sheet.cell(i, 1).value
            path = self.main_sheet.cell(i, 2).value
            url = self.host + self.main_sheet.cell(i, 2).value
            features = self.main_sheet.cell(i, 9).value  # 是否自动修改参数
            headers = eval(self.main_sheet.cell(i, 3).value)  # 字符串转字典需要用eval函数;
            if self.env == "pro":
                headers["token"] = "020d787a7e7ccac7756c19e46f9ee626"   # 正式
            elif self.env == "dev":
                headers["token"] = "c032a1b5ff24292124f5e4b292e9a9c9"  # 测试
            else:
                return "Token错误"

            try:
                params = eval(self.main_sheet.cell(i, 4).value)
                if features == "showAdd":
                    text = now_time + " 晒单测试；请勿审核"
                    images = [
                        {"image": "https://cdn.55haitao.com/bbs/data/attachment/forum/202112/21/202112211047435024.jpg",
                         "is_cover": "1",
                         "width": 1200,
                         "height": 1200,
                         "tags": []
                         }]

                    if self.env == "dev":
                        images[0]["image"] = "https://cdn-test.55haitao.com/bbs/data/attachment/deal/2021/12/28/6800c8cff496ea0016145623968ddd92d2d.png"
                    params["title"] = text
                    params["images"] = json.dumps(images)
                    platform = ["iOS"]
                elif features == "commentAdd":
                    text = ranString(8)
                    params["content"] = text
                    platform = ["iOS"]
                elif features == "loseorderAdd":
                    text = "TestOrder_" + str(round(time.time()))
                    params["order_number"] = text
                    platform = ["iOS"]
            except SyntaxError:
                params = " "
            except TypeError:
                return "接口参数不规范或格式错误"

            for p in platform:
                headers["p"] = p
                msg = self.main_sheet.cell(i, 5).value
                if method == 'get':
                    data = requests.get(url=url, headers=headers, params=params).json()
                    if data["msg"] == msg:
                        self.write_sheet.write(i, 6, now_time)
                        self.write_sheet.write(i, 7, "pass")
                    else:
                        self.write_sheet.write(i, 6, now_time)
                        self.write_sheet.write(i, 7, "fail")
                        self.write_sheet.write(i, 8, data["msg"])
                        ding = ' 接口 {} 返回结果异常 "platform : {}; msg : {}"; {}'
                        self.sendMsg.execution(self.website, ding.format(path, p, data["msg"], now_time))
                        break   # 跳出本次设备型号循环，开始执行下一个接口

                elif method == 'post':
                    data = requests.post(url=url, headers=headers, json=params).json()
                    if data["msg"] == msg:
                        self.write_sheet.write(i, 6, now_time)
                        self.write_sheet.write(i, 7, "pass")
                    else:
                        self.write_sheet.write(i, 6, now_time)
                        self.write_sheet.write(i, 7, "fail")
                        self.write_sheet.write(i, 8, data["msg"])
                        ding = ' 接口 {} 返回结果异常 "platform : {}; msg : {}"; {}'
                        self.sendMsg.execution(self.website, ding.format(path, p, data["msg"], now_time))
                        break

        self.write_book.save("C:\\Users\\55haitao\\Desktop\\apiReport.xlsx")