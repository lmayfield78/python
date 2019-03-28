from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class leptinshred_cart():

    def __init__(self, driver):
        self.driver = driver


    def leptinShred_normal_cart(self):

        time.sleep(2)

        #cctype
        cctype = Select(self.driver.find_element(By.ID, "creditcardtype"))
        cctype.select_by_value("amex")

        #ccnumber
        ccnumber = self.driver.find_element(By.ID, "creditcardnumber")
        ccnumber.send_keys("379568521301035")

        #cc_expireMo
        cc_expireMo = Select(self.driver.find_element(By.ID, "expirationMonth"))
        cc_expireMo.select_by_value("05")

        #cc_year
        cc_year = Select(self.driver.find_element(By.ID, "expirationYear"))
        cc_year.select_by_value("22")

        #CC_CVV
        CVV = self.driver.find_element(By.ID, "CVV")
        CVV.send_keys("9707")

        #18 confirm
        confirm18 = self.driver.find_element(By.ID, "ageCheck")
        confirm18.click()

        #agree
        agree = self.driver.find_element(By.ID, "TrialAgreement")
        agree.click()

        #Button
        button = self.driver.find_element(By.CSS_SELECTOR, ".purchase-button.btn.btn-warning.btn-block")
        button.click()

        time.sleep(10)

