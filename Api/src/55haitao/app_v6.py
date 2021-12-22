import json
import sys
import time

import requests
import xlrd
from xlutils.copy import copy

from Api.utils.dingtalk import DingTalk


class ApiAutoTest:
    def __init__(self, sheet_name="haitao"):
        file_path = "C:\\Users\\55haitao\\Desktop\\app_v6.xlsx"
        try:
            book = xlrd.open_workbook(file_path)
            self.write_book = copy(book)
            self.allSheet = book.sheet_names()
            self.main_sheet = book.sheet_by_name(sheet_name)
            self.write_sheet = self.write_book.get_sheet(0)
            self.host = "https://appv6.55haitao.com"
            # self.host = "https://app.test.55haitao.com"
            self.sendMsg = DingTalk()
        except FileNotFoundError:
            print("%s is not found" % file_path)
            sys.exit()

    def readWork(self):
        rows = self.main_sheet.nrows
        # 不同设备所使用的header参数'p'有所不同;
        platform = ["web", "wap", "iOS", "BaiduApplet"]
        for i in range(1, rows):
            now_time = time.strftime("%Y-%m-%d %H:%M:%S")
            method = self.main_sheet.cell(i, 1).value
            path = self.main_sheet.cell(i, 2).value
            url = self.host + self.main_sheet.cell(i, 2).value
            features = self.main_sheet.cell(i, 9).value  # 是否自动修改参数
            headers = eval(self.main_sheet.cell(i, 3).value)  # 字符串转字典需要用eval函数;
            # headers["token"] = "c032a1b5ff24292124f5e4b292e9a9c9"  # 测试
            headers["token"] = "020d787a7e7ccac7756c19e46f9ee626"   # 正式
            try:
                params = eval(self.main_sheet.cell(i, 4).value)
                if features == "showAdd":
                    text = now_time + " 自动发布测试"
                    params["title"] = text
                    params["images"] = json.dumps(params["images"])
                    platform = ["iOS"]
                elif features == "commentAdd":
                    text = now_time + " 自动发布测试；请勿审核"
                    params["content"] = text
                    platform = ["iOS"]
            except SyntaxError:
                params = " "
            for p in platform:
                headers["p"] = p
                msg = self.main_sheet.cell(i, 5).value
                if method == 'get':
                    data = requests.get(url=url, headers=headers, params=params).json()
                    if data["msg"] == msg:
                        self.write_sheet.write(i, 6, now_time)
                        self.write_sheet.write(i, 7, "pass")
                    if data["msg"] != msg:
                        self.write_sheet.write(i, 6, now_time)
                        self.write_sheet.write(i, 7, "fail")
                        self.write_sheet.write(i, 8, data["msg"])
                        ding = '接口 {} 返回结果异常 "platform = {}; msg = {}"; {}'
                        self.sendMsg.execution("55Haitao", ding.format(path, p, data["msg"], now_time))
                        break   # 跳出本次设备型号循环，开始执行下一个接口
                elif method == 'post':
                    data = requests.post(url=url, headers=headers, json=params).json()
                    if data["msg"] == msg:
                        self.write_sheet.write(i, 6, now_time)
                        self.write_sheet.write(i, 7, "pass")
                    if data["msg"] != msg:
                        self.write_sheet.write(i, 6, now_time)
                        self.write_sheet.write(i, 7, "fail")
                        self.write_sheet.write(i, 8, data["msg"])
                        ding = '接口 {} 返回结果异常 "platform = {}; msg = {}"; {}'
                        self.sendMsg.execution("55Haitao", ding.format(path, p, data["msg"], now_time))
                        break
        self.write_book.save("apiReport.xlsx")


if __name__ == '__main__':
    a = ApiAutoTest()
    a.readWork()
