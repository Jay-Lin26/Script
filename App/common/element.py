# coding = GBK
"""
作者：Linse

全局使用key value形式获取text或resource_id；
{"text": '', "id": ''}
页面tab切换使用下标方式获取text；
定位方式使用UiAutomator中的new UiSelector()定位resource_id和text；
source_id如果为空请务必使用text进行定位；

时间：2020:04:13 10:40
"""


# 优惠
class Deal:
    DEAL = {"text": "优惠", "id": "com.haitao:id/tab_deal"}
    DEAL_TAB = ["关注", "最新", "热榜", "专区", "国内"]
    KING_KONG_DISTRICT = ["大促汇总",   "邀请赚钱",  "热卖排行",  "首单高返", "国内返利",
                          "球鞋潮鞋",   "直邮专区",  "亚马逊海外购", "海淘攻略", "信用卡",
                          "星巴克返利",  "京东返利",   "美团外卖",   "考拉返利",  "小程序商家",
                          "淘宝返利",   "饿了么返利", "肯德基返利", "唯品会返利", "全部商家"]


# 分类
class Cate:
    CATE = {"text": "分类", "id": "com.haitao:id/tab_category"}
    CATE_TAB = ["找热卖", "找品牌", "找商家", "找转运"]


# 社区
class Forum:
    FORUM = {"text": "社区", "id": "com.haitao:id/tab_forum"}
    FORUM_TAB = ["关注", "推荐", "最新"]
    COLLECTING = {"text": '更多', "id": ''}

    RECOMMEND_BANNER = {"text": '', "id": 'com.haitao:id/iv_image'}
    RECOMMEND_STRATEGY = {"text": '海淘攻略', "id": ''}
    RECOMMEND_ANSWER = {"text": '海淘问答', "id": ''}
    RECOMMEND_UNUSED = {"text": '闲置拼单', "id": ''}
    RECOMMEND_TRANSPORT = {"text": '海淘转运', "id": ''}
    RECOMMEND_TAB = ['最新推荐', '美妆护肤', '时尚穿搭', '母婴保健', '5姐晒单']

    RELEASE_SHOW_BTN = {"text": '', "id": 'com.haitao:id/img_add_post'}
    RELEASE_NEXT = {"text": '下一步', "id": 'com.haitao:id/tv_right'}

    RELEASE_TAG= {"text": '标签', "id": "com.haitao:id/tv_tag"}
    TAG_INPUT_SEARCH = {"text": '输入标签', "id": 'com.haitao:id/et_search'}

    SHOW_CANCEL = {"text": '', "id": 'com.haitao:id/ib_cancel'}
    SHOW_COMMIT = {"text": '发布', "id": 'com.haitao:id/tv_publish'}
    SHOW_TITLE = {"text": '添加你喜欢的标题！', "id": 'com.haitao:id/et_unboxing_title'}
    SHOW_CONTENT = {"text": '写写你要晒的好东西吧！', "id": 'com.haitao:id/et_unboxing_desc'}
    MORE_EDIT_IMG = {"text": '编辑', "id": ''}
    MORE_REMOVE_IMG = {"text": '移除', "id": ''}
    MORE_FIRST_IMG = {"text": '设为封面', "id": ''}
    MORE_CANCEL = {"text": '', "id": 'com.haitao:id/ib_cancel'}

    SHOW_ACTIVITY = {"text": '话题 & 活动', "id": 'com.haitao:id/ll_select_topic_activity'}
    ACTIVITY_CANCEL = {"text": ' ', "id": 'com.haitao:id/ib_left'}
    ACTIVITY_CONFIRM = {"text": '确定', "id": 'com.haitao:id/tv_right'}
    # 已发布待审核状态下的修改
    REVIEWED_SHOW_ACTION= {"text": '', "id": 'com.haitao:id/ib_more_title'}
    EDIT_SHOW = {"text": '编辑', "id": ''}


