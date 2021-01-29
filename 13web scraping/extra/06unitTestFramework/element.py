from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object): #this will represent one element from page, ej: searchbar o form input
#we have an element on a page, we want to set its value, always follow this process:
    def __set__(self,obj,value):
        driver = obj.driver #essentially the web driver
        WebDriverWait(driver,100).until(
            lambda driver: driver.find_element_by_name(self.locator)) #self.locator va ser = to the name we want to use to locate the element
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self,obj,owner):
        driver = obj.driver
        WebDriverWait(driver,100).until( #waiting for element to exist on page
            lambda driver: driver.find_element_by_name(self.locator)) #waiting for element to exist on page
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute('value') #dice get the attribute from html of value and return that
        #esto dice we want to access a value of an element is lets wait for that element to exist on the page, then we set element = driver.find_element_by_name(self.locator)
