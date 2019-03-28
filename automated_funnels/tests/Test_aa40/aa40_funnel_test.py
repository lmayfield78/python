from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.index.aa40_index import aa40_Index
from pages.step2.step_2 import Step2Page
from pages.cart.cart import Cart
from pages.upsells.aa40a_Upsell import aa40aUpsell
from pages.upsells.testReload_Upsell import TestReloadUpsell
from pages.upsells.leptinshred_upsell import LeptinShredUpsell
from pages.complete.aa40_complete import Complete_aa40
from pages.upsells.leptinshred_upsell import LeptinShredUpsell
import time


class aa40FunnelTest():

    url = "http://sixpackshortcuts.com/desktop/absafter40"
    #  from tools.text_search import Text
    # print("============  aa40_Index Banned words Start ===============")
    # go = Text(self.driver)
    # go.bannedWords(self.driver)
    # print("====== aa40_Index banned words finish  ===============")

    def test_aa40_funnel(self):

        try:
            # == Load Browser and go to site  ==
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get(self.url)
            time.sleep(3)

            #Index Page
            index = aa40_Index(driver)
            index.indexClick()

            #Step 2
            step2 = Step2Page(driver)
            step2.step2Inputs()

            #cart
            cart = Cart(driver)
            cart.cart_pass()

            #aa40a Upsell
            aa40a = aa40aUpsell(driver)
            aa40a.aa40aUpsell_pass()

            #TestReload Upsell
            testo = TestReloadUpsell(driver)
            testo.testRealoadPass()

            #LeptinShred Upsell
            #lep = LeptinShredUpsell(driver)
            #lep.leptinShred_pass_aa40a()

            #Complete Page
            comp = Complete_aa40(driver)
            comp.completePage_verify()

            print("AA40 funnel is complete")

        except Exception as e:
            print('AA40 Funnel Verification Pass is a Fail', format(e))
        finally:
            driver.quit()
            print("Aa40 funnel pass finished")

go = aa40FunnelTest()
go.test_aa40_funnel()
