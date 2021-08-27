# coding = GBK
from selenium import webdriver


class WebOptions(object):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=options)

    def option(self, url):
        self.driver.get(url=url)
        self.driver.implicitly_wait(3)

    def cssEle(self, element):
        result = self.driver.find_element_by_css_selector(element)
        return result

    def xpathEle(self, element):
        result = self.driver.find_element_by_xpath(element)
        return result








