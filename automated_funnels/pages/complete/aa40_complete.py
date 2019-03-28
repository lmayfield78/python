from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Complete_aa40():

    def __init__(self, driver):
        self.driver = driver

    def completePage_verify(self):

        time.sleep(10)

        try:
            assert "Congratulations! You're Now A Six Pack Shortcuts VIP Client." in self.driver.title
            print('Test complete. Funnel has reached complete page')

        except Exception as e:
            print('Test Failed, Funnel did not reach complete page', format(e))

        finally:
            self.driver.quit()

