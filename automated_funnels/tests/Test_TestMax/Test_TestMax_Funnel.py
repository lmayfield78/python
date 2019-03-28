from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.index.test_max import Test_Max_Index
from pages.step2.testMax_Step2 import TestMax_Step2
from pages.cart.tmax_cart import TestMaxCart
from pages.upsells.testReload_Upsell import TestReloadUpsell
from pages.upsells.aa40_Upsell import Aa40_Upsell
from pages.upsells.alphaArmor_Upsell import AlphaArmorUpsell

class Test_TestMax():

    url = 'https://sixpackshortcuts.com/desktop/tmax/main/index/index'

    def Tmax_normal_funnel_pass_test(self):
        try:
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get(self.url)

            tmax = Test_Max_Index(driver)
            tmax.testMax_normal_button()

            tmaxS2 = TestMax_Step2(driver)
            tmaxS2.tmax_normal_pass()

            tmaxCart = TestMaxCart(driver)
            tmaxCart.cartNormalPass()

            tReloadUpsell = TestReloadUpsell(driver)
            tReloadUpsell.tmax_reload()

            aa40Up = Aa40_Upsell(driver)
            aa40Up.aa40Upsell_normal()

            aArmor = AlphaArmorUpsell(driver)
            aArmor.alphaArmor_Pass()

            print('You have reached the Complete Page')

        except Exception as e:
            print('Something went wrong', format(e))
        finally:
            print("Tmax funnel pass is Finished")
            driver.quit()


#go = Test_TestMax()
#go.Tmax_normal_funnel_pass_test()

#self.driver.implicitly_wait()



