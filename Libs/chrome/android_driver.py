# coding = GBK
import sys
from random import randint
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import *
from urllib3.exceptions import *


class AndroidOptions(object):
    def __init__(self, apk):
        try:
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', apk)
            self.driver.implicitly_wait(8)
        except WebDriverException as e:
            print(e)
            sys.exit(1)
        except MaxRetryError:
            print({
                "code": 0,
                "msg": "无法连接至http://127.0.0.1:4723/wd/hub；请检查appium客户端是否启动"
            })
            sys.exit(1)

    # 通过id定位 => 点击
    def by_id_click(self, element):
        if element == ' ':
            print("element为空；请补充元素后重试！！！")
            sys.exit(1)
        try:
            self.driver.find_element_by_id(element).click()
        except NoSuchElementException:
            try:
                resource_id = 'new UiSelector().resourceId("%s")' % element
                self.driver.find_element_by_android_uiautomator(resource_id).click()
            except NoSuchElementException:
                print('请检查元素 "%s" 是否有误！！！' % element)
                sys.exit(1)

    # 通过id定位 => 输入
    def by_id_input(self, element, content):
        if element == ' ':
            print("element为空；请补充元素后重试！！！")
            sys.exit(1)
        try:
            self.driver.find_element_by_id(element).send_keys(content)
        except NoSuchElementException:
            try:
                resource_id = 'new UiSelector().resourceId("%s")' % element
                self.driver.find_element_by_android_uiautomator(resource_id).send_keys(content)
            except NoSuchElementException:
                print('请检查元素 "%s" 是否有误！！！' % element)
                sys.exit(1)

    # 通过text定位 => 点击
    def by_text_click(self, element):
        if element == ' ':
            print("element为空；请补充元素后重试！！！")
            sys.exit(1)
        try:
            text = 'new UiSelector().text("%s")' % element
            self.driver.find_element_by_android_uiautomator(text).click()
        except NoSuchElementException:
            print('请检查元素 "%s" 是否有误！！！' % element)
            sys.exit(1)

    # 通过name/text定位 => 输入
    def by_text_input(self, element, content):
        if element == ' ':
            print("element为空；请补充元素后重试！！！")
            sys.exit(1)
        try:
            text = 'new UiSelector().text("%s")' % element
            self.driver.find_element_by_android_uiautomator(text).send_keys(content)
        except NoSuchElementException:
            print('请检查元素 "%s" 是否有误！！！' % element)
            sys.exit(1)

    # 判断元素是否存在 True/False
    def check_elements(self, element, attribute):
        """
        :param element: 定位值
        :param attribute: 标签类型id/text
        :return: Ture or False
        """
        resource_id = 'new UiSelector().resourceId("%s")' % element
        text = 'new UiSelector().text("%s")' % element
        try:
            if attribute == 'id':
                self.driver.find_element_by_android_uiautomator(resource_id)
                return True
            elif attribute == 'text':
                self.driver.find_element_by_android_uiautomator(text)
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    # 登录、注册滑动验证界面
    def slide_verification(self):
        """ """
        TouchAction(self.driver).press(x=250, y=600).move_to(x=900, y=600).release().perform()

    # 页面滑动
    def page_slide(self, direction):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        _x = round(width/2)
        _y = round(height/2)
        # 以手指为标准
        if direction == "down":
            move = TouchAction(self.driver).press(x=_x, y=round(height*0.3)).move_to(x=_x, y=round(height-(height*0.1))).perform()
            return move
        elif direction == "up":
            move = TouchAction(self.driver).press(x=_x, y=round(height-(height*0.1))).move_to(x=_x, y=round(height*0.1)).perform()
            return move
        elif direction == "right":
            move = TouchAction(self.driver).press(x=round(width*0.1), y=_y).move_to(x=round(width-(width*0.1)), y=_y).perform()
            return move
        elif direction == "left":
            move = TouchAction(self.driver).press(x=round(width-(width*0.1)), y=_y).move_to(x=round(width*0.1), y=_y).release().perform()
            sleep(3)
            return move

    # 选择图片
    def choose_img(self, method):
        try:
            if method == 'add':
                element = 'com.haitao:id/img_check'
                resource_id = 'new UiSelector().resourceId("%s")' % element
                img = self.driver.find_elements_by_android_uiautomator(resource_id)
                choose_img = img[randint(0, len(img)-1)]
                return choose_img.click()
            elif method == 'edit':
                element = 'com.haitao:id/img_check'
                resource_id = 'new UiSelector().resourceId("%s")' % element
                img = self.driver.find_elements_by_android_uiautomator(resource_id)
                edit_image = img[0]
                return edit_image.click()
        except NoSuchElementException:
            element = 'com.haitao:id/img'
            resource_id = 'new UiSelector().resourceId("%s")' % element
            img = self.driver.find_elements_by_android_uiautomator(resource_id)
            choose_img = img[randint(0, len(img) - 1)]
            return choose_img.click()

    # 选择标签搜索内容
    def choose_tag(self):
        try:
            element = "标签"
            resource_id = 'new UiSelector().text("%s")' % element
            tags = self.driver.find_elements_by_android_uiautomator(resource_id)
            tag = tags[randint(0, len(tags))]
            sleep(1)
            return tag.click()
        except NoSuchElementException:
            print("......新增标签")
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("添加")').click()

    # 选择活动
    def choose_activity(self):
        element = "com.haitao:id/img_tag_logo"
        resource_id = 'new UiSelector().resourceId("%s")' % element
        activities = self.driver.find_elements_by_android_uiautomator(resource_id)
        activity = activities[randint(0, len(activities)-1)]
        sleep(1)
        return activity.click()

    # 退出
    def quit(self):
        print("执行完毕~~~~")
        self.driver.quit()