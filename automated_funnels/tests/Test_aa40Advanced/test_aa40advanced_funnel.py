from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.index.aa40Advanced_index import aa40Advanced
from pages.step2.aa40Advanced_Step2 import Absafter40Advanced_Step2
from pages.cart.aa40Advanced_cart import aa40Advanced_cart
from pages.upsells.testReload_Upsell import TestReloadUpsell
from pages.upsells.sixpacksleep_Upsell import SixpackSleepUpsell
from pages.upsells.leptinshred_upsell import LeptinShredUpsell


class Test_aa40Advanced_Funnel():


    def Test_aa40Advanced_Pass(self):

        try:
            url = "https://sixpackshortcuts.com/desktop/aa40a/main/index/index"

            driver = webdriver.Firefox()
            driver.get(url)
            #driver.maximize_window()
            time.sleep(1)

            #index
            aa_index = aa40Advanced(driver)
            aa_index.qualifyClick()

            #step 2
            aa40_step2 = Absafter40Advanced_Step2(driver)
            aa40_step2.normalSurvey()

            #cart
            cart = aa40Advanced_cart(driver)
            cart.aa40Advanced_cart_normal()

            #Upsell_testReload
            upsell1 = TestReloadUpsell(driver)
            upsell1.testRealoadPass_aa40a()

            #Upsell Sleep
            upsell2 = SixpackSleepUpsell(driver)
            upsell2.sixpacksleep_Pass()

            #Upsell Leptin Shred
            #upsell3 = LeptinShredUpsell(driver)
            #upsell3.leptinShred_pass_aa40a()

            #Complete
            time.sleep(3)
            print("You have reached the complete page")

        except Exception as e:
            print('AA40A Funnel Verification Pass is a Fail', format(e))
        finally:
            print("aa40a pass COMPLETE")
            driver.quit()








#test = Test_aa40Advanced_Funnel()
#test.Test_aa40Advanced_Pass()