import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
class calender():

    global driver

    def Launch_Browser(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://www.makemytrip.com/")
        # self.driver.get("https://www.ebay.com/")
        # self.driver.get("https://leafground.com/drag.xhtml")
        self.driver.maximize_window()

    def dateselection(self,actualdate):
        rowval="//*[@class='DayPicker-Months']//div[@class='DayPicker-Month'][1]//div[@class='DayPicker-Body']//div[@class='DayPicker-Week']["
        colval="]//div[contains(@class,'DayPicker-Day')]["
        self.driver.find_element(by=By.CLASS_NAME,value="langCardClose").click()
        identified="notdone"
        self.driver.find_element(by=By.XPATH,value="//*[@for='departure']").click()
        time.sleep(2)
        totalrows=self.driver.find_elements(by=By.XPATH,value="//*[@class='DayPicker-Months']//div[@class='DayPicker-Month'][1]//div[@class='DayPicker-Body']//div[@class='DayPicker-Week']")
        print(len(totalrows))
        for eachrow in range(1,len(totalrows)+1):
            allcolmn=self.driver.find_elements(by=By.XPATH,
                                      value=rowval+str(eachrow)+"]//div[contains(@class,'DayPicker-Day')]")

            for eachcolumn in range(1, len(allcolmn) + 1):
                classvaraiblevalue=self.driver.find_element(by=By.XPATH,
                                          value=rowval+ str(
                                              eachrow) + colval+str(eachcolumn)+"]").get_attribute("class")
                print(classvaraiblevalue)
                if classvaraiblevalue.__contains__('disabled'):
                    pass
                else:
                    datevalue = self.driver.find_element(by=By.XPATH,
                                                                  value=rowval+ str(
                                                                      eachrow) + colval + str(
                                                                      eachcolumn) + "]//p").text
                    print(datevalue)
                    if datevalue == actualdate:
                        print("got in to if condition")
                        self.driver.find_element(by=By.XPATH,
                                                 value="//*[@class='DayPicker-Months']//div[@class='DayPicker-Month'][1]//div[@class='DayPicker-Body']//div[@class='DayPicker-Week'][" + str(
                                                     eachrow) + "]//div[contains(@class,'DayPicker-Day')][" + str(
                                                     eachcolumn) + "]").click()
                        identified="done"
                        break
            if identified=="done":
                break

obj=calender()
obj.Launch_Browser()
obj.dateselection("30")

