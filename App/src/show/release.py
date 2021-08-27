# coding = GBK
from random import randint

from App.common.apk import *
from App.common.element import *
from Libs.chrome.android_driver import AndroidOptions

haitao = AndroidOptions(HUAWEI_DEVICE_INFO)

_TITLE = '视客中奖几率真的高呀！超级开心哎'
_CONTENT = '不知不觉55海淘用了两年多了，从没有去争取过福利' \
           '隐形眼镜一直通过55在视客买，上个月下单突然看到居然有抽奖，一直以来错过了太多啦！' \
           '晒了一下自己的单号就收到了试用了' \
           '下次再接再厉再买#5姐送福利#'
_TAG = ['eBay', 'MAC', 'GNC', 'Vans', 'ColourPop', 'Nike', 'Coach', 'Farfetch', 'Adidas', 'SSENSE', 'SkinStore', 'Puma']
_STORE_NAME = _TAG[randint(0, len(_TAG)-1)]


# 点击发布选择照片
def choose_img():
    haitao.by_id_click(Forum.FORUM['id'])
    haitao.by_id_click(Forum.RELEASE_SHOW_BTN['id'])
    haitao.choose_img('add')
    haitao.choose_img('add')
    haitao.by_id_click(Forum.RELEASE_NEXT['id'])


# 选择标签，最多三个
def choose_tag():
    haitao.by_text_click(Forum.RELEASE_TAG['text'])
    haitao.by_id_input(Forum.TAG_INPUT_SEARCH['id'], _STORE_NAME)
    haitao.choose_tag()
    haitao.page_slide('left')
    haitao.by_id_click(Forum.RELEASE_TAG['id'])
    haitao.by_id_input(Forum.TAG_INPUT_SEARCH['id'], _STORE_NAME)
    haitao.choose_tag()
    haitao.by_id_click(Forum.RELEASE_NEXT['id'])


# 填写发布内容
def content():
    haitao.by_id_input(Forum.SHOW_TITLE['id'], _TITLE)
    haitao.by_id_input(Forum.SHOW_CONTENT['id'], _CONTENT)


# 选择活动
def choose_activity():
    haitao.by_id_click(Forum.SHOW_ACTIVITY['id'])
    haitao.choose_activity()
    haitao.by_text_click(Forum.ACTIVITY_CONFIRM['text'])
    haitao.by_id_click(Forum.SHOW_COMMIT['id'])


if __name__ == '__main__':
    choose_img()
    choose_tag()
    content()
    choose_activity()
