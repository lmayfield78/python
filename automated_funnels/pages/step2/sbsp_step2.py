from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from tools.text_search import Text
import time


class sbsp_step2():

    def __init__(self, driver):
        self.driver = driver


    def sbsp_step2_pass(self):

        #firstname
        FirstName = self.driver.find_element(By.ID, "first_name")
        FirstName.send_keys("Lawrence")

        #last name
        LastName = self.driver.find_element(By.ID, "last_name")
        LastName.send_keys("Mayfield")

        #email
        email = self.driver.find_element(By.ID, "email")
        email.send_keys("lmayfield@spscoach.com")

        #phone
        phone = self.driver.find_element(By.ID, "phone")
        phone.send_keys("1231231234")

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

        #zipcode
        zipcode = self.driver.find_element(By.ID, "shipping_zipcode")
        zipcode.send_keys("78758")

        #agree
        checkbox = self.driver.find_element(By.ID, "trial_agreement")
        checkbox.click()

        #submit button
        submit = self.driver.find_element(By.ID, "submit_button")
        submit.click()


        print("============  sbsp step2  Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== sbsp step 2 banned words finish  ===============")

        time.sleep(12)
