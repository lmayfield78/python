from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.smtp import SendMessage
import time
from bs4 import BeautifulSoup
import requests
from shops.seniorityhealth.urls import SeniorityHealth_urls
from urls.all import All_urls
import urllib3
import re
import linkGrabber

# https://stackoverflow.com/questions/18733023/getting-attributes-value-using-beautifulsoup  #YAY!!

def imgs_status_Check(url):

    '''
    This function will search through all URLS and detect if any of the images return a 404 status.
    :param url:
    :return:
    '''

    #_url_ = "https://sixpackshortcuts.com/desktop/sps/main/index/index-ub-lawrence-is-bad"
    #url2 = "https://shop.sixpackabs.com/products/test-reload"
    url3 = "https://shop.sixpackabs.com/products/lawrence-test-of-organifi-green-juice"

     # ==========    This finds everything .img  ==========

    # Launch Site
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(2)

    source = driver.page_source
    soup = BeautifulSoup(source, "html.parser")
    email = SendMessage()

    # find all the src links
    links = soup.find_all('img', {"src": True})

    for i in links:
        if "http" in i['src']:
            print(i['src'])

            result = requests.get(i['src'])
            print(result)

            error = "At " + url + "  \n" + str(i) + " returns =====> " + str(result)

            #send email if 404.
            code = result.status_code  # print this to view the int code.

            if code == 404:
                email.sendEmail(error)

    driver.quit()

imgs_status_Check()
