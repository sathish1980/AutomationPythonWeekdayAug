import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class createAccount():

    def createcccountfunctionality(self, web=None):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        driver.get("https://www.facebook.com/")
        driver.maximize_window()
        driver.find_element(by=By.XPATH ,value="//*[@data-testid='open-registration-form-button']").click()
        driver.implicitly_wait(20)
        driver.find_element(by=By.NAME,value="firstname").send_keys("sathish")
        driver.find_element(by=By.NAME, value="lastname").send_keys("kumar")
        driver.find_element(by=By.NAME, value="reg_email__").send_keys("kumar.sathish189@gmail.com")
        #time.sleep(2)
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.NAME,'reg_email_confirmation__')))
        driver.find_element(by=By.NAME, value="reg_email_confirmation__").send_keys("kumar.sathish189@gmail.com")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'reg_passwd__')))
        driver.find_element(by=By.NAME, value="reg_passwd__").send_keys("password")
        driver.find_element(by=By.XPATH, value="//*[@value='2' and contains(@id,'u_')]").click()
        time.sleep(2)


obj=createAccount()
obj.createcccountfunctionality()