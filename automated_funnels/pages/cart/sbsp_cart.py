from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


class sbsp_cart():

    def __init__(self, driver):
        self.driver = driver

    def sbsp_cart_pass(self):
        #card type
        CardType = Select(self.driver.find_element(By.ID, "creditcardtype"))
        CardType.select_by_value("amex")

        #CC number
        cc_number = self.driver.find_element(By.ID, "creditcardnumber")
        cc_number.send_keys("379568521301035")

        #Month expire
        mo_expire = Select(self.driver.find_element(By.ID, "expirationMonth"))
        mo_expire.select_by_value("05")

        #Year expire
        yr_expire = Select(self.driver.find_element(By.ID, "expirationYear"))
        yr_expire.select_by_value("22")

        #security code
        security_code = self.driver.find_element(By.ID, "CVV")
        security_code.send_keys("9707")

        #agree
        trial = self.driver.find_element(By.ID, "TrialAgreement")
        trial.click()

        #complete button
        complete = self.driver.find_element(By.CSS_SELECTOR, ".purchase-button.btn.btn-warning.btn-block")
        complete.click()

        time.sleep(10)

