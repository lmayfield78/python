from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tools.text_search import Text


class TestReload_Index():

    def __init__(self, driver):
        self.driver = driver

    def testReload_index_claim(self):

        # this turns the lights on
        lightsOff = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.toggle-on")
        lightsOff.click()

        time.sleep(1)

        claimButton =  self.driver.find_element(By.CSS_SELECTOR, "#form")
        print("============  Test Reload Index Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== Test Reload Index banned words finish  ===============")
        claimButton.click()

