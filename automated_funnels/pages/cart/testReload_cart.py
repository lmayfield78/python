from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class TestReload_Cart():

    def __init__(self, driver):
        self.driver = driver

    def testReload_cartNormal(self):

        creditcardType = Select(self.driver.find_element(By.ID, "creditcardtype"))
        creditcardType.select_by_value("amex")

        creditcardNumber = self.driver.find_element(By.ID, "creditcardnumber")
        creditcardNumber.send_keys("379568521301035")

        CCMonth_expire = Select(self.driver.find_element(By.ID, "expirationMonth"))
        CCMonth_expire.select_by_value("05")

        CCYear_Expire = Select(self.driver.find_element(By.ID, "expirationYear"))
        CCYear_Expire.select_by_value("22")

        CVV = self.driver.find_element(By.ID, "CVV")
        CVV.send_keys("9707")

        #18 confirm
        check18 = self.driver.find_element(By.ID, "ageCheck")
        check18.click()

        #conditions
        conditions = self.driver.find_element(By. ID, "TrialAgreement")
        conditions.click()


        #complete

        complete = self.driver.find_element(By.CSS_SELECTOR, ".purchase-button.btn.btn-warning.btn-block")
        complete.click()

        time.sleep(10)







