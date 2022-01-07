import re

import requests

from utils.dingtalk import DingTalk
from Libs.host import *


class PriceComparisonWeb:
    def __init__(self):
        """
        @:param thecashback_api 提供给比价网站的接口
        @:param holic_api
        @:param monitor_api
        @:param msg  钉钉机器人
        """
        self.thecashback_api = HOST_MAX_TEST + '/Thecashback/store?token=ca06f53ca3557cb6db77d6752b4840ee'
        self.holic_api = HOST_MAX_TEST + '/cashbackholic/store?token=107de22963d510d53601e8d6c21a3e53'
        self.monitor_api = HOST_MAX_TEST + "/stores/rebate?token=25c16a7b6351412d7fbdb74ccaf40d0f"
        self.msg = DingTalk()

    def thecashback(self):
        r = requests.get(url=self.thecashback_api).json()
        try:
            sign_up_url = r["list"]["sign_up"]["sign_up_url"]
            store_data = r["list"]["store_data"]
            if store_data == ' ' or sign_up_url == ' ':
                self.msg.execution("Maxrebates", 'TheCashBack.kr数据异常, 请及时处理; 数据返回为空')
            elif store_data != " ":
                for i in range(len(store_data)):
                    rebate = store_data[i]["rebate"]
                    if re.match("^([^\d]*)0([^\d]*) Cash Back", rebate) is not None:
                        self.msg.execution("Maxrebates", "[Thecashback] 商家 {}".format(store_data[i]["name"]) + "({})".format(store_data[i]["rebate"]) + " 数据异常！")
            # self.msg.execution("执行完毕！！Thecashback未发现异常数据")
        except IndexError:
            self.msg.execution("Maxrebates", 'TheCashBack.kr数据异常, 请及时处理')
        except KeyError:
            self.msg.execution("Maxrebates", 'TheCashBack.kr数据异常, 请及时处理')

    def holic(self):
        r = requests.get(url=self.holic_api).json()
        try:
            store_data = r["list"]
            if store_data == ' ':
                self.msg.execution("Maxrebates", 'TheCashBackHolic数据异常, 请及时处理')
            elif store_data != " ":
                for i in range(len(store_data)):
                    rebate = store_data[i]["rebate"]
                    if re.match("^([^\d]*)0([^\d]*) Cash Back", rebate) is not None:
                        self.msg.execution("Maxrebates", "[holic] 商家 {}".format(store_data[i]["name"]) + "({})".format(
                            store_data[i]["rebate"]) + " 数据异常！")
                # self.msg.execution("执行完毕！！Holic未发现异常数据")
        except IndexError:
            self.msg.execution("Maxrebates", 'TheCashBackHolic数据异常, 请及时处理')
        except KeyError:
            self.msg.execution("Maxrebates", 'TheCashBackHolic数据异常, 请及时处理')

    def monitor(self):
        result = requests.get(url=self.monitor_api).json()
        try:
            storeRebate = result["list"]
            for i in range(len(storeRebate)):
                rebate = storeRebate[i]["rebate"]
                # high_rebate = storeRebate[i]["high_rebate"]
                if re.match("^([^\d]*)0([^\d]*) Cash Back", rebate) is not None:
                    self.msg.execution("Maxrebates", "[Thecashback] 商家 {}".format(storeRebate[i]["name"]) + "({})".format(
                        storeRebate[i]["rebate"]) + " 数据异常！")
            # self.msg.execution("执行完毕！！Monitor未发现异常数据")
        except IndexError:
            self.msg.execution("Maxrebates", 'monitor数据异常, 请及时处理')
        except KeyError:
            self.msg.execution("Maxrebates", 'monitor数据异常, 请及时处理')


if __name__ == '__main__':
    T = PriceComparisonWeb()
    T.thecashback()
    T.holic()
    T.monitor()