# 我的
class Mine:
    MINE = {"text": "我", "id": "com.haitao:id/tab_mine"}
    SETTING = {"text": "设置", "id": "com.haitao:id/img_setting_title"}
    SETTING_TAB = ["手机号码绑定", "社交账号绑定", "编辑个人资料", "修改登录密码",
                   "管理提现账户", "快速填充",
                   "消息推送设置", "发布图片水印", "清除缓存", "给与好评", "用户协议", "隐私政策", "检查更新", "联系我们", "注销账户", "关于55海淘"]

    LOGIN_REGISTER = {"text": "登录/注册", "id": "com.haitao:id/tv_username"}
    MODIFY_DATA = {"text": "编辑资料", "id": ""}

    LOGOUT = {"text": "退出登录", "id": "com.haitao:id/btn_logout"}
    LOGOUT_Y = {"text": "确定", "id": "com.haitao:id/tv_confirm"}
    LOGOUT_N = {"text": "取消", "id": "com.haitao:id/tv_cancel"}

    MESSAGE = {"text": "通知", "id": "com.haitao:id/img_notification_title"}
    PRAISE = {"text": "收到的赞", "id": "com.haitao:id/tv_praise_count"}
    FANS = {"text": "粉丝", "id": "com.haitao:id/tv_fans_count"}
    FOLLOW = {"text": "关注", "id": "com.haitao:id/tv_follow_count"}
    COIN = {"text": "金币", "id": "com.haitao:id/tv_coin_count"}

    REBATE = {"text": "我的收益", "id": "com.haitao:id/tvRebate"}
    ORDERS = {"text": "购物订单", "id": "com.haitao:id/tvOrder"}
    ORDER_LOST = {"text": "丢单反馈", "id": "com.haitao:id/tv_ordre_lost_trace"}
    COUPON = {"text": "返利券", "id": "com.haitao:id/tv_coupon"}

    PENDING = {"text": "待生效返利", "id": "com.haitao:id/tv_pending_rebate_title"}
    IN_FORCE = {"text": "生效返利", "id": "com.haitao:id/tv_rebate_title"}
    WITHDRAW = {"text": "提现", "id": "com.haitao:id/tv_withdraw"}

    INVITE_FRIEND = {"text": "邀请赚钱", "id": "com.haitao:id/cl_invite_friends"}
    INVITE_RECORD = {"text": "邀请记录", "id": "com.haitao:id/cl_invite_record"}

    MORE_TAB1 = ["每日签到", "我的收藏", "收件地址", "我的发布",
                 "海淘攻略", "金币兑换", "信用卡返利", "客服"]
    MORE_TAB2 = ["专属推荐", "最近浏览", "跳转记录"]


# 修改用户信息
class UserInfo:
    HEAD_IMG = {'text': '头像', "id": ""}
    IMG_RESET = {"text": "重选", "id": "com.haitao:id/btnReselection"}
    IMG_CONFIRM = {"text": "选取", "id": "com.haitao:id/btnSelection"}
    NICK_NAME = {'text': '昵称', "id": ""}
    NICK_NAME_INPUT = {'text': '', "id": "com.haitao:id/et_nickname"}
    NICK_NAME_CANCEL = {'text': '取消', "id": "com.haitao:id/tv_cancel"}
    NICK_NAME_CONFIRM = {'text': '确定', "id": "com.haitao:id/tv_confirm"}
    SEX = {'text': '性别', "id": ""}
    SEX_MAN = {'text': '男', "id": ""}
    SEX_WOMEN = {'text': '女', "id": ""}
    SEX_CANCEL = {'text': '', 'id': 'com.haitao:id/ib_cancel'}
    CITY = {'text': '地区', "id": ""}
    BRIEF_INTRODUCTION = {'text': '简介', "id": ""}
    BRIEF_INPUT = { "text": "介绍一下自己（120字以内）","id": "com.haitao:id/et_brief_intro"}
    BRIEF_CANCEL = {"text": "取消", "id": "com.haitao:id/tv_cancel"}
    BRIEF_CONFIRM = {"text": "确定", "id": "com.haitao:id/tv_confirm"}


# L-登录注册
class Entry:
    MOBILE = {"text": "请输入手机号", "id": ""}
    VERIFICATION_CODE = {"text": "验证码", "id": ""}
    SEND_VERIFICATION_CODE = {"text": "发送验证码", "id": ""}

    ACCOUNT_LOGIN = {"text": "密码登录", "id": "com.haitao:id/tv_use_account_login"}
    MOBILE_LOGIN = {"text": "手机号登录", "id": ""}

    FORGET_PWD = {"text": "忘记密码", "id": ""}
    NEW_PASSWORD = {"text": "请输入新密码", "id": ""}
    RESET_PASSWORD = {"text": "重置密码", "id": "com.haitao:id/tv_reset_pwd"}

    USERNAME = {"text": "用户名/邮箱/手机号码", "id": ""}
    PASSWORD = {"text": "请输入登录密码", "id": ""}
    LOGIN_SUB = {"text": "立即登录", "id": "com.haitao:id/tv_account_login_commit"}

    INVITE_CODE = {"text": "输入或粘贴邀请码", "id": ""}
    INVITE_CODE_YES = {"text": "确认", "id": ""}
    INVITE_CODE_NO = {"text": "跳过", "id": ""}


