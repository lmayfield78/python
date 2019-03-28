from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from tools.text_search import Text
import time

class Absafter40Advanced_Step2():

    def __init__(self, driver):
        self.driver = driver

    def normalSurvey(self):

        time.sleep(1)

        #firstname
        first_name = self.driver.find_element(By.ID, "first_name")
        first_name.send_keys('Lawrence')

        #lastname
        last_name = self.driver.find_element(By.ID, "last_name")
        last_name.send_keys("Mayfield")

        #email
        email = self.driver.find_element(By.ID, "email")
        email.send_keys("lmayfield@spscoach.com")

        #phone
        phone = self.driver.find_element(By.ID, "phone")
        phone.send_keys('1234567890')

        #address
        address = self.driver.find_element(By.ID, "shipping_address")
        address.send_keys("9111 Research Blvd")

        #country
        country = Select(self.driver.find_element(By.ID, "shipping_country"))
        country.select_by_value("226")

        #state
        statedrop = Select(self.driver.find_element(By.ID, "shipping_state"))
        statedrop.select_by_value("Texas")

        #city
        city = self.driver.find_element(By.ID, "shipping_city")
        city.send_keys("Austin")

        #zipcode
        zipcode = self.driver.find_element(By.ID, "shipping_zipcode")
        zipcode.send_keys("78758")

        #claim Button click
        submitButton = self.driver.find_element(By.ID, "submit_button")

        print("============  aa40a_step2 Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== aa40a_step2 banned words finish  ===============")
        submitButton.click()
