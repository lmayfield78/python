from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tools.text_search import Text


class Sps_index():

    def __init__(self, driver):
        self.driver = driver

    def spsIndexPass(self):
        firstButton = self.driver.find_element(By.ID, "1st_cta")

        print("============  SPS Index Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("========= SPS Index banned words finish  ===============")
        firstButton.click()


    # Verification methods below