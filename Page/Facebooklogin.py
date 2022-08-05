from datetime import time

from selenium.webdriver.common.by import By


class Facebookloginpage():

    def __init__(self, driver):
        self.driver = driver

    def Enter_the_username(self,usrname):
        username = self.driver.find_element(by=By.XPATH, value="//input[@data-testid='royal_email']")  # webelement
        username.send_keys(usrname)  # action

    def Enter_password(self,password):
        self.driver.find_element(by=By.XPATH,
                            value="//*[contains(@class,'_55r1') and @name='pass' or @id='pass']").send_keys(password)

    def Click_loginbutton(self):
        self.driver.find_element(by=By.XPATH, value="(//*[text()='Log In'])[1]").click()

    def creataccountbutton(self):
        self.driver.find_element(by=By.XPATH, value="//*[@data-testid='open-registration-form-button']").click()