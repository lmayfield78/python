from selenium import webdriver
from selenium.webdriver.common.by import By
from tools.text_search import Text
import time


class Acceleratedabs():

    def __init__(self, driver):
        self.driver = driver

    def acceleratedabs_normal(self):


        print("============  acc_abs Upsell Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== acc_abs Upsell banned words finish  ===============")

        button = self.driver.find_element(By.CSS_SELECTOR, ".buybutton>img")
        button.click()

        time.sleep(4)