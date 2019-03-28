from selenium import webdriver
from pages.index.testReload_index import TestReload_Index
from pages.step2.testReload_step2 import TestReload_Step2
from pages.cart.testReload_cart import TestReload_Cart
from pages.upsells.testReload_Upsell import TestReloadUpsell
from pages.upsells.doneforyoudiet import doneforyoudiet
from pages.upsells.acceleratedabse_upsell import Acceleratedabs

class Test_TestReload():


    def TestReload_Funnel(self):

        try:
            url = 'https://sixpackshortcuts.com/desktop/reload/main/index/index'

            driver = webdriver.Firefox()
            driver.get(url)

            #index
            index = TestReload_Index(driver)
            index.testReload_index_claim()

            #step 2
            step2 = TestReload_Step2(driver)
            step2.testReload_step2_normal()

            #cart
            cart = TestReload_Cart(driver)
            cart.testReload_cartNormal()

            # Upsell 1
            cart = TestReloadUpsell(driver)
            cart.testRealoadPass_aa40a()

            # Upsell 2
            done = doneforyoudiet(driver)
            done.doneforyoudiet_normal()

            # Upsell 3
            abs = Acceleratedabs(driver)
            abs.acceleratedabs_normal()

            print("You have reached the end of the Test Reload Funnel")

        except Exception as e:
            print('Test Reload Funnel Verification Pass is a Fail', format(e))
        finally:
            print("Test Reload pass COMPLETE")
            driver.quit()

testRun = Test_TestReload()
testRun.TestReload_Funnel()