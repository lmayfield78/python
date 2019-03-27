from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
#import requests



class Text():
    '''
    This function is intended to scrape urls for certain keywords that would
    be flagged by crawlers.
    '''



    def __init__(self,driver):
        self.driver = driver

    def findText_standalone(self):


        url = "https://sixpackshortcuts.com/desktop/tmax/main/index/index"
        url2 = "http://sixpackshortcuts.com/desktop/absafter40"

        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url2)
        time.sleep(2)

        #r = requests.get(url)
        #data = r.text
        source = driver.page_source
    
        soup = BeautifulSoup(source, "html.parser")
        test = soup.get_text().lower()
        p = soup.find_all('<body>')

        alllist = [
            "testosterone",
            "HGH",
            "Reverse Aging",
            "lose pounds",
            "pounds",
            "norephedrine",

            ]

        for word in alllist:
            if word in test:
                print(word + " was found in source")

        driver.quit()


    def bannedWords(self,driver):
        '''
        This function will search the current page for banned words.
        :return:
        '''

        source = self.driver.page_source

        soup = BeautifulSoup(source, "html.parser")
        test = soup.get_text().lower()
        p = soup.find_all('<body>')

        alllist = [
            "testosterone",
            "HGH",
            "Reverse Aging",
            "lose pounds",
            "pounds",
            "norephedrine",
        ]

        for word in alllist:
            if word in test:
                print(word + " was found in source in the body")

#go = Text()
#go.findText_standalone()

