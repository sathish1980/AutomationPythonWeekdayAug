import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Page.FacebookLogoutpage import Facebooklogoutpage
from Page.Facebooklogin import Facebookloginpage
from TestData.FBLoginData import FBLogindata
from Utils.ExcelReadData import ExcelReadData


@pytest.mark.usefixtures("browserlaunch")
class Test_Facebook():

    def test_UrlLaunch(self,baseUrl):
        self.driver.get(baseUrl)
        print("URL launched sucessfully")

    def Test_LoginintoFacebook(self,FbTestData):
        #WebDriverWait(self.driver, 60).until(EC.presence_of_all_elements_located(by=By.ID, value="email"))
        time.sleep(2)
        print(FbTestData)
        self.driver.find_element(by=By.ID,value="email").send_keys(FbTestData[1])
        self.driver.find_element(by=By.ID, value="pass").send_keys(FbTestData["password"+1])
        self.driver.find_element(by=By.XPATH, value="//button[text()='Log In']").click()
        print("Login sucessfull")
        #WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(by=By.XPATH, value="//*[local-name()='svg' and @aria-label='Your profile']"))
        time.sleep(4)
        name = self.driver.find_element(by=By.XPATH,
                                           value="((//*[@role='navigation' ]//*[ @data-visualcompletion='ignore-dynamic'])[4]//span)[2]").text
        print(name)
        self.driver.find_element(by=By.XPATH, value="//*[local-name()='svg' and @aria-label='Your profile']").click()
        #WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(by=By.XPATH, value="//*[text()='Log Out']"))
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="//*[text()='Log Out']").click()

    def est_LoginintoFacebookwithExcel(self,FbTestDatawithExcel):
        #WebDriverWait(self.driver, 60).until(EC.presence_of_all_elements_located(by=By.ID, value="email"))
        time.sleep(2)
        print(len(ExcelReadData.retrundicvalue()))
        print(FbTestDatawithExcel["username"+str(2)])
        totarows=len(ExcelReadData.retrundicvalue())/5
        for eachvalue in  range(1,int(totarows)+1):
            self.driver.find_element(by=By.ID,value="email").send_keys(FbTestDatawithExcel["username"+str(eachvalue)])
            self.driver.find_element(by=By.ID, value="pass").send_keys(FbTestDatawithExcel["password"+str(eachvalue)])
            self.driver.find_element(by=By.XPATH, value="//button[text()='Log In']").click()
            print("Login sucessfull")
            #WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(by=By.XPATH, value="//*[local-name()='svg' and @aria-label='Your profile']"))
            time.sleep(4)
            name = self.driver.find_element(by=By.XPATH,
                                               value="((//*[@role='navigation' ]//*[ @data-visualcompletion='ignore-dynamic'])[4]//span)[2]").text
            print(name)
            self.driver.find_element(by=By.XPATH, value="//*[local-name()='svg' and @aria-label='Your profile']").click()
            #WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(by=By.XPATH, value="//*[text()='Log Out']"))
            time.sleep(2)
            self.driver.find_element(by=By.XPATH, value="//*[text()='Log Out']").click()

    def test_LoginWithPOM(self,FbTestDatawithExcel):
        FBLGPage=Facebookloginpage(self.driver)
        FBLGoutPage = Facebooklogoutpage(self.driver)
        time.sleep(2)
        print(len(ExcelReadData.retrundicvalue()))
        print(FbTestDatawithExcel["username" + str(2)])
        totarows = len(ExcelReadData.retrundicvalue()) / 5
        for eachvalue in range(1, int(totarows) + 1):
            FBLGPage.Enter_the_username(FbTestDatawithExcel["username" + str(eachvalue)])
            FBLGPage.Enter_password(FbTestDatawithExcel["password" + str(eachvalue)])
            FBLGPage.Click_loginbutton()
            time.sleep(4)
            FBLGoutPage.Login_username()
            FBLGoutPage.Click_Logout_Dropdown()
            time.sleep(2)
            FBLGoutPage.Click_Logout()
            print("Login sucessfull")


