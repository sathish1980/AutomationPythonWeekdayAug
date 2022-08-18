import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class grid():
    global driver

    def Launch_Browser(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://leafground.com/grid.xhtml")
        #self.driver.get("https://www.ebay.com/")
        #self.driver.get("https://leafground.com/drag.xhtml")
        self.driver.maximize_window()
    def gridcheckbox(self,valuetoselect):
        xpathallvalue="//*[@class='ui-datatable-tablewrapper']//table//tbody//tr"
        identified="NotDone"
        pagination=self.driver.find_elements(by=By.XPATH,value="//*[@id='form:dt-products_paginator_bottom']//span//a")
        pageSize = len(pagination)
        for eachvaluepage in range(1, pageSize + 1):
            allvalue=self.driver.find_elements(by=By.XPATH,value=xpathallvalue)
            listsize=len(allvalue)
            time.sleep(1)
            for eachvalue in range(1,listsize+1):
                ProductName=self.driver.find_element(by=By.XPATH, value=xpathallvalue+"["+str(eachvalue)+"]//td[3]").text
                if ProductName==valuetoselect:
                    self.driver.find_element(by=By.XPATH,
                                              value=xpathallvalue+"[" + str(
                                                  eachvalue)+"]//td[1]").click()
                    print(self.driver.find_element(by=By.XPATH,
                                             value=xpathallvalue+"[" + str(
                                                 eachvalue) + "]//td[5]").text)
                    identified="Done"
                    break
            if identified=="Done":

                self.driver.quit()
                break
            else:
                self.driver.find_element(by=By.XPATH, value="//*[@id='form:dt-products_paginator_bottom']//span//a["+str(eachvaluepage)+"]").click()



obj=grid()
obj.Launch_Browser()
obj.gridcheckbox("Headphones")