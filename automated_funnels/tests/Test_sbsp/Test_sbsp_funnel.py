from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.step2.sbsp_step2 import sbsp_step2
import time
from pages.index.sbsp_index import sbsp_Index
from pages.cart.sbsp_cart import sbsp_cart
from pages.upsells.korfactor_upsell import KorfactorUpsell
from pages.upsells.aa40_Upsell import Aa40_Upsell
from pages.upsells.testReload_Upsell import TestReloadUpsell


class sbspFunnelTest():

    url = "https://deals.sixpackabs.com/science"

    def sbsp_funnel_pass(self):

        try:

            #open browser, go to site
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get(self.url)

            #Index page click next
            index = sbsp_Index(driver)
            index.sbsp_index_button()
            time.sleep(6)

            #step 2
            step2 = sbsp_step2(driver)
            step2.sbsp_step2_pass()

            #cart
            cart = sbsp_cart(driver)
            cart.sbsp_cart_pass()

            # Upsell 1
            korfactorUpsell = KorfactorUpsell(driver)
            korfactorUpsell.korfactor_upsell_sbsp()

            #Upsell 2
            aabutton = Aa40_Upsell(driver)
            aabutton.aa40Upsell_sbsp()

            #Upsell 3
            testbutton = TestReloadUpsell(driver)
            testbutton.sbs_reload()

            #completePage
            if driver.title == "Congratulations! You're Now A Science Based Six Pack VIP Client.":
                print("Transaction Complete")
        except Exception as e:
            print("Bad" + format(e))
        finally:
            driver.quit()
            print("Funnel Pass Finished.")

go = sbspFunnelTest()
go.sbsp_funnel_pass()