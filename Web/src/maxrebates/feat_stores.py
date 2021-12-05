# coding = utf-8
from Libs.chrome.web_driver import WebOptions

mrs = WebOptions()
mrs.option("https://www.maxrebates.com")
for num in range(1, 11):
    store_card_element = "div.mrpm__double.in-middle > div:nth-child(%d)" % num
    store_card = mrs.cssEle(store_card_element)
    store_bg_img = store_card.find_element_by_css_selector("div.store-img-box.border-none").get_attribute("style").split('"')[1]
    store_img = store_card.find_element_by_css_selector("img.store-img").get_attribute("data-src")
    store_title = store_card.find_element_by_css_selector("p.store-title.en").text
    store_cashback = store_card.find_element_by_css_selector("p.store-cashback").text
    print(store_bg_img)
    print(store_img)
    print(store_title)
    print(store_cashback)
    print('-------------------------------')