from selenium import webdriver
from selenium.webdriver.common.by import By
from tools.text_search import Text
import time

class doneforyoudiet():

    def __init__(self, driver):
        self.driver = driver

    def doneforyoudiet_normal(self):


        print("============  Done for you diet Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== Done for you diet banned words finish  ===============")

        button = self.driver.find_element(By.CSS_SELECTOR, ".buy-it-now-box.center-block>a>img")
        button.click()
        time.sleep(3)