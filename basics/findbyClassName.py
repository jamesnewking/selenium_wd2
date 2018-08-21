from selenium import webdriver

class FindByClassName():

    def test(self):
        baseURL = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        elementByClassName = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("Testing the element")

        if elementByClassName is not None:
            print("we found an element by Class Name")

        elementByTagName = driver.find_element_by_tag_name("h1")
        text = elementByTagName.text

        if elementByTagName is not None:
            print("we found an element by Tag Name and the text on the element is: " + text)

ffclassname = FindByClassName()
ffclassname.test()
