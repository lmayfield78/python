from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from tools.text_search import Text
import time

class leptinshred_step2():

    def __init__(self, driver):
        self.driver = driver

    def leptin_step2_normal(self):

        time.sleep(2)

        #first name
        firstname = self.driver.find_element(By.ID, "first_name")
        firstname.send_keys("Lawrence")

        #last name
        lastname = self.driver.find_element(By.ID, "last_name")
        lastname.send_keys("Mayfield")

        #email
        email = self.driver.find_element(By.ID, "email")
        email.send_keys("lmayfield@spscoach.com")

        #phone
        phone = self.driver.find_element(By.ID, "phone")
        phone.send_keys("512123456")

        #address
        address = self.driver.find_element(By.ID, "shipping_address")
        address.send_keys("911 Research Blvd")

        #country
        country = Select(self.driver.find_element(By.ID, "shipping_country"))
        country.select_by_value("226")

        #state
        state = Select(self.driver.find_element(By.ID, "shipping_state"))
        state.select_by_value("Texas")

        #city
        city = self.driver.find_element(By.ID, "shipping_city")
        city.send_keys("Austin")

        #zip code
        zipcode = self.driver.find_element(By.ID, "shipping_zipcode")
        zipcode.send_keys("78758")

        #click here button
        button = self.driver.find_element(By.ID, "submit_button")


        print("============  leptin shred 2 Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== leptin shred 2 banned words finish  ===============")

        button.click()