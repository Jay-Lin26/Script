import xlrd
from xlutils.copy import copy
import requests
from Api.utils.dingtalk import DingTalk
import time
import sys


class ApiAutoTest:
    def __init__(self):
        file_path = "C:\\Users\\55haitao\\Desktop\\app_v6.xlsx"
        try:
            book = xlrd.open_workbook(file_path)
            self.write_book = copy(book)
            self.allSheet = book.sheet_names()
            self.main_sheet = book.sheet_by_name("main")
            self.write_sheet = self.write_book.get_sheet(0)
            self.host = "https://appv6.55haitao.com"
            self.sendMsg = DingTalk()
        except FileNotFoundError:
            print("%s 接口文档找不到了~~" % file_path)
            sys.exit()

    def readWork(self):
        rows = self.main_sheet.nrows
        # 不同设备所使用的header参数'p'有所不同;
        platform = ["web", "wap", "iOS", "BaiduApplet"]
        for p in platform:
            for i in range(1, rows):
                now_time = time.strftime("%Y-%m-%d %H:%M")
                method = self.main_sheet.cell(i, 1).value
                path = self.main_sheet.cell(i, 2).value
                url = self.host + self.main_sheet.cell(i, 2).value
                headers = eval(self.main_sheet.cell(i, 3).value)  # 字符串转字典需要用eval函数;
                headers["token"] = "020d787a7e7ccac7756c19e46f9ee626"
                headers["p"] = p
                try:
                    params = eval(self.main_sheet.cell(i, 4).value)
                except SyntaxError:
                    params = " "
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
        self.write_book.save("apiReport.xlsx")


if __name__ == '__main__':
    a = ApiAutoTest()
    a.readWork()