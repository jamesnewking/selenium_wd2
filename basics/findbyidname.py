from selenium import webdriver

class FindByIdName():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        elementById = driver.find_element_by_id("name")

        if elementById is not None:
            print("we found an element by Id")

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print("we found an element by name")

findIDName = FindByIdName()
findIDName.test()
