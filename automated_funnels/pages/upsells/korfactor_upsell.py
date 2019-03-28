from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class KorfactorUpsell():

    def __init__(self, driver):
        self.driver = driver

    def korfactor_upsell_sbsp(self):

        time.sleep(5)

        parentHandle = self.driver.current_window_handle

        button = self.driver.find_element(By.CSS_SELECTOR, ".plan_button")
        button.click()

        time.sleep(5)

        handles1 = self.driver.window_handles

        for handle1 in handles1:
            if handle1 not in parentHandle:
                self.driver.switch_to.window(handle1)

        secondButton = self.driver.find_element(By.CSS_SELECTOR, ".confirm.btn.btn-success")
        secondButton.click()

        time.sleep(10)









