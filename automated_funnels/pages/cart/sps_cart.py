from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class Sps_Cart():

    def __init__(self, driver):
        self.driver = driver

    def sps_cart_pass(self):

        time.sleep(3)

        cardType = Select(self.driver.find_element(By.ID, "creditcardtype"))
        cardType.select_by_value("amex")

        cc_number = self.driver.find_element(By.ID, "creditcardnumber")
        cc_number.send_keys("379568521301035")

        exp_Mo = Select(self.driver.find_element(By.ID, "expirationMonth"))
        exp_Mo.select_by_value("05")

        exp_Year = Select(self.driver.find_element(By.ID, "expirationYear"))
        exp_Year.select_by_value("22")

        sec_code = self.driver.find_element(By.ID, "CVV")
        sec_code.send_keys("9707")

        checkBox = self.driver.find_element(By.ID, "TrialAgreement")
        checkBox.click()

        submitButton = self.driver.find_element(By.NAME, "send")
        submitButton.click()

        time.sleep(15)