from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class aa40_funnel():

    url = "http://sixpackshortcuts.com/desktop/absafter40"

    def __init__(self, driver):
        self.drver = driver



    def normalPass(self):

        # =========  Load Browser and go to site  ==================
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(self.url)


        nextButton = driver.find_element(By.LINK_TEXT, "CLICK HERE TO TAKE YOUR BODY BACK TODAY!")
        nextButton.click()


        time.sleep(3)


        firstname = driver.find_element(By.ID, "first_name")
        firstname.send_keys("Lawrence")

        lastname = driver.find_element(By.ID, "last_name")
        lastname.send_keys("Mayfield")

        email = driver.find_element(By.ID, "email")
        email.send_keys("lmayfield@spscoach.com")

        phone = driver.find_element(By.ID, "phone")
        phone.send_keys("1234567890")

        address = driver.find_element(By.ID, "shipping_address")
        address.send_keys("9111 Research Blvd.")

        countryDropdown = Select(driver.find_element(By.ID, "shipping_country"))
        countryDropdown.select_by_value("226")

        statedrop = Select(driver.find_element(By.ID, "shipping_state"))
        statedrop.select_by_value("Texas")

        city = driver.find_element(By.ID, "shipping_city")
        city.send_keys("Austin")

        zipCode = driver.find_element(By.ID, "shipping_zipcode")
        zipCode.send_keys("78758")

        claimButton = driver.find_element(By.ID, "submit_button")
        claimButton.click()


        # ================  on to Cart page  =======================

        driver.implicitly_wait(20)
        time.sleep(3)

        cardType = Select(driver.find_element(By.ID, "creditcardtype"))
        cardType.select_by_value("amex")

        cc_number = driver.find_element(By.ID, "creditcardnumber")
        cc_number.send_keys("379568521301001")

        exp_Mo = Select(driver.find_element(By.ID, "expirationMonth"))
        exp_Mo.select_by_value("12")

        exp_Year = Select(driver.find_element(By.ID, "expirationYear"))
        exp_Year.select_by_value("20")

        sec_code = driver.find_element(By.ID, "CVV")
        sec_code.send_keys("3513")

        checkBox = driver.find_element(By.ID, "TrialAgreement")
        checkBox.click()

        submitButton = driver.find_element(By.NAME, "send")
        submitButton.click()

        driver.implicitly_wait(20)
        time.sleep(15)


        # =============   Upsell 1 -> AA40A  =======================
        addButton = driver.find_element(By.ID, "purchase")
        addButton.click()

        driver.implicitly_wait(20)
        time.sleep(10)

        # ==============    Upsell 2 -> TEST RELOAD  ====================


        parentHandle_test = driver.current_window_handle

        testButton_1 = driver.find_element(By.XPATH, "//*[@id='upsell_1']")
        testButton_1.click()

        time.sleep(5)

        handles1 = driver.window_handles


        for handle in handles1:
            if handle not in parentHandle_test:
                driver.switch_to.window(handle)


        testButton_confirm = driver.find_element(By.XPATH, '//button[@class="confirm btn btn-success"]')
        testButton_confirm.click()


        time.sleep(10)



        # ==============   Upsell 3 -> Leptin   =============================

        parentHandle_Leptin = driver.current_window_handle


        addButton1 = driver.find_element(By.ID, "upsell_1")
        addButton1.click()
        time.sleep(3)


        handles2 = driver.window_handles

        for handle in handles2:
            if handle not in parentHandle_Leptin:
                driver.switch_to.window(handle)


        secondButtonConfirm = driver.find_element(By.XPATH, '//button[@class="confirm btn btn-success"]')
        secondButtonConfirm.click()

        time.sleep(3)


        # =============== Complete Page ==========================

        driver.implicitly_wait(10)
        time.sleep(10)


        try:
            assert "Congratulations! You're Now A Six Pack Shortcuts VIP Client." in driver.title
            print('Test complete. Funnel has reached complete page')

        except Exception as e:
            print('Test Failed, Funnel did not reach complete page', format(e))

        finally:
            driver.quit()

test = aa40_funnel()
test.normalPass()