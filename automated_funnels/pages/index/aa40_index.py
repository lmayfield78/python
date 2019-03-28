from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from tools.text_search import Text


class aa40_Index():


    def __init__(self,driver):
        self.driver = driver


    def turnLightsON(self):
        lightsOn = self.driver.find_element(By.ID, "shadow")
        lightsOn.click()




    def surveyAndSubmit(self, firstName, lastName, email, phone):
        '''
        This will fill out the customer survey and submit user information.

        :param lastName:
        :param email:
        :param phone:
        :return:
        '''

        firstNameInput = self.driver.find_element(By.ID, "first_name")
        firstNameInput.send_keys(firstName)

        lastNameIput = self.driver.find_element(By.ID, "last_name")
        lastNameIput.send_keys(lastName)

        emailInput = self.driver.find_element(By.ID, "email")
        emailInput.send_keys(email)

        phoneInput = self.driver.find_element(By.ID, "phone")
        phoneInput.send_keys(phone)

        submitButton = self.driver.find_element(By.ID, "hybrid-submit")


    def indexClick(self):
        '''
        This function only clicks the button that takes users to the step 2 page.
        :return:
        '''

        #This will click the first / top "Get abs after 40 now" button.

        getAbsButton1 = self.driver.find_element(By.CSS_SELECTOR, "a.btn.btn-green.btn-block.btn-qualify")
        print("============  aa40_Index Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== aa40_Index banned words finish  ===============")
        getAbsButton1.click()













