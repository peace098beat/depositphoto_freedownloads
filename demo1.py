# -*- coding:utf-8 -*-
"""
id で取得: driver.find_element_by_id('ID')
class で取得: driver.find_element_by_class_name('CLASS_NAME')
name で取得: driver.find_element_by_name('NAME')
link textで取得: driver.find_elements_by_link_text('LINK_TEXT')
ネストされた要素は path を指定して取得: driver.find_elements_by_xpath(".//a")
"""
import time
from selenium import webdriver

#Depositphotos 情報
ID = "***"
PASS = "***"
ROOT_URL = "https://jp.depositphotos.com"

#webdriverをセットしトップページを表示
browser = webdriver.Chrome()
browser.get("ROOT_URL")

#ログインのリンクをクリック
browser.find_element_by_class_name("_btn-sign-in").click()
time.sleep(1)

#IDとパスワードを入力
browser.find_element_by_name("webId").send_keys(ID)
browser.find_element_by_name("webPassword").send_keys(PASS)
browser.find_element_by_name("submit1").click()
time.sleep(5)

#誕生日のラジオボタンを選択し入力
browser.find_element_by_xpath("//*[@id='addAuthSelect2']").click()
browser.find_element_by_id("webBirthDay").send_keys(BIRTHDAY)
browser.find_element_by_id("submit").click()
time.sleep(5)

#請求額のリンクをクリック
browser.find_element_by_class_name("btnBg").click()
time.sleep(3)

#操作ブラウザを変更
browser.switch_to_window(browser.window_handles[1])
time.sleep(3)

#未確定分と確定分の支払金額取得
undecided = browser.find_element_by_xpath("//td[2]").text
decision = browser.find_element_by_xpath("//tbody/tr[2]/td[2]").text

#利用残高のページに移動
browser.find_element_by_id("menu11").click()
time.sleep(1)

#利用残高の取得
loan = browser.find_element_by_xpath('//div[@id="container"]/div[1]/div[5]/div[2]/table/tbody/tr[2]/td[1]').text
browser.quit()

#表示
print(u"未確定分:" + decision)
print(u"　確定分：" + undecided)
print(u"支払残高：" + loan)
