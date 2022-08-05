import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def launch(web=None):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    #username = driver.find_element(by=By.NAME, value="email") #webelement
    #username = driver.find_element(by=By.CSS_SELECTOR, value="input.inputtext _55r1 _6luy[type=text]")
    #username = driver.find_element(by=By.CSS_SELECTOR, value="input.inputtext _55r1 _6luy[type=text]")  # webelement
    username = driver.find_element(by=By.XPATH, value="//input[@data-testid='royal_email']")  # webelement
    username.send_keys("kumar.sathish189@gmail.com") #action
    time.sleep(2)
    username.clear()
    time.sleep(2)
    driver.find_element(by=By.XPATH ,value="//*[contains(@class,'_55r1') and @name='pass' or @id='pass']").send_keys("password")
    driver.find_element(b=By.XPATH,value="(//*[text()='Log In'])[1]").click()
    driver.find_element(by=By.LINK_TEXT, value="Forgotten password?").click()
    time.sleep(2)
    driver.find_element(by=By.PARTIAL_LINK_TEXT, value="gotten").click()
    time.sleep(2)

    #driver.minimize_window()
""" driver.set_window_size(300,700)
    driver.forward()
    driver.back()
    driver.refresh()
    driver.quit()"""


launch()