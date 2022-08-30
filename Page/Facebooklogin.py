from datetime import time

from selenium.webdriver.common.by import By


class Facebookloginpage():

    def __init__(self, driver):
        self.driver = driver
    username=(By.XPATH, "//input[@data-testid='royal_email']")
    password = (By.XPATH, "//*[contains(@class,'_55r1') and @name='pass' or @id='pass']")
    loginbutton = (By.XPATH, "(//*[text()='Log In'])[1]")
    createaccount = (By.XPATH, "//*[@data-testid='open-registration-form-button']")
    Forgotpassword = (By.LINK_TEXT, "Forgotten password?")

    def Enter_the_username(self,usrnme):
        #username = self.driver.find_element(by=By.XPATH, value="//input[@data-testid='royal_email']")  # webelement
        usrname = self.driver.find_element(*Facebookloginpage.username)  # webelement
        usrname.send_keys(usrnme)  # action

    def Enter_password(self,pwrd):
        #self.driver.find_element(by=By.XPATH,value="//*[contains(@class,'_55r1') and @name='pass' or @id='pass']").send_keys(password)
        self.driver.find_element(*Facebookloginpage.password).send_keys(pwrd)

    def Click_loginbutton(self):
        #self.driver.find_element(by=By.XPATH, value="(//*[text()='Log In'])[1]").click()
        self.driver.find_element(*Facebookloginpage.loginbutton).click()

    def creataccountbutton(self):
        #self.driver.find_element(by=By.XPATH, value="//*[@data-testid='open-registration-form-button']").click()

        self.driver.find_element(*Facebookloginpage.createaccount).click()

    def ForgotPassword(self):
        #self.driver.find_element(by=By.LINK_TEXT, value="Forgotten password?").click()
        self.driver.find_element(*Facebookloginpage.Forgotpassword).click()