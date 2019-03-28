from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.index.sps_index import Sps_index
from pages.step2.sps_step2 import SpsStep2
from pages.cart.sps_cart import Sps_Cart
from pages.upsells.leptinshred_upsell import LeptinShredUpsell
from pages.upsells.testReload_Upsell import TestReloadUpsell
from pages.upsells.Afterburn_Upsell import AfterBurnUpsell
from pages.complete.sps_survey import Sps_survey
from pages.complete.sps_complete import Complete_sps


class SpsFunnelTest():

    url = "https://sixpackshortcuts.com/desktop/sps/main/index/index"

    def Sps_Pass_Test(self):

        try:
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get(self.url)

            #Index page
            print("At index")
            index = Sps_index(driver)
            index.spsIndexPass()

            #step 2 page
            print("At Step 2")
            step2 = SpsStep2(driver)
            step2.spsStep2Pass()

            #cart
            print("At Cart")
            spsCart = Sps_Cart(driver)
            spsCart.sps_cart_pass()

            #Leptin - https://sixpackshortcuts.com/cart/customize/sps_leptinshred
            #print("At Leptin Upsell")
            #leptin = LeptinShredUpsell(driver)
            #leptin.sps_leptinshred()

            #Test Reload - https://sixpackshortcuts.com/cart/customize/sps_testreload
            print("At Test Reload")
            test = TestReloadUpsell(driver)
            test.sps_testreload()

            #AfterBurn - https://sixpackshortcuts.com/cart/customize/sps_afterburnfuel
            print("At Afterburn")
            after = AfterBurnUpsell(driver)
            after.afterBurn_Pass()

            #survey
            print("At Survey")
            sur = Sps_survey(driver)
            sur.survey_noThanks()

            #complete page
            print("At Complete Page")
            comp = Complete_sps(driver)
            comp.Sps_completePage_verify()

            print("SPS Funnel Pass Successful")
        except Exception as e:
            print('SPS Funnel Verification PASS Failed', format(e))
        finally:
            print("SPS Funnel Pass Finished")
            driver.quit()



sps = SpsFunnelTest()
sps.Sps_Pass_Test()


