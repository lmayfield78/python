from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from tools.text_search import Text
import time


class SpsStep2():

    def __init__(self, driver):
        self.driver = driver

    def spsStep2Pass(self):

        time.sleep(2)
        firstname = self.driver.find_element(By.ID, "first_name")
        firstname.send_keys("Lawrence")

        lastname = self.driver.find_element(By.ID, "last_name")
        lastname.send_keys("Mayfield")

        email = self.driver.find_element(By.ID, "email")
        email.send_keys("lmayfield@spscoach.com")

        phone = self.driver.find_element(By.ID, "phone")
        phone.send_keys("1234567890")

        address = self.driver.find_element(By.ID, "shipping_address")
        address.send_keys("9111 Research Blvd.")

        countryDropdown = Select(self.driver.find_element(By.ID, "shipping_country"))
        countryDropdown.select_by_value("226")

        statedrop = Select(self.driver.find_element(By.ID, "shipping_state"))
        statedrop.select_by_value("Texas")

        city = self.driver.find_element(By.ID, "shipping_city")
        city.send_keys("Austin")

        zipCode = self.driver.find_element(By.ID, "shipping_zipcode")
        zipCode.send_keys("78758")

        agreeTerms = self.driver.find_element(By.ID, "trial_agreement")
        agreeTerms.click()

        claimButton = self.driver.find_element(By.ID, "submit_button")

        from tools.text_search import Text
        print("============  sps step 2 Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== sps step 2 banned words finish  ===============")

        claimButton.click()
