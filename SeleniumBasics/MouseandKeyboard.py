import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class mouseactions():
    global driver

    def Launch_Browser(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://www.facebook.com/")
        #self.driver.get("https://www.ebay.com/")
        #self.driver.get("https://leafground.com/drag.xhtml")
        self.driver.maximize_window()

    def mouseacti(self):
        mouseactionsineabay=ActionChains(self.driver)
        mouseactionsineabay.move_to_element(self.driver.find_element(by=By.XPATH,value="(//a[text()='Electronics'])[2]")).perform()
        mouseactionsineabay.move_to_element(self.driver.find_element(by=By.XPATH,value="//a[text()='Computers and tablets']")).click().perform()

    def draganddrop(self):
        mouseactionsineabay = ActionChains(self.driver)
        mouseactionsineabay.move_to_element(self.driver.find_element(by=By.ID,value="form:drag_content"))\
            .drag_and_drop(self.driver.find_element(by=By.ID,value="form:drag_content"),
                           self.driver.find_element(By.ID,value="form:drop_header")).perform()

    def draganddropwithtable(self):
        mouseactionsineabay = ActionChains(self.driver)
        mouseactionsineabay.move_to_element(self.driver.find_element(by=By.XPATH,value="(//tr[@data-ri='0'])[2]")).click_and_hold().move_to_element(self.driver.find_element(By.XPATH,value="//tbody[@id='form:j_idt111_data']//tr[3]")).release().perform()
        time.sleep(2)
        print(self.driver.find_element(by=By.XPATH,value="//*[@class='ui-growl-message']//span").text)

    def fbmouseact(self):
        mouseactionsineabay = ActionChains(self.driver)
        mouseactionsineabay.move_to_element(self.driver.find_element(by=By.ID,value="email")).send_keys("sathishkumar").double_click().context_click().perform()

    def keyboarusingpyautogui(self):
        #pyautogui.press("down")
        #pyautogui.press("down")
        pyautogui.keyDown("down")
        pyautogui.keyUp("down")
        pyautogui.keyDown("down")
        pyautogui.keyUp("down")


        #pyautogui.press(['down', 'down','down'])
        #pyautogui.press("down")
        #time.sleep(2)
        pyautogui.press("enter")
        pyautogui.press("tab")
        pyautogui.hotkey('ctrl', 'v')



obj=mouseactions()
obj.Launch_Browser()
obj.fbmouseact()
obj.keyboarusingpyautogui()