from selenium import webdriver
from selenium.webdriver.common.by import By
from tools.text_search import Text
import time


class AlphaArmorUpsell():

    def __init__(self, driver):
        self.driver = driver

    def alphaArmor_Pass(self):


        print("============  AlphaArmor Upsell Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== AlphaArmor Upsell banned words finish  ===============")

        parentHandle_test = self.driver.current_window_handle

        testButton_1 = self.driver.find_element(By.CLASS_NAME, 'plan_button')
        testButton_1.click()

        time.sleep(5)

        handles1 = self.driver.window_handles

        for handle in handles1:
            if handle not in parentHandle_test:
                self.driver.switch_to.window(handle)


        testButton_confirm = self.driver.find_element(By.XPATH, '//button[@class="confirm btn btn-success"]')
        testButton_confirm.click()

        time.sleep(10)