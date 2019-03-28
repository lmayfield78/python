import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from tools.text_search import Text


class aa40Advanced():

    def __init__(self, driver):
        self.driver = driver

    def qualifyClick(self):

        light = self.driver.find_element(By.CLASS_NAME, "lightSwitcher")
        light.click()

        time.sleep(3)

        qualifyButton = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-block")
        print("============  aa40Advanced Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== aa40Advanced banned words finish  ===============")
        qualifyButton.click()






