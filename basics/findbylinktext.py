from selenium import webdriver

class FindByLinkText():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        elementByLinkText = driver.find_element_by_link_text("Login")

        if elementByLinkText is not None:
            print("we found an element by Link Text")

        elementByPartialLinkText = driver.find_element_by_partial_link_text("Pract")

        if elementByPartialLinkText is not None:
            print("we found an element by Partial Link Text")

fflinktext = FindByLinkText()
fflinktext.test()
