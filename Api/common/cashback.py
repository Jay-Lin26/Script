# coding = GBK
from Libs.database import DataBase
payable_sql = "select sum(`add`)-sum(`dec`) from money_detail where uid = 8119895 and status = 'G_CONFIRMED';"
pending_sql = "select sum(`add`) from money_detail where uid = 8119895 and status = 'G_NO_CONFIRM';"
paid_sql = "select sum(amount) from cash_records where uid = 8119895 and status = 'CA_OK';"
history_sql = "select sum(`add`) from maxrebates_v2_pre.money_detail where uid = 8119895 ;"
balance_sql = ""
max_v2_pre = DataBase('maxrebates')
# Payable
payable = str(round(max_v2_pre.select(payable_sql)[0][0], 2))
print("Payable:  " + payable)
# Pending
pending = str(max_v2_pre.select(pending_sql)[0][0])
print("Pending:  " + pending)
# Paid
paid = str(max_v2_pre.select(paid_sql)[0][0])
print("Paid: " + paid)
# Lifetime Cash Back (历史总收入)
history = str(max_v2_pre.select(history_sql)[0][0])
print("Paid: " + history)
# 可提现金额 Available Balance
