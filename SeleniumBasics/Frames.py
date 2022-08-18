import time

import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class Frames():
    global driver

    def Launch_Browser(self):
        options = webdriver.ChromeOptions()
        prefs = {
            "download.default_directory": "C:\\Users\\sathishkumar\\PycharmProjects\\AutomationPythonWeekdayAug\\Downloads\\"}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        #self.driver.get("https://leafground.com/grid.xhtml")
        self.driver.get("https://leafground.com/frame.xhtml")
        #self.driver.get("https://www.ebay.com/")
        #self.driver.get("https://leafground.com/drag.xhtml")
        #self.driver.maximize_window()

    def frameconcepts(self):
        iframecount=self.driver.find_elements(by=By.TAG_NAME, value="iframe")
        totallenofiframe=len(iframecount)
        for eachvalue in range (0,totallenofiframe+1):
            self.driver.switch_to.frame(eachvalue)
            elementcount=self.driver.find_elements(by=By.ID,value="Click")
            print(len(elementcount))
            if len(elementcount) > 0:
                self.driver.find_element(by=By.ID,value="Click").click()
                time.sleep(1)
                print(self.driver.find_element(by=By.ID,value="Click").text)
                self.driver.switch_to.default_content()
                break
            self.driver.switch_to.default_content()

    def frameinsideofanotherframe(self):
        iframecount=self.driver.find_elements(by=By.TAG_NAME, value="iframe")
        totallenofiframe=len(iframecount)
        for eachvalue in range (0,totallenofiframe+1):
            self.driver.switch_to.frame(eachvalue)
            iframecountinside = self.driver.find_elements(by=By.TAG_NAME, value="iframe")
            totallenofiframeinsside = len(iframecountinside)
            if totallenofiframeinsside>0:
                self.driver.switch_to.frame("frame2")
                elementcount=self.driver.find_elements(by=By.ID,value="Click")
                print(len(elementcount))
                if len(elementcount) > 0:
                    self.driver.find_element(by=By.ID,value="Click").click()
                    time.sleep(1)
                    print(self.driver.find_element(by=By.ID,value="Click").text)
                    self.driver.switch_to.default_content()
                    break
                self.driver.switch_to.default_content()
            self.driver.switch_to.default_content()

obj=Frames()
obj.Launch_Browser()
obj.frameinsideofanotherframe()