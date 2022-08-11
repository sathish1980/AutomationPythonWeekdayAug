import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Alerts():
    global driver

    def Launch_Browser(self, web=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
        self.driver.get("https://leafground.com/radio.xhtml")
        #self.driver.get("https://leafground.com/alert.xhtml")
        self.driver.maximize_window()

    def alerthandling(self):
        self.driver.find_element(by=By.XPATH,value="(//span[text()='Show']//ancestor::button)[1]").click()
        alertobject=self.driver.switch_to.alert
        time.sleep(2)
        print(alertobject.text)
        alertobject.accept()
        sucessful_text=self.driver.find_element(by=By.ID,value="simple_result").text
        print(sucessful_text)

        ####
        self.driver.find_element(by=By.XPATH, value="(//span[text()='Show']//ancestor::button)[2]").click()
        alertobject = self.driver.switch_to.alert
        time.sleep(2)
        print(alertobject.text)
        alertobject.dismiss()
        sucessful_text = self.driver.find_element(by=By.ID, value="result").text
        print(sucessful_text)

        ## sweet Alert
        self.driver.find_element(by=By.XPATH, value="(//span[text()='Show']//ancestor::button)[3]").click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value="//span[text()='Dismiss']//ancestor::button").click()

        ## sweet Alert 2
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value="(//span[text()='Show']//ancestor::button)[4]").click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value="(//span[contains(@class,'ui-icon-closethick')]//parent::a)[2]").click()

        ## prompt Alert
        self.driver.find_element(by=By.XPATH, value="(//span[text()='Show']//ancestor::button)[5]").click()
        time.sleep(2)
        alertobject = self.driver.switch_to.alert
        time.sleep(2)
        alertobject.send_keys("Sathish from Besant")
        alertobject.accept()
        sucessful_text = self.driver.find_element(by=By.ID, value="confirm_result").text
        print(sucessful_text)

    def radiobuttonclick(self):

        ##Verrification
        print(self.driver.title)
        print(self.driver.current_url)
        browservalue=self.driver.find_element(by=By.XPATH, value="//table[@id='j_idt87:console2']//td[4]//label").text
        print(browservalue)
        elementattribute = self.driver.find_element(by=By.XPATH,
                                                value="//table[@id='j_idt87:console2']//td[4]//label").get_attribute("for")
        print(elementattribute)
        print(self.driver.current_window_handle)

        checkboxtobeclicked=self.driver.find_element(by=By.XPATH,value="//table[@id='j_idt87:console2']//td[4]//span")
        if(checkboxtobeclicked.is_enabled()):
            print("passed enabled")
            if(checkboxtobeclicked.is_displayed()):
                print("passed displayed")

                if(checkboxtobeclicked.is_selected()==False):
                    print(self.driver.find_element(by=By.XPATH,value="(//table[@id='j_idt87:console1']//td[4]//div)[3]").is_selected())
                    self.driver.find_element(by=By.XPATH, value="//table[@id='j_idt87:console2']//td[4]//span").click()
                    time.sleep(2)
                    value=self.driver.find_element(by=By.XPATH,
                                                   value="//table[@id='j_idt87:console2']//td[4]//span").is_selected()
                    print(value)
                else:
                    print("The element is areadt selected")


obj=Alerts()
obj.Launch_Browser()
obj.radiobuttonclick()
