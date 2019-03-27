from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup


class AltImg():

    """
    This function searches through specific URLS and searches for specific pixel images.
    """

    _url_ = "http://sixpackshortcuts.com/desktop/absafter40/main/faqs"




    def locateImgs(self):

        # Launch Site
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(self._url_)
        driver.implicitly_wait(10)
        time.sleep(2)

        # ==========    Beautiful Soup   ==========

        source = driver.page_source
        soup = BeautifulSoup(source, "html.parser")
        imgs = soup.find_all('img')
        img_total = len(imgs)
        total = (str(img_total))
        print("==============================================================")
        print("The total amount of Images = " + total + "  From Beautiful Soup")
        print("==============================================================")

        lowcount = soup.findAll('img')

        for count in lowcount:
            print(count)

        print("*****************************************************************")



        print("==============================================================")

        new_imgs = soup.find_all('img')
        new_img_len = len(new_imgs)
        new_total = (str(new_img_len))

        pixels1 = soup.find_all('img', width='1', height='1')

        for pic in pixels1:
            new_imgs.remove(pic)

        pixels2 = soup.find_all('img', width='0', height='0')

        for pic in pixels2:
            new_imgs.remove(pic)

        #print(pic['width'], pic['height'])

        current = new_imgs
        current_len = len(current)
        new_current = (str(current_len))
        filtered_number = new_current
        print("==============================================================")
        print("The total amount of NON-Pixel Images = " + filtered_number + "  From Beautiful Soup")
        print("==============================================================")

        for u in new_imgs:
            print(u)

        print("==============================================================")



        driver.quit()



altRun = AltImg()
altRun.locateImgs()


