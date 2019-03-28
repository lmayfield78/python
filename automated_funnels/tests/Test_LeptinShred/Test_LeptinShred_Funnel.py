from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.index.leptinSherd_index import LeptinShred_Index
from pages.step2.leptinshred_step2 import leptinshred_step2
from pages.cart.leptinshred_cart import leptinshred_cart
from pages.upsells.leptinshred_upsell import LeptinShredUpsell
from pages.upsells.insanehomefatloss_upsell import insanehomefatloss
from pages.upsells.sixpackshortcuts_upsell import sixpackshortcuts_upsell

class LeptinShredFunnel:

    def leptinShred_funnel_normal_pass(self):

        try:

            url = "https://sixpackshortcuts.com/desktop/leptin/main/index/index"

            driver = webdriver.Firefox()
            driver.get(url)

            #index
            index = LeptinShred_Index(driver)
            index.leptin_index_clickhere()

            #step 2
            step2 = leptinshred_step2(driver)
            step2.leptin_step2_normal()

            #Cart
            cart = leptinshred_cart(driver)
            cart.leptinShred_normal_cart()

            #Leptin
            leptin = LeptinShredUpsell(driver)
            leptin.leptinShred_pass_aa40a()

            #IHFL
            ihfl = insanehomefatloss(driver)
            ihfl.insanehomefatloss_upsell()

            #Upsell 3
            sps = sixpackshortcuts_upsell(driver)
            sps.sixpackshortcuts_normal_upsell()

            #complete
            print("Leptin Shred pass completed")

        except Exception as e:
            print('Leptin Funnel Verification Pass is a Fail', format(e))
        finally:
            driver.quit()
            print("Leptin Shred Funnel Finished")





#go = LeptinShredFunnel()
#go.leptinShred_funnel_normal_pass()