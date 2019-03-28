from selenium import webdriver
from selenium.webdriver.common.by import By
from tools.text_search import Text
import time


class insanehomefatloss():

    def __init__(self, driver):
        self.driver = driver

    def insanehomefatloss_upsell(self):

        print("============  insanehomefatloss upsell Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== insanehomefatloss upsell banned words finish  ===============")

        button = self.driver.find_element(By.CSS_SELECTOR, ".text-center>img")
        button.click()
        time.sleep(5)