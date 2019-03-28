from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Sps_survey():

    def __init__(self,driver):
        self.driver = driver

    def survey_noThanks(self):

        time.sleep(10)
        noThanks = self.driver.find_element(By.ID, "no_help")
        noThanks.click()

