from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handywrapper import HandyWrappers
import time

class UsingWrappers():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        textField1 = hw.getElement("name")
        textField1.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()
        time.sleep(2)

        eleResult1 = hw.isElementPresent("name", By.ID)
        print('Check if element "name" exists ' + str(eleResult1))

        eleResult2 = hw.elementPresenceCheck("//input[@id='name']", By.XPATH)
        print('Check if element "name" exists again ' + str(eleResult2))

        driver.quit()
        print('closed tests')

ff = UsingWrappers()
ff.test()


