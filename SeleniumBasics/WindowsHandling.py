import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class Windowshandling():
    global driver

    def Launch_Browser(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://leafground.com/window.xhtml")
        #self.driver.get("https://www.ebay.com/")
        #self.driver.get("https://leafground.com/drag.xhtml")
        self.driver.maximize_window()

    def windowshandling(self):

        parentwindow=self.driver.current_window_handle
        self.driver.find_element(by=By.ID,value="j_idt88:new").click()
        Allwindows=self.driver.window_handles
        for child in Allwindows:

            if(child!=parentwindow):
                self.driver.switch_to.window(child) # to switch over in to the each child window
                Title=self.driver.title
                print(Title)
                self.driver.find_element(By.ID,value="email").send_keys("kumar.sathish189@gmail.com")
                self.driver.find_element(By.ID, value="message").send_keys("This is for testing purpose")
                time.sleep(2)
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                self.driver.quit()

    def windowshandlingwithvalidation(self):

        parentwindow=self.driver.current_window_handle
        self.driver.find_element(by=By.ID,value="j_idt88:j_idt91").click()
        Allwindows=self.driver.window_handles
        for child in Allwindows:

            if(child!=parentwindow):
                self.driver.switch_to.window(child) # to switch over in to the each child window
                self.driver.maximize_window()
                Title=self.driver.title
                print(Title)
                Elementavailable=self.driver.find_elements(By.ID,value="email")
                Elementavailablesize=len(Elementavailable)
                if Elementavailablesize>0:
                    self.driver.find_element(By.ID,value="email").send_keys("kumar.sathish189@gmail.com")
                    self.driver.find_element(By.ID, value="message").send_keys("This is for testing purpose")
                    time.sleep(2)
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)

                    self.driver.close()
                    break
        self.driver.switch_to.window(parentwindow)
        self.driver.find_element(by=By.ID, value="j_idt88:new").click()
obj=Windowshandling()
obj.Launch_Browser()
obj.windowshandlingwithvalidation()
