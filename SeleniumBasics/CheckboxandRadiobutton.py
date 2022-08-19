import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
class checboxandradiobutton():

    global driver

    def Launch_Browser(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://leafground.com/checkbox.xhtml")
        # self.driver.get("https://www.ebay.com/")
        # self.driver.get("https://leafground.com/drag.xhtml")
        self.driver.maximize_window()
    def checkboxvalidation(self,actualcoursname):

        self.driver.find_element(by=By.XPATH,value="//*[@id='j_idt87:j_idt89']//div[2]").click()
        self.driver.find_element(by=By.XPATH, value="//*[@id='j_idt87:j_idt91']//div[2]").click()
        totalvalues=self.driver.find_elements(by=By.XPATH,value="//*[@id='j_idt87:basic']//tbody//tr//td")
        size=len(totalvalues)
        for eachvalue in range(1,size+1):
            coursename=self.driver.find_element(by=By.XPATH, value="//*[@id='j_idt87:basic']//tbody//tr//td["+str(eachvalue)+"]//label").text
            if coursename in actualcoursname:
                self.driver.find_element(by=By.XPATH, value="//*[@id='j_idt87:basic']//tbody//tr//td[" + str(
                    eachvalue) + "]//div[2]").click()

        print(self.driver.find_element(by=By.XPATH, value="//*[@id='j_idt87:j_idt102']//div[2]").is_selected())
        #self.driver.find_element(By.XPATH, value="//*[@id='j_idt87:j_idt102']//div[2]").click()

    def togglebutton(self):
        toggleslected=self.driver.find_element(by=By.CLASS_NAME,value="ui-toggleswitch-slider").is_selected()
        if toggleslected == False:
            self.driver.find_element(by=By.CLASS_NAME,value="ui-toggleswitch-slider").click()
            #time.sleep(2)
            print(self.driver.find_element(by=By.XPATH,value="//*[@class='ui-growl-message']//span").text)
            time.sleep(2)
            print(self.driver.find_element(by=By.CLASS_NAME, value="ui-toggleswitch-slider").is_selected())

obj=checboxandradiobutton()
obj.Launch_Browser()
obj.checkboxvalidation(["Python","C-Sharp","Java","Javascript"])
obj.togglebutton()