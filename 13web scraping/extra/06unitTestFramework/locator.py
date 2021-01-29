#any css selector, any id, any way we locate elements we keep here
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.ID,'Submit') #how we want to access and what their value is, me fije en la pagina de Python.org, fui al boton de go inspeccione vi q tiene un id y q tiene submit

class SearchResultsPageLocators(object):
    pass
