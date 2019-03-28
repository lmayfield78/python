from selenium.webdriver.support.select import  Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class aa40Advanced_cart():

    def __init__(self, driver):
        self.driver = driver

    def aa40Advanced_cart_normal(self):

        time.sleep(5)

        #cc type
        cardType = Select(self.driver.find_element(By.ID, "creditcardtype"))
        cardType.select_by_value("amex")

        #CC Number
        creditCardNumber = self.driver.find_element(By.ID, "creditcardnumber")
        creditCardNumber.send_keys("379568521301035")

        #cc Mo. Exp
        monthExpire = Select(self.driver.find_element(By.ID, "expirationMonth"))
        monthExpire.select_by_value("05")

        #cc Yr. Exp
        yearExpire = Select(self.driver.find_element(By.ID, "expirationYear"))
        yearExpire.select_by_value("22")

        #Security Code
        CVV = self.driver.find_element(By.ID, "CVV")
        CVV.send_keys("9707")

        #Agree
        agree = self.driver.find_element(By.ID, "TrialAgreement")
        agree.click()

        #Complete Button
        completePurchase = self.driver.find_element(By.CSS_SELECTOR, ".purchase-button.btn.btn-warning.btn-block")
        completePurchase.click()



