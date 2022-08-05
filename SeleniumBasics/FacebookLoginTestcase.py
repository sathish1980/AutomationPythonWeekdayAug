
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Page.Facebooklogin import Facebookloginpage


class Facebooklogintestcase():
    global driver

    def Launch_Browser(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()

    def ValidLoginintoFacebook(self, web=None):
        FBloginPage=Facebookloginpage(self.driver)
        FBloginPage.Enter_the_username("kumar.sathish189@gmail.com")
        FBloginPage.Enter_password("password")
        FBloginPage.Click_loginbutton()

    def InValidLoginintoFacebook(self, web=None):
        FBloginPage=Facebookloginpage(self.driver)
        FBloginPage.Enter_the_username("kumar.sathish189@gmail.com")
        FBloginPage.Enter_password("password")
        FBloginPage.Click_loginbutton()

obj1=Facebooklogintestcase()
obj1.Launch_Browser()
obj1.ValidLoginintoFacebook()