from selenium import webdriver
from selenium.webdriver.common.by import By
from tools.text_search import Text
import time


class LeptinShredUpsell():


    def __init__(self, driver):
        self.driver = driver


    def leptinShred_pass(self):


        print("============  Leptin Shred Upsell Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== Leptin Shred Upsell banned words finish  ===============")

        parentHandle_Leptin = self.driver.current_window_handle

        # https://sixpackshortcuts.com/cart/customize/sps_leptinshred

        addButtons_1st = self.driver.find_element(By.ID, "upsell_1")
        addButtons_1st.click()

        #addButton1 = self.driver.find_element(By.ID, "upsell_1")
        #addButton1.click()
        time.sleep(3)

        handles2 = self.driver.window_handles

        for handle in handles2:
            if handle not in parentHandle_Leptin:
                self.driver.switch_to.window(handle)

        secondButtonConfirm = self.driver.find_element(By.XPATH, '//button[@class="confirm btn btn-success"]')
        secondButtonConfirm.click()

        time.sleep(3)


    def leptinShred_pass_aa40a(self):
        '''
        This will be ran for the aa40a funnel
        :return:
        '''

        print("============  Leptin Shred Upsell Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== Leptin Shred Upsell banned words finish  ===============")

        parentHandle_Leptin = self.driver.current_window_handle

        addButtons_1st = self.driver.find_element(By.CSS_SELECTOR, ".plan_button")
        addButtons_1st.click()

        time.sleep(1)

        handles2 = self.driver.window_handles

        for handle in handles2:
            if handle not in parentHandle_Leptin:
                self.driver.switch_to.window(handle)

        secondButtonConfirm = self.driver.find_element(By.CSS_SELECTOR, '.confirm.btn.btn-success')
        secondButtonConfirm.click()

        time.sleep(5)


    def sps_leptinshred(self):
        '''
        This will be ran for sixpackshortcuts2 funnel
        :param self:
        :return:
        '''


        print("============  Leptin Shred Upsell Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== Leptin Shred Upsell banned words finish  ===============")

        parentHandle_Leptin = self.driver.current_window_handle

        addButtons_1st = self.driver.find_element(By.ID, "show_1st_modal")
        addButtons_1st.click()

        time.sleep(1)

        handles2 = self.driver.window_handles

        for handle in handles2:
            if handle not in parentHandle_Leptin:
                self.driver.switch_to.window(handle)

        secondButtonConfirm = self.driver.find_element(By.CSS_SELECTOR, '.confirm.btn.btn-success')
        secondButtonConfirm.click()


    def leptinShred_pass_sbs_leptin(self):
        '''
        This will be ran for the science base six pack funnel
        :return:
        '''


        print("============  Leptin Shred Upsell Banned words Start ===============")
        go = Text(self.driver)
        go.bannedWords(self.driver)
        print("====== Leptin Shred Upsell banned words finish  ===============")

        time.sleep(1)
        parentHandle_Leptin = self.driver.current_window_handle

        addButtons_1st = self.driver.find_element(By.CSS_SELECTOR, ".plan_button")
        addButtons_1st.click()

        time.sleep(1)

        handles2 = self.driver.window_handles

        for handle in handles2:
            if handle not in parentHandle_Leptin:
                self.driver.switch_to.window(handle)

        secondButtonConfirm = self.driver.find_element(By.CSS_SELECTOR, '.confirm.btn.btn-success')
        secondButtonConfirm.click()

        time.sleep(5)
