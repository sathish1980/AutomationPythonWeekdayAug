from datetime import time

from selenium.webdriver.common.by import By


class Facebooklogoutpage():

    def __init__(self, driver):
        self.driver = driver

    def Login_username(self):
        return self.driver.find_element(by=By.XPATH,
                                 value="((//*[@role='navigation' ]//*[ @data-visualcompletion='ignore-dynamic'])[4]//span)[2]").text

    def Click_Logout_Dropdown(self):
        self.driver.find_element(by=By.XPATH,value="//*[local-name()='svg' and @aria-label='Your profile']").click()

    def Click_Logout(self):
        self.driver.find_element(by=By.XPATH, value="//*[text()='Log Out']").click()