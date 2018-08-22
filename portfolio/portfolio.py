from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class JamesPortfolio():

    def contactForm(self):
        portfolioUrl = 'http://jameswww.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(portfolioUrl)
        pageTitle = driver.title
        print('Title of the webpage is: ' + pageTitle)
        moreButton = driver.find_element(By.XPATH,"//body[@id='page-top']//a[text()='Tell Me More']")
        cname = driver.find_element(By.ID,"name")
        cemail = driver.find_element(By.ID,"email")
        cphone = driver.find_element(By.ID,"phone")
        cmessage = driver.find_element(By.ID, "message")
        cbutton = driver.find_element(By.ID,"sendMessageButton")
        moreButton.click()
        time.sleep(2)
        cname.send_keys("James")
        cbutton.click()
        time.sleep(2)
        cemail.send_keys("jamesnewking@gmail.com")
        cbutton.click()
        time.sleep(2)
        cphone.send_keys("9495551212")
        cbutton.click()
        time.sleep(1)

        #self.snackPortfolio()
        snackPort = driver.find_element(By.XPATH, "//section[@id='portfolio']//a[@href='#portfolioModal1']")
        snackPort.click()
        time.sleep(3)
        # driver.switch_to.active_element()
        snackModal = driver.find_element(By.XPATH, "//div[@id='portfolioModal1']//a[@href='http://snackseriously.com']/img[@alt='']")
        snackModal.click()
        print('clicked on snackseriously inside of modal')
        time.sleep(4)


        #self.closeTest()
        # driver.close()
        driver.quit()
        print('closed tests')


    # def snackPortfolio(self):


    # def closeTest(self):


portfolioTest = JamesPortfolio()
portfolioTest.contactForm()



