import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class Draganddrop():
    global driver

    def Launch_Browser(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://leafground.com/drag.xhtml")
        #self.driver.get("https://www.ebay.com/")
        #self.driver.get("https://leafground.com/drag.xhtml")
        self.driver.maximize_window()
    def draganddroptotheelemt(self,dropvalue):
        time.sleep(1)
        dragleft=self.driver.find_element(by=By.XPATH,value="//*[@id='form:j_idt125']//span[1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", dragleft)
        droptoelem=self.driver.find_element(by=By.XPATH,value="//*[@id='form:j_idt125' ]//span[@style['left: +"+str(dropvalue)+"%;']][1]")
        mc=ActionChains(self.driver)
        mc.move_to_element(dragleft).drag_and_drop(dragleft,droptoelem).perform()

obj=Draganddrop()
obj.Launch_Browser()
obj.draganddroptotheelemt(45)
