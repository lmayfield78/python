from selenium import webdriver
from selenium.webdriver.common.by import By
from tools.text_search import Text
import time


class Aa40_Upsell():

    def __init__(self, driver):
        self.driver = driver

    def aa40Upsell_normal(self):
        print("============  aa40 Upsell Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== aa40_Index banned words finish  ===============")

        getButton = self.driver.find_element(By.LINK_TEXT, 'Get Abs After 40 Now!')
        getButton.click()
        time.sleep(6)

    def aa40Upsell_sbsp(self):
        print("============  aa40_sbsp Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== aa40_Index banned words finish  ===============")

        #Bugged https://trello.com/c/qO3xlPYy/1404-request-add-id-to-button
        upgradeButton = self.driver.find_element(By.CLASS_NAME, "buybutton")
        upgradeButton.click()



