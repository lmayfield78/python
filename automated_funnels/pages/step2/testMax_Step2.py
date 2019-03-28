from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from tools.text_search import Text
import time


class TestMax_Step2():

    def __init__(self, driver):
        self.driver = driver

    def tmax_normal_pass(self):

        time.sleep(2)

        firstName = self.driver.find_element(By. ID, 'first_name')
        firstName.send_keys('Lawrence')

        lastName = self.driver.find_element(By.ID, 'last_name')
        lastName.send_keys("Mayfield")

        email = self.driver.find_element(By.ID, 'email')
        email.send_keys('lmayfield@spscoach.com')

        phone = self.driver.find_element(By.ID, 'phone')
        phone.send_keys('1231231230')

        address = self.driver.find_element(By.ID, 'shipping_address')
        address.send_keys('9111 Research Blvd')

        countryDropdown = Select(self.driver.find_element(By.ID, "shipping_country"))
        countryDropdown.select_by_value("226")

        stateDrop = Select(self.driver.find_element(By.ID, "shipping_state"))
        stateDrop.select_by_value("Texas")

        city = self.driver.find_element(By.ID, "shipping_city")
        city.send_keys("Austin")

        zipcode = self.driver.find_element(By.ID, 'shipping_zipcode')
        zipcode.send_keys('78758')

        submit_button = self.driver.find_element(By.ID, 'submit_button')


        print("============  testmax step 2 Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== testmax step 2 banned words finish  ===============")

        submit_button.click()


