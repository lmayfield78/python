from selenium import webdriver
from selenium.webdriver.common.by import By
from tools.text_search import Text



class Test_Max_Index():

    def __init__(self, driver):
        self.driver = driver

    def testMax_normal_button(self):

        clickHereButton = self.driver.find_element(By.ID, 'video')

        print("============  Tmax Index Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== Tmax Index banned words finish  ===============")
        clickHereButton.click()





