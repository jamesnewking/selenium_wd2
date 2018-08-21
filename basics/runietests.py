from selenium import webdriver
import os

class RunIETests():
    def test(self):
        driverLocation = "C:\\Users\\james\\Documents\\Personal\\selenium\\lib\\IEDriverServer_64.exe"
        os.environ["webdriver.ie.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Ie(driverLocation)
        # Open the provided URL
        driver.get("http://www.yahoo.com")
 
ieTest = RunIETests()
ieTest.test()
