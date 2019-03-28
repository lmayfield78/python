from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tools.text_search import Text

class sbsp_Index():

    def __init__(self, driver):
        self.driver = driver

    def sbsp_index_button(self):
        '''
        Button click to move to step 2
        :return:
        '''
        button = self.driver.find_element(By.ID, "video")
        print("============  sbsp_Index Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== sbsp_Index banned words finish  ===============")
        button.click()
        time.sleep(3)



