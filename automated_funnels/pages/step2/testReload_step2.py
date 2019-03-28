from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from tools.text_search import Text
import time

class TestReload_Step2():

    def __init__(self, driver):
        self.driver = driver

    def testReload_step2_normal(self):

        time.sleep(10)

        # Agree button
        agreeButton = self.driver.find_element(By.ID, "trial_agreement")
        agreeButton.click()

        # User Info
        firstName = self.driver.find_element(By.ID, "first_name")
        firstName.send_keys("Lawrence")

        lastName = self.driver.find_element(By.ID, "last_name")
        lastName.send_keys("Mayfield")

        email = self.driver.find_element(By.ID, "email")
        email.send_keys("lmayfield@spscoach.com")

        phone = self.driver.find_element(By.ID, "phone")
        phone.send_keys("5121231234")

        address = self.driver.find_element(By.ID, "shipping_address")
        address.send_keys("911 Research Blvd")

        country = Select(self.driver.find_element(By.ID, "shipping_country"))
        country.select_by_value("226")

        state = Select(self.driver.find_element(By.ID, "shipping_state"))
        state.select_by_value("Texas")

        city = self.driver.find_element(By.ID, "shipping_city")
        city.send_keys("Austin")

        zipcode = self.driver.find_element(By.ID, "shipping_zipcode")
        zipcode.send_keys("78758")

        # Claim Button
        claimButton = self.driver.find_element(By.ID, "submit_button")

        print("============  Test Reload step 2 Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== Test Reload step 2 banned words finish  ===============")

        claimButton.click()
