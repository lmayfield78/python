from selenium import webdriver
from selenium.webdriver.common.by import By
from tools.text_search import Text
import time


class TestReloadUpsell():

    def __init__(self, driver):
        self.driver = driver

    def testRealoadPass(self):
        #https://sixpackshortcuts.com/cart/customize/sps_testreload
        #https://sixpackshortcuts.com/cart/customize/tmax_reload


        print("============  Test Reload Upsell Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== Test Reload Upsell banned words finish  ===============")

        parentHandle_test = self.driver.current_window_handle

        testButton_1 = self.driver.find_element(By.ID, "upsell_1")
        testButton_1.click()

        time.sleep(5)

        handles1 = self.driver.window_handles

        for handle in handles1:
            if handle not in parentHandle_test:
                self.driver.switch_to.window(handle)


        testButton_confirm = self.driver.find_element(By.XPATH, "//*[@class='confirm btn btn-success']")
        testButton_confirm.click()

        time.sleep(10)



    def testRealoadPass_aa40a(self):
        # https://sixpackshortcuts.com/cart/customize/sps_testreload
        # https://sixpackshortcuts.com/cart/customize/tmax_reload


        print("============  Test Reload Upsell Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== Test Reload Upsell banned words finish  ===============")

        time.sleep(10)

        parentHandle_test = self.driver.current_window_handle

        testButton_1 = self.driver.find_element(By.CSS_SELECTOR, ".plan_button")
        testButton_1.click()

        time.sleep(5)

        handles1 = self.driver.window_handles

        for handle in handles1:
            if handle not in parentHandle_test:
                self.driver.switch_to.window(handle)

        testButton_confirm = self.driver.find_element(By.CSS_SELECTOR, ".confirm.btn.btn-success")
        testButton_confirm.click()

        time.sleep(10)

    def sps_testreload(self):


        print("============  Test Reload Upsell Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== Test Reload Upsell banned words finish  ===============")


        time.sleep(10)

        parentHandle_test = self.driver.current_window_handle

        testButton_1 = self.driver.find_element(By.CSS_SELECTOR, ".plan_button.first-option")
        testButton_1.click()

        time.sleep(5)

        handles1 = self.driver.window_handles

        for handle in handles1:
            if handle not in parentHandle_test:
                self.driver.switch_to.window(handle)

        testButton_confirm = self.driver.find_element(By.CSS_SELECTOR, ".confirm.btn.btn-success")
        testButton_confirm.click()

        time.sleep(10)



    def tmax_reload(self):


        print("============  Test Reload Upsell Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== Test Reload Upsell banned words finish  ===============")

        time.sleep(10)

        parentHandle_test = self.driver.current_window_handle

        testButton_1 = self.driver.find_element(By.CLASS_NAME, "plan_button")
        testButton_1.click()

        time.sleep(5)

        handles1 = self.driver.window_handles

        for handle in handles1:
            if handle not in parentHandle_test:
                self.driver.switch_to.window(handle)

        testButton_confirm = self.driver.find_element(By.CSS_SELECTOR, ".confirm.btn.btn-success")
        testButton_confirm.click()

        time.sleep(10)


    def sbs_reload(self):


        print("============  Test Reload Upsell Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== Test Reload Upsell banned words finish  ===============")

        time.sleep(10)

        parentHandle_test = self.driver.current_window_handle

        testButton_1 = self.driver.find_element(By.CSS_SELECTOR, ".plan_button")
        testButton_1.click()

        time.sleep(5)

        handles1 = self.driver.window_handles

        for handle in handles1:
            if handle not in parentHandle_test:
                self.driver.switch_to.window(handle)

        testButton_confirm = self.driver.find_element(By.CSS_SELECTOR, ".confirm.btn.btn-success")
        testButton_confirm.click()

        time.sleep(10)