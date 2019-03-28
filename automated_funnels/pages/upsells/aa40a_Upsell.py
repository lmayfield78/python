from selenium import webdriver
from selenium.webdriver.common.by import By
from tools.text_search import Text
import time


class aa40aUpsell():

    def __init__(self, driver):
        self.driver = driver

    def aa40aUpsell_pass(self):

        print("============  aa40s_Upsell Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== aa40s_Upsell banned words finish  ===============")

        addButton = self.driver.find_element(By.ID, "purchase")
        addButton.click()

        time.sleep(10)


