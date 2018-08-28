from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitDemo():

    def test(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.find_element(By.ID, "primary-header-flight").click()
        driver.find_element(By.ID, "flight-origin-flp").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination-flp").send_keys("NYC")
        # driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("12/24/2018")
        driver.find_element(By.ID, "flight-departing-flp").click()
        driver.find_element(By.XPATH, "//div[@id='flight-departing-wrapper-flp']/div[@class='datepicker-dropdown']/div/div[2]/table[@class='datepicker-cal-weeks']/tbody/tr[5]/td[5]/button[@type='button']").click()
        # returnDate = driver.find_element(By.ID, "flight-returning")
        # returnDate.clear()
        # returnDate.send_keys("12/26/2018")
        # driver.find_element(By.ID, "flight-returning-flp").click()
        # driver.find_element(By.ID, "//div[@id='package-returning-wrapper-hp-package']/div[@class='datepicker-dropdown']/div/div[3]/table[@class='datepicker-cal-weeks']/tbody/tr[5]/td[3]/button[@type='button']").click()
        # driver.find_element(By.XPATH,'//div[@id="package-returning-wrapper-flp"]/div/div/div[3]/table/tbody/tr[5]/td[3]/button').click()
        # //section[@class='cal-month][position()=2]//a[text()='25']
        driver.find_element(By.CSS_SELECTOR, "button.btn-primary.btn-action.gcw-submit").click()

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID, "flexible-search-toggle")))
        element.click()

        time.sleep(2)
        driver.quit()

ff = ExplicitWaitDemo()
ff.test()
