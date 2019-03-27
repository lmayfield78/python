from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os
import time


class BuyNow():

    def __init__(self, driver):

        self.driver = driver

    def buy_now(self):
        '''
        This is the buy now button on the page.
        '''
        page_buy_now = self.driver.find_element(By.CSS_SELECTOR, ".fold-button.fold-buy-btn")
        page_buy_now.click()

        # This will bring the up the buy now pop-up


    def pop_one_time_purchase(self):
        '''
        This is the one time purchase radio selection of the pop up.
        '''

        onetime_radio = self.driver.find_element(By.CSS_SELECTOR, ".bold-ro__one-time-radio-btn")
        onetime_radio.click()

        buyButton = self.driver.find_element(By.ID, "send_to_cart")
        buyButton.click()

        # takes User to Cart Page


    def pop_continuity_purchase(self, driver):
        '''
        This will select the continuity radio button of the pop up.
        :return:
        '''

        continuity_button = self.driver.find_element(By.XPATH, ".//*[@id='product-actions-3567604993']/div[1]/div/div[3]/label/input")
        continuity_button.click()

        buyButton = self.driver.find_element(By.ID, "send_to_cart")
        buyButton.click()

        # takes User to Cart Page


