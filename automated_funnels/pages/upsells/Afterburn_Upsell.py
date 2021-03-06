from selenium import webdriver
from selenium.webdriver.common.by import By
from tools.text_search import Text
import time


class AfterBurnUpsell():

    def __init__(self, driver):
        self.driver = driver

    def afterBurn_Pass(self):

        print("============ Afterburn Upsell Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== Afterburn Upsell banned words finish  ===============")

        parentHandle_test = self.driver.current_window_handle

        testButton_1 = self.driver.find_element(By.LINK_TEXT, "Add To Cart")
        testButton_1.click()

        time.sleep(6)

        handles1 = self.driver.window_handles

        for handle in handles1:
            if handle not in parentHandle_test:
                self.driver.switch_to.window(handle)


        testButton_confirm = self.driver.find_element(By.XPATH, "//*[@class='confirm btn btn-success']")
        testButton_confirm.click()


        time.sleep(10)
