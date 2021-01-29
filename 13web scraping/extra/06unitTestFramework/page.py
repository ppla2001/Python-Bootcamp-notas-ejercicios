from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = 'q' #search bar id name is 'q'

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver


class MainPage(BasePage): #no hace falta definir un init en esta class porq estamos usando los metodos de BasePage

    search_text_element = SearchTextElement()

    def is_title_matches(self): #title of webpage matches what we want it to match?
        return 'Python' in self.driver.title #Python in title of website?

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON) #*significa unpack, pasa de un tuple a arguments, lo separa en dos entities
        element.click()

class SearchResultPage(BasePage):

    def is_results_found(self):
        return 'No results found' not in self.driver.page_source #si el 'No results found' no aparece en html, significa q el codigo funciono bien, otherwise it will be False
