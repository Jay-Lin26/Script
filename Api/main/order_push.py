import requests
from Libs.encryption import Encrypt

# requests请求参数
# Post
# data => form_data
# json => raw
# Get
# params => params
encrypt = Encrypt()
# 参数变动后需要重新获取token
c_source = "maxrebates"
c_affiliate_id = "2"
c_order_id = "W937976577"
salt = "FUii1omnjo_0-9aAnv"
token = encrypt.md5(c_source, c_affiliate_id, c_order_id, salt)
# 接口json参数
data = {
    "c_id": 27121613,  # 适配器订单主键
    "c_affiliate_id": c_affiliate_id,   # 联盟id
    "c_track": "v3yzsf",
    "c_merchant": "LUISAVIAROMA",    # 商家名
    "c_merchant_id": "2547997",   # 商家唯一码
    "c_order_id": c_order_id,
    "c_purchase_amount": "272.8300",    # 交易金额
    "c_cashback": "27.28",  # 给平台的佣金
    "c_cashback_to_user": "0.0000",  # 不用填
    "c_currency": "USD",
    "c_quantity": "1",
    "c_transaction_date": "1630585904",     # 交易时间
    "c_transaction_raw_datetime": "",
    "c_report_date": "1630585904",
    "c_status": "0",
    "c_source": c_source,   # 来源
    "c_callback": "0",
    "c_callback_lasttime": "0",
    "c_create_date": "1630585904",
    "c_update_date": "1630585904",
    "push_amount": "0.0000",
    "push_qty": "0",
    "push_commission": "0.0000",
    "is_compared": "0",
    "last_compare_time": "0",
    "c_account_source": c_source,   # 账号来源
    "c_order_details": "",
    "d_origin_flag": "1",
    "d_origin_currency": "CNY",
    "d_origin_amount": "7074.3400",
    "d_origin_commission": "141.4800",
    "c_subUnionId": "13",
    "c_orig_transaction_date": "",
    "token": token
}
headers = {
    "v": "v3.1"
}
url = "https://dashboard.staging.51huaji.com/orderapi/add_orders"
result = requests.post(url=url, headers=headers, data=data).text
print(result)