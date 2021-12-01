import xlrd
from xlutils.copy import copy
import requests
from Api.utils.dingtalk import DingTalk


class ApiAutoTest:
    def __init__(self):
        book = xlrd.open_workbook("C:\\Users\\55haitao\\Desktop\\app_v6.xlsx")
        self.write_book = copy(book)
        self.allSheet = book.sheet_names()
        self.main_sheet = book.sheet_by_name("main")
        self.write_sheet = self.write_book.get_sheet(0)
        self.host = "https://appv6.55haitao.com"
        self.sendMsg = DingTalk()

    def writeWork(self, row=0, col=0, content=""):
        self.write_sheet.write(2, 7, content)
        self.write_book.save("new_api.xlsx")

    def readWork(self):
        rows = self.main_sheet.nrows
        for i in range(1, rows):
            method = self.main_sheet.cell(i, 1).value
            url = self.host + self.main_sheet.cell(i, 2).value
            headers = eval(self.main_sheet.cell(i, 3).value)  # 字符串转字典需要用eval函数
            params = self.main_sheet.cell(i, 4).value
            msg = self.main_sheet.cell(i, 5).value
            if method == 'get':
                data = requests.get(url=url, headers=headers, params=params).json()
                if data["msg"] == msg:
                    self.write_sheet.write(i, 6, "2021-12-01")
                    self.write_sheet.write(i, 7, "pass")
                if data["msg"] != msg:
                    self.write_sheet.write(i, 6, "2021-12-01")
                    self.write_sheet.write(i, 7, "fail")
                    self.write_sheet.write(i, 8, data["msg"])
                    ding = "接口 {} 返回结果异常 '{}'; 请及时排查！{}"
                    self.sendMsg.execution("55Haitao", ding.format(url, data["msg"], "2021-12-01"))
            elif method == 'post':
                data = requests.post(url=url, headers=headers, json=params).json()
                if data["msg"] == msg:
                    self.write_sheet.write(i, 6, "2021-12-01")
                    self.write_sheet.write(i, 7, "pass")
                if data["msg"] != msg:
                    self.write_sheet.write(i, 6, "2021-12-01")
                    self.write_sheet.write(i, 7, "fail")
                    self.write_sheet.write(i, 8, data["msg"])
                    ding = "接口 {} 返回结果异常 '{}'; 请及时排查！{}"
                    self.sendMsg.execution("55Haitao", ding.format(url, data["msg"], "2021-12-01"))
        self.write_book.save("new_api.xlsx")


if __name__ == '__main__':
    a = ApiAutoTest()
    a.readWork()
    # a.writeWork()