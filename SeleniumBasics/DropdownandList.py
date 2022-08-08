import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class droddownandlist():
    global driver

    def Launch_Browser(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        #self.driver.get("https://www.facebook.com/")
        self.driver.get("https://leafground.com/select.xhtml")
        self.driver.maximize_window()

    def dropdown(self):
        self.driver.find_element(by=By.XPATH, value="//*[@data-testid='open-registration-form-button']").click()
        self.driver.implicitly_wait(20)
        datadropdown=Select(self.driver.find_element(by=By.ID, value="day"))
        print(datadropdown.is_multiple)
        datadropdown.select_by_index(10)
        datadropdown.select_by_value("12")
        datadropdown.select_by_visible_text("25")
        monthdropdown = Select(self.driver.find_element(by=By.ID, value="month"))
        monthdropdown.select_by_value("11")
        yeardropdown = Select(self.driver.find_element(by=By.ID, value="year"))
        yeardropdown.select_by_visible_text("1990")


    def leafgroundSelect(self):
        uiautomatniotool=Select(self.driver.find_element(by=By.CLASS_NAME, value="ui-selectonemenu"))
        uiautomatniotool.select_by_index(2)

    def listvalue(self,actualcountryvalue):
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value="(//*[contains(@class,'ui-selectonemenu-trigger')])[1]").click()
        time.sleep(2)
        Allcountries= self.driver.find_elements(by=By.XPATH,value="//*[contains(@id,'country')]//li")
        size=len(Allcountries)
        print(size)
        for eachvalue in range(1,size+1):
            print(eachvalue)
            country=self.driver.find_element(by=By.XPATH, value="//*[contains(@id,'country_items')]//li["+ str(eachvalue) +"]").text
            print(country)
            if country==actualcountryvalue:
                self.driver.find_element(by=By.XPATH,
                                        value="//ul[contains(@id,'country_items')]//li[" + str(eachvalue) + "]").click()
                break

    def CityList(self,actualcityvalue):
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value="(//*[contains(@class,'ui-selectonemenu-trigger')])[2]").click()
        time.sleep(1)
        Allcountries= self.driver.find_elements(by=By.XPATH,value="//*[contains(@id,'city')]//li")
        size=len(Allcountries)
        print(size)
        for eachvalue in range(1,size+1):
            print(eachvalue)
            City=self.driver.find_element(by=By.XPATH, value="//*[contains(@id,'city')]//li["+ str(eachvalue) +"]").text
            print(City)
            if City==actualcityvalue:
                self.driver.find_element(by=By.XPATH,
                                        value="//*[contains(@id,'city')]//li[" + str(eachvalue) + "]").click()
                break

    def CourseList(self,actualcoursevalue):
        for eachvalueinlist in actualcoursevalue:
            time.sleep(1)
            self.driver.find_element(by=By.XPATH,value="//*[contains(@class,'ui-autocomplete-dropdown')]").click()
            time.sleep(1)
            Allcountries= self.driver.find_elements(by=By.XPATH,value="//*[contains(@id,'j_idt87:auto-complete_panel')]//li")
            size=len(Allcountries)
            print(size)
            for eachvalue in range(1,size+1):
                print(eachvalue)
                course=self.driver.find_element(by=By.XPATH, value="//*[contains(@id,'j_idt87:auto-complete_panel')]//li["+ str(eachvalue) +"]").text
                print(course)
                if course==eachvalueinlist:
                    self.driver.find_element(by=By.XPATH,
                                            value="//*[contains(@id,'j_idt87:auto-complete_panel')]//li[" + str(eachvalue) + "]").click()
                    break

dp=droddownandlist()
dp.Launch_Browser()
dp.listvalue("India")
dp.CityList("Chennai")
dp.CourseList(["JMeter","AWS"])
