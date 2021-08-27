# coding = GBK
from App.common.apk import *
from App.common.element import *
from App.src.mine.account_number import login
from Libs.chrome.android_driver import AndroidOptions

"""
    修改个人资料：
    1、已登录，点击个人头像进入用户详情界面，点击编辑资料
    2、已登录，点击设置按钮，选择修改个人资料进入
    3、未登录，则跳转登录后，走选项1或选项2
"""
haitao = AndroidOptions(HUAWEI_DEVICE_INFO)
haitao.by_id_click(Mine.MINE['id'])

result = haitao.check_elements(Mine.PENDING['text'], 'text')


def update_userinfo():
    haitao.by_text_click(UserInfo.HEAD_IMG['text'])
    haitao.choose_img()
    haitao.by_text_click(UserInfo.IMG_CONFIRM['text'])
    haitao.by_text_click(UserInfo.NICK_NAME['text'])

    haitao.by_text_click(UserInfo.SEX['text'])

    haitao.by_text_click(UserInfo.CITY['text'])

    haitao.by_text_click(UserInfo.BRIEF_INTRODUCTION['text'])


if result is True:
    haitao.by_id_click(Mine.LOGIN_REGISTER['id'])
    haitao.by_text_click(Mine.MODIFY_DATA['text'])
    update_userinfo()
elif result is False:
    login()
    haitao.by_id_click(Mine.SETTING['id'])
    haitao.by_text_click(Mine.SETTING_TAB[2])
    update_userinfo()