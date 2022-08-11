import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
class scroll():

    global driver

    def Launch_Browser(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://leafground.com/dashboard.xhtml")
        #self.driver.get("https://www.ebay.com/")
        #self.driver.get("https://leafground.com/drag.xhtml")
        self.driver.maximize_window()

    def scrollvalidation(self):
        #scroll down Vertically
        self.driver.execute_script("window.scrollTo(0, 700)", "")
        time.sleep(1)
        obj.screenshot("Verticalldown")
        # scroll up Vertically
        self.driver.execute_script("window.scrollTo(0, -400)", "")
        time.sleep(1)
        obj.screenshot("Verticallup")
        # scroll right horizontaly
        self.driver.execute_script("window.scrollTo(300, 0)", "")
        time.sleep(1)
        # scroll left horizontaly
        self.driver.execute_script("window.scrollTo(-300, 0)", "")
        time.sleep(1)
        # scroll bottom
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        obj.screenshot("Towardsdown")
        # scroll up
        self.driver.execute_script("window.scrollTo(0, -0);")
        time.sleep(1)
        obj.screenshot("Towardsup")
        #scroll to be element
        element = self.driver.find_element(by=By.XPATH,value="//*[text()='Previous']")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        obj.screenshot("Towardstotherespectiveelement")

    def screenshot(self, filename):
        self.driver.save_screenshot(
                "C:\\Users\\sathishkumar\\PycharmProjects\\AutomationPythonWeekdayAug\\Screenshot\\" + filename + ".png")

obj=scroll()
obj.Launch_Browser()
obj.scrollvalidation()