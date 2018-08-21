from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElements():

    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/pages/practice'
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementListByClassName = driver.find_elements_by_class_name("inputs")
        length = len(elementListByClassName)

        if elementListByClassName is not None:
            print("Size of the class name list is: " + str(length))

        elementListByTagName = driver.find_elements(By.TAG_NAME, "td")
        lengthtag = len(elementListByTagName)

        if elementListByTagName is not None:
            print("Size of the tag name list is: " + str(lengthtag))

ff = ListOfElements()
ff.test()