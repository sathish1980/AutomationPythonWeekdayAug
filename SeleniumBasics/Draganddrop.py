import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def Range(self):
        self.driver.execute_script("document.querySelector('.ui-state-default').style.left = '0%'")
        #self.driver.execute_script("document.querySelector('.ui-state-default').style.left = '100%'")
        mc = ActionChains(self.driver)
        frmovalue=self.driver.find_element(by=By.XPATH,value="//*[contains(@id,'form:j_idt125')]//div[1]")
        """mc.move_to_element(self.driver.find_element(by=By.XPATH,
                                                    value="//*[contains(@id,'form:j_idt125')]//span[1]")).drag_and_drop(
            self.driver.find_element(by=By.XPATH,
                                     value="//*[contains(@id,'form:j_idt125')]//span[1]"),self.driver.find_element(by=By.XPATH,
                                                    value="//*[contains(@id,'form:j_idt125')]//span[2]")
        ).perform()"""

        mc.move_to_element(self.driver.find_element(by=By.XPATH,value="//*[contains(@id,'form:j_idt125')]//span[1]")).drag_and_drop_by_offset(frmovalue, 0,1).perform()

    def Progressbar(self):
        self.driver.find_element(by=By.ID, value="form:j_idt119").click()
        WebDriverWait(self.driver,60).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"ui-progressbar-label"),"100%"))
        print(self.driver.find_element(by=By.XPATH, value="//*[@class='ui-growl-message']//span").text)


obj=Draganddrop()
obj.Launch_Browser()
obj.draganddroptotheelemt(45)
obj.Range()
obj.Progressbar()
