from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class TestMaxCart():

    def __init__(self, driver):
        self.driver = driver

    def cartNormalPass(self):

        time.sleep(2)

        cardType = Select(self.driver.find_element(By.ID, "creditcardtype"))
        cardType.select_by_value("amex")

        creditCardInput = self.driver.find_element(By.ID, 'creditcardnumber')
        creditCardInput.send_keys('379568521301035')

        expMO = Select(self.driver.find_element(By.ID, 'expirationMonth'))
        expMO.select_by_value("05")

        yearMo = Select(self.driver.find_element(By.ID, 'expirationYear'))
        yearMo.select_by_value('22')

        CVV = self.driver.find_element(By.ID, 'CVV')
        CVV.send_keys('9707')

        agreementCheckbox = self.driver.find_element(By.ID, 'TrialAgreement')
        agreementCheckbox.click()

        purchaseButton = self.driver.find_element(By.CSS_SELECTOR, ".purchase-button.btn.btn-warning.btn-block")
        purchaseButton.click()

        print('Test made it to cart')





