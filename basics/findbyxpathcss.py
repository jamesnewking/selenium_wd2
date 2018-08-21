from selenium import webdriver

class FindByXpathCSS():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")

        if elementByXpath is not None:
            print("we found an element by xpath")

        elementByCSS = driver.find_element_by_css_selector("#displayed-text")

        if elementByCSS is not None:
            print("we found an element by CSS selector")

fxpath = FindByXpathCSS()
fxpath.test()
