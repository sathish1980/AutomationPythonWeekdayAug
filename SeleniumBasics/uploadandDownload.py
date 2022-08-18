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

class UploadandDownload():
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
        self.driver.get("https://cleartax.in/paytax/UploadForm16")
        #self.driver.get("https://www.ebay.com/")
        #self.driver.get("https://leafground.com/drag.xhtml")
        #self.driver.maximize_window()
    def download(self):
        self.driver.find_element(by=By.ID,value="form:j_idt93").click()

    def upload(self):
        self.driver.find_element(by=By.XPATH,value="(//*[contains(@class,'input-file-upload')])[1]").click()
        pyperclip.copy("C:\\Users\\sathishkumar\\PycharmProjects\\AutomationPythonWeekdayAug\\Downloads\\products.pdf")
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(2)
        filenameafterupload= self.driver.find_element(by=By.XPATH,value="(//*[contains(@class,'input-file-upload')])[2]").text
        print(filenameafterupload)
        if filenameafterupload == "products.pdf":
            print("uploaded sucessfully")


obj=UploadandDownload()
obj.Launch_Browser()
obj.upload()