import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
class webtable():

    global driver

    def Launch_Browser(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://leafground.com/table.xhtml")
        # self.driver.get("https://www.ebay.com/")
        # self.driver.get("https://leafground.com/drag.xhtml")
        self.driver.maximize_window()

    def webtablevalidation(self,SearchCountry,QualifiedStatus):
        xpathvariable="//div[@class='ui-datatable-scrollable-body']//table//tbody//tr"
        Pagenumber=self.driver.find_elements(by=By.XPATH,value="//*[@class='ui-paginator-pages']//a")
        TotalPage=len(Pagenumber)
        for eachvalue1 in range(1, TotalPage + 1):
            if eachvalue1>1:
                self.driver.find_element(by=By.XPATH, value="//*[@class='ui-paginator-pages']//a["+str(eachvalue1)+"]").click()
                time.sleep(1)
            #EachRow=self.driver.find_elements(by=By.XPATH,value="//div[@class='ui-datatable-scrollable-body']//table//tbody//tr")
            EachRow=self.driver.find_elements(by=By.XPATH,value=xpathvariable)
            TablerowSize=len(EachRow)

            for eachvalue in range(1,TablerowSize+1):
                #time.sleep(2)
                CountryName=self.driver.find_element(by=By.XPATH,
                                          value=xpathvariable+"["+ str(eachvalue) +"]//td[2]//span[3]").text
                if CountryName == SearchCountry:
                   #time.sleep(2)
                   Status= self.driver.find_element(by=By.XPATH,
                                             value=xpathvariable+"[" + str(
                                                 eachvalue) + "]//td[5]//span[2]").text
                   if Status==QualifiedStatus:
                       print(QualifiedStatus)
                       #time.sleep(2)
                       Name = self.driver.find_element(by=By.XPATH,
                                                        value=xpathvariable+"[" + str(
                                                            eachvalue) + "]//td[1]").text
                       Representative = self.driver.find_element(by=By.XPATH,
                                                       value="//div[@class='ui-datatable-scrollable-body']//table//tbody//tr[" + str(
                                                           eachvalue) + "]//td[3]//span[2]").text
                       JoinDate = self.driver.find_element(by=By.XPATH,
                                                                 value="//div[@class='ui-datatable-scrollable-body']//table//tbody//tr[" + str(
                                                                     eachvalue) + "]//td[4]").text

                       print(Name + " "+CountryName+" "+Representative+ " "+JoinDate+" "+Status)

obj= webtable()
obj.Launch_Browser()
obj.webtablevalidation("Germany","RENEWAL")

