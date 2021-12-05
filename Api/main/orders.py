# coding = GBK
from Libs.database import DataBase
# max_v2_pre, affiliate_project
max_v2_pre = DataBase('maxrebates')
affiliate_project = DataBase('affiliate_project')
# 1、创建数据intergrate_order
track = 'spb_v3cxv8'
store_name = 'ebay'
merchant_code = '41610'
order_id = "1-60884221"
m_code = " select alliance_code from alliance_store where store_id = 1 and is_disabled = 1 "
sql = """
    update intergrate_order 
    set c_track = {track}, c_merchant = {store_name}, c_merchant_id = {merchant_code}
    where c_order_id = {order_id}
"""
_merchant_code = max_v2_pre.select(m_code)
affiliate_project.select(sql.format(track=track, store_name=store_name, merchant_code=merchant_code, order_id=order_id))
print(_merchant_code)
# 2、结算批次
# payment_summary
summary_sql = " select * from payment_summary where alliance_id = 1 "
# 原始币种结算数据
po_sql = " select * from payment_order where payment_id = '1911209' and order_id = '99861561114' "
# 转换为美金后的结算数据
op_sql = " select * from order_payment where payment_id = '1911209' and order_id = '99861561114' "

# 3、交易订单 （佣金与返利对比）
# orders

# 4、资金明细
# money_detail

# 5、用户可用金额
# member_extend

# 6、提现记录
# cash_records

# 、加入队列
# recalculate_queue

# 邀请奖励规则，被邀请人orders.amount >= 25 and money_detail.`add` >= 10 and money_detail.status = 'G_CONFIRMED'
# 注册奖励生效规则，orders.amount >= 25 and orders.cashback >= 10 and orders.status = 4

# 英文站注册奖励
# 注册奖励金额在$5-$50之间随机值。
# 英文站邀请奖励
# 邀请奖励金额在$5-$50之间随机值，
# 被邀请人和邀请人，获得的邀请奖励相同，都是$5-$50之前的随机值。
# 邀请奖励生效规则
# 被邀请人，购物返利满$25，邀请奖励才生效（邀请人和被邀请人的奖励）
# 中文站/英文站提现规则
# 首次提现门槛：已生效的购物返利余额达到 10 美元（不含非购物类返利，如注册赠送、办卡返利，推广注册赠送和网站活动赠送等）。
# When your cashback status have become payable and payable amount reaches $10, you can request it.
# 后续提现门槛：已生效的所有返利余额达到 10 美元，包括购物返利及非购物类返利。
