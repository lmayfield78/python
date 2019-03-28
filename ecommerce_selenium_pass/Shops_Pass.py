from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import  ActionChains
import os
import time


class Shop_passes():


    def Shop_Abs_Max(self):

        try:
            driver = webdriver.Firefox()
            driver.get("https://shop.seniorityhealth.com/")
            driver.maximize_window()

            # ===============   Open chrome browser  =================
            #driverLocation = "/Users/spsonline1/lib/chromedriver"
            #os.environ["webdriver.chrome.driver"] = driverLocation
            #driver = webdriver.Chrome(driverLocation)
            #driver.get("https://shop.sixpackabs.com/")
            #driver.maximize_window()

            # ============  Index -> lick on supplement  ===============
            suppNavButton = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default")
            suppNavButton.click()

            #  =================   Leptin Page   ============================
            page_buy_now = driver.find_element(By.CSS_SELECTOR, ".fold-button.fold-buy-btn")
            page_buy_now.click()
            time.sleep(2)

            # ===============   pop up -> continuity Button  ========================
            continuity_button = driver.find_element(By.CSS_SELECTOR,
                                                         ".bold-ro__radio-div.bold-ro__recurring-div.bold-ro__sub")
            continuity_button.click()

            buyButton = driver.find_element(By.ID, "send_to_cart")
            buyButton.click()

            #===================== CART  ==================================


            checkOutButton = driver.find_element(By.XPATH, "//input[@name='checkout']")
            checkOutButton.click()

            # ====================  customer_info   =========================


            email = driver.find_element(By.CSS_SELECTOR, ".customer_email")
            email.send_keys("lmayfield@spscoach.com")

            firstName = driver.find_element(By.ID, "checkout_shipping_address_first_name")
            firstName.send_keys("Lawrence")

            LastName = driver.find_element(By.ID, "checkout_shipping_address_last_name")
            LastName.send_keys("Mayfield")

            AddressInput = driver.find_element(By.ID, "checkout_shipping_address_address1")
            AddressInput.send_keys("9111 Research blvd")

            city = driver.find_element(By.ID, "checkout_shipping_address_city")
            city.send_keys("Austin")

            country = Select(driver.find_element(By.ID, "checkout_shipping_address_country"))
            country.select_by_value("US") #This will be different depending on continuity/single option - Set for Cont.

            time.sleep(1)
            state = Select(driver.find_element(By.CSS_SELECTOR, ".address_info.province"))
            state.select_by_value("TX") #This will be different depending on continuity/single option - Set for Cont.

            zipcode = driver.find_element(By.ID, "checkout_shipping_address_zip")
            zipcode.send_keys("78758")

            phone = driver.find_element(By.ID, "checkout_shipping_address_phone")
            phone.send_keys("1235555555")

            continueShipping = driver.find_element(By.CSS_SELECTOR, ".btn.continue_btn")
            continueShipping.click()

            # driver.implicitly_wait(5)
            # continuePayment = driver.find_element(By.CSS_SELECTOR, ".btn.btn--primary")
            # continuePayment.click()


            time.sleep(2)

            title = driver.title

            if title == "Seniority Health Shop - Checkout":
                print("You have reached " + title)
                print("You have reached the end")
            else:
                print("Something went wrong. User did not reach the end.")

        except Exception as e:
            print("There was an error: ", format(e))
        finally:
            print("SixPack Abs Shop Pass complete")
            driver.quit()


    def Shop_Abs_Mobile(self):

        try:
            # Open Firefox and go to url
            driver = webdriver.Firefox()
            driver.get("https://shop.sixpackabs.com/")
            driver.set_window_size(375, 667)
            time.sleep(3)

            # ===============   Open chrome browser  =================
            #driverLocation = "/Users/spsonline1/lib/chromedriver"
            #os.environ["webdriver.chrome.driver"] = driverLocation
            #driver = webdriver.Chrome(driverLocation)
            #driver.get("https://shop.sixpackabs.com/")
            #driver.set_window_size(375, 667)
            #time.sleep(1)

            # ============  Index -> lick on supplement  ===============

            #page = driver.find_element(By.TAG_NAME, 'html')
            #page.send_keys(Keys.PAGE_DOWN)
            #time.sleep(2)

            suppNavButton = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default")
            suppNavButton.click()


            #  =================    Page   ============================
            #page = driver.find_element(By.TAG_NAME, 'html')
            #page.send_keys(Keys.PAGE_DOWN)
            #time.sleep(1)
            #page.send_keys(Keys.PAGE_DOWN)
            #time.sleep(1)
            #page.send_keys(Keys.ARROW_UP)
            #time.sleep(1)
            #page.send_keys(Keys.ARROW_UP)
            #time.sleep(1)


            page_buy_now = driver.find_element(By.CSS_SELECTOR, ".fold-button.fold-buy-btn")
            #page_buy_now = driver.find_element(By.XPATH, '//[@id="science-based-six-pack"]/div[1]/main/div/div/div[4]/div/div[4]/button]')
            if page_buy_now is not None:
                    print("Element is present")
            else:
                    print("element is not present")

            page_buy_now.click()

            # ===============   pop up -> continuity Button  ========================
            continuity_button = driver.find_element(By.CSS_SELECTOR,
                                                       ".bold-ro__radio-div.bold-ro__recurring-div.bold-ro__sub")
            continuity_button.click()

            buyButton = driver.find_element(By.ID, "send_to_cart")
            buyButton.click()
            time.sleep(2)

            #===================== CART  ==================================


            checkOutButton = driver.find_element(By.CLASS_NAME, 'btn')
            checkOutButton.click()
            time.sleep(2)

            # ====================  customer_info   =========================


            email = driver.find_element(By.CSS_SELECTOR, ".customer_email")
            email.send_keys("lmayfield@spscoach.com")

            firstName = driver.find_element(By.ID, "checkout_shipping_address_first_name")
            firstName.send_keys("Lawrence")

            LastName = driver.find_element(By.ID, "checkout_shipping_address_last_name")
            LastName.send_keys("Mayfield")

            AddressInput = driver.find_element(By.ID, "checkout_shipping_address_address1")
            AddressInput.send_keys("9111 Research blvd")

            city = driver.find_element(By.ID, "checkout_shipping_address_city")
            city.send_keys("Austin")

            country = Select(driver.find_element(By.ID, "checkout_shipping_address_country"))
            country.select_by_value("US") #This will be different depending on continuity/single option - Set for Cont.

            time.sleep(1)
            state = Select(driver.find_element(By.CSS_SELECTOR, ".address_info.province"))
            state.select_by_value("TX") #This will be different depending on continuity/single option - Set for Cont.

            zipcode = driver.find_element(By.ID, "checkout_shipping_address_zip")
            zipcode.send_keys("78758")

            phone = driver.find_element(By.ID, "checkout_shipping_address_phone")
            phone.send_keys("1235555555")

            continueShipping = driver.find_element(By.CSS_SELECTOR, ".btn.continue_btn")
            continueShipping.click()

            # driver.implicitly_wait(5)
            # continuePayment = driver.find_element(By.CSS_SELECTOR, ".btn.btn--primary")
            # continuePayment.click()

            time.sleep(2)

            title = driver.title

            if title == "Sixpack Store - Checkout":
                print("You have reached " + title)
                print("You have reached the end")
            else:
                print("Something went wrong. User did not reach the end.")

        except Exception as e:
            print("There was an error: ", format(e))
        finally:
            print("SixPack Abs Shop Pass complete")
            driver.quit()




    def Shop_Senior_Pass_Max(self):
        try:

            #Open Firefox and go to url
            driver = webdriver.Firefox()
            driver.get("https://shop.seniorityhealth.com/")
            driver.maximize_window()

            # ===============   Open chrome browser  =================
            #driverLocation = "/Users/spsonline1/lib/chromedriver"
            #os.environ["webdriver.chrome.driver"] = driverLocation
            #driver = webdriver.Chrome(driverLocation)
            #driver.get("https://shop.seniorityhealth.com/")
            #driver.maximize_window()

            # ============  Index -> lick on supplement  ===============
            suppNavButton = driver.find_element(By.LINK_TEXT, "TRY TEST RELOAD")
            suppNavButton.click()

            #  =================   TR Page   ============================
            page_buy_now = driver.find_element(By.CSS_SELECTOR, ".fold-button.fold-buy-btn")
            page_buy_now.click()
            time.sleep(1)


            # ===============   pop up -> continuity Button  ========================
            continuity_button = driver.find_element(By.CSS_SELECTOR,
                                                         ".bold-ro__radio-div.bold-ro__recurring-div.bold-ro__sub")
            continuity_button.click()

            buyButton = driver.find_element(By.ID, "send_to_cart")
            buyButton.click()

            #===================== CART  ==================================

            checkOutButton = driver.find_element(By.XPATH, "//input[@name='checkout']")
            checkOutButton.click()

            # ====================  customer_info   =========================

            email = driver.find_element(By.CSS_SELECTOR, ".customer_email")
            email.send_keys("lmayfield@spscoach.com")

            firstName = driver.find_element(By.ID, "checkout_shipping_address_first_name")
            firstName.send_keys("Lawrence")

            LastName = driver.find_element(By.ID, "checkout_shipping_address_last_name")
            LastName.send_keys("Mayfield")

            AddressInput = driver.find_element(By.ID, "checkout_shipping_address_address1")
            AddressInput.send_keys("9111 Research blvd")

            city = driver.find_element(By.ID, "checkout_shipping_address_city")
            city.send_keys("Austin")

            country = Select(driver.find_element(By.ID, "checkout_shipping_address_country"))
            country.select_by_value("US") #This will be different depending on continuity/single option - Set for Cont.

            time.sleep(1)
            state = Select(driver.find_element(By.CSS_SELECTOR, ".address_info.province"))
            state.select_by_value("TX") #This will be different depending on continuity/single option - Set for Cont.

            zipcode = driver.find_element(By.ID, "checkout_shipping_address_zip")
            zipcode.send_keys("78758")

            phone = driver.find_element(By.ID, "checkout_shipping_address_phone")
            phone.send_keys("1235555555")

            continueShipping = driver.find_element(By.CSS_SELECTOR, ".btn.continue_btn")
            continueShipping.click()

            # driver.implicitly_wait(5)
            # continuePayment = driver.find_element(By.CSS_SELECTOR, ".btn.btn--primary")
            # continuePayment.click()

            time.sleep(2)

            title = driver.title

            if title == "Seniority Health Shop - Checkout":
                print("You have reached " + title)
                print("You have reached the end")
            else:
                print("Something went wrong. User did not reach the end.")

        except Exception as e:
                print("There was an error: ", format(e))

        finally:
            print("Seniority Health shop pass complete")
            driver.quit()


    def Shop_Senior_Pass_Mobile(self):
        try:

            # Open Firefox and go to url
            driver = webdriver.Firefox()
            driver.get("https://shop.seniorityhealth.com/")
            driver.set_window_size(375, 667)

            # ===============   Open chrome browser  =================
            #driverLocation = "/Users/spsonline1/lib/chromedriver"
            #os.environ["webdriver.chrome.driver"] = driverLocation
            #driver = webdriver.Chrome(driverLocation)
            #driver.get("https://shop.seniorityhealth.com/")
            #driver.set_window_size(375, 800)
            time.sleep(2)


            # ============  Index -> lick on supplement  ===============
            suppNavButton = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default")
            suppNavButton.click()

            #  =================   TR Page   ============================
            page_buy_now = driver.find_element(By.CSS_SELECTOR, ".fold-button.fold-buy-btn")
            page_buy_now.click()
            time.sleep(2)

            # ===============   pop up -> continuity Button  ========================
            continuity_button = driver.find_element(By.CSS_SELECTOR,
                                                         ".bold-ro__radio-div.bold-ro__recurring-div.bold-ro__sub")
            continuity_button.click()

            buyButton = driver.find_element(By.ID, "send_to_cart")
            buyButton.click()

            #===================== CART  ==================================

            checkOutButton = driver.find_element(By.XPATH, "//input[@name='checkout']")
            checkOutButton.click()

            # ====================  customer_info   =========================

            email = driver.find_element(By.CSS_SELECTOR, ".customer_email")
            email.send_keys("lmayfield@spscoach.com")

            firstName = driver.find_element(By.ID, "checkout_shipping_address_first_name")
            firstName.send_keys("Lawrence")

            LastName = driver.find_element(By.ID, "checkout_shipping_address_last_name")
            LastName.send_keys("Mayfield")

            AddressInput = driver.find_element(By.ID, "checkout_shipping_address_address1")
            AddressInput.send_keys("9111 Research blvd")

            city = driver.find_element(By.ID, "checkout_shipping_address_city")
            city.send_keys("Austin")

            country = Select(driver.find_element(By.ID, "checkout_shipping_address_country"))
            country.select_by_value("US") #This will be different depending on continuity/single option - Set for Cont.

            time.sleep(1)
            state = Select(driver.find_element(By.CSS_SELECTOR, ".address_info.province"))
            state.select_by_value("TX") #This will be different depending on continuity/single option - Set for Cont.

            zipcode = driver.find_element(By.ID, "checkout_shipping_address_zip")
            zipcode.send_keys("78758")

            phone = driver.find_element(By.ID, "checkout_shipping_address_phone")
            phone.send_keys("1235555555")

            continueShipping = driver.find_element(By.CSS_SELECTOR, ".btn.continue_btn")
            continueShipping.click()

            # driver.implicitly_wait(5)
            # continuePayment = driver.find_element(By.CSS_SELECTOR, ".btn.btn--primary")
            # continuePayment.click()

            time.sleep(2)

            title = driver.title

            if title == "Seniority Health Shop - Checkout":
                print("You have reached " + title)
                print("You have reached the end")
            else:
                print("Something went wrong. User did not reach the end.")

        except Exception as e:
                print("There was an error: ", format(e))

        finally:
            print("Seniority Health shop pass complete")
            driver.quit()




#go = Shop_passes()
#go.Shop_Abs_Pass_Max()
#go.Shop_Abs_Mobile()
#go.Shop_Senior_Pass_Max()
#go.Shop_Senior_Pass_Mobile()


