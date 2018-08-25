from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
        navTech = driver.find_element(By.XPATH,"//div[@id='navbarResponsive']//li/a[text()='Technologies']")
        navPortfolio = driver.find_element(By.XPATH, "//div[@id='navbarResponsive']//li/a[text()='Portfolio']")
        navAbout = driver.find_element(By.XPATH, "//div[@id='navbarResponsive']//li/a[text()='About']")
        navContact = driver.find_element(By.XPATH, "//div[@id='navbarResponsive']//li/a[text()='Contact']")

        cname = driver.find_element(By.ID,"name")
        cemail = driver.find_element(By.ID,"email")
        cphone = driver.find_element(By.ID,"phone")
        cmessage = driver.find_element(By.ID, "message")
        cbutton = driver.find_element(By.ID,"sendMessageButton")

        moreButton.click()
        time.sleep(1)
        navTech.click()
        time.sleep(1)
        navPortfolio.click()
        time.sleep(1)
        navAbout.click()
        time.sleep(1)
        navContact.click()
        time.sleep(1)
        cname.send_keys("James")
        cbutton.click()
        time.sleep(2)
        cemail.send_keys("jamesnewking@gmail.com")
        cbutton.click()
        time.sleep(2)
        cphone.send_keys("9495551212")
        cbutton.click()
        cname.clear()
        cemail.clear()
        cphone.clear()
        time.sleep(2)

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



