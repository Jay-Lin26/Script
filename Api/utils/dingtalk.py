import base64
import hashlib
import hmac
import time
import urllib.parse

import requests


class DingTalk:
    def __init__(self):
        self.timestamp = str(round(time.time() * 1000))
        secret = 'SEC7edb7882c53c3b4dda55d2c4b495789e6aebcbeb295bf6e480c30443a230b618'
        secret_enc = secret.encode('utf-8')
        str_sign = "{}\n{}".format(self.timestamp, secret)
        str_sign_enc = str_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, str_sign_enc, digestmod=hashlib.sha256).digest()
        self.sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

    def execution(self, message):
        params = {
            "access_token": "d010a68e3c5685a83fefa6e2e5809c6c388fdcff856539a62eb15a9faee7e326",
            "timestamp": self.timestamp,
            "sign": self.sign
        }
        headers = {
            "Content-Type": "application/json;charset=utf-8"
        }
        data = {
                    "at": {
                        "atMobiles": [],
                        "atUserIds": [],
                        "isAtAll": False
                    },
                    "text": {
                        "content": "[Maxrebates] " + message
                    },
                    "msgtype": "text"
        }
        requests.post(
            url="https://oapi.dingtalk.com/robot/send",
            params=params,
            headers=headers,
            json=data
        )