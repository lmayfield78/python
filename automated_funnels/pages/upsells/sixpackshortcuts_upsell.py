from selenium import webdriver
from selenium.webdriver.common.by import By
from tools.text_search import Text
import time

class sixpackshortcuts_upsell():

    def __init__(self, driver):
        self.driver = driver

    def sixpackshortcuts_normal_upsell(self):

        print("============  sps upsell Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== sps upsell banned words finish  ===============")

        button = self.driver.find_element(By.CSS_SELECTOR, ".text-center>img")
        button.click()

        time.sleep(4)