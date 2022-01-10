from src.haitao.app_v6 import ApiAutoTest


# 55海淘
App = ApiAutoTest(sheet_name="55haitao", environments="dev")
App.run()