from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tools.text_search import Text


class LeptinShred_Index():

    def __init__(self, driver):
        self.driver = driver

    def leptin_index_clickhere(self):

        #click here button
        clickhereButton = self.driver.find_element(By.ID, "video-btn")

        print("============  Leptin Index Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== Leptin Index banned words finish  ===============")
        clickhereButton.click()

