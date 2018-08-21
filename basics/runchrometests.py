from selenium import webdriver
import os

class RunChromeTests():
    def test(self):
        driverLocation = "C:\\Users\\james\\Documents\\Personal\\selenium\\lib\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)
        # Open the provided URL
        driver.get("http://www.yahoo.com")

chromeTest = RunChromeTests()
chromeTest.test()
