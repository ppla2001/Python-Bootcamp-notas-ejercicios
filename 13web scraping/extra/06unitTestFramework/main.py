import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase): #unittest.TestCase nos da acceso a algunos methods y cosas q van a ser inherited

    def setUp(self): #esto runs in the beggining, todas las veces que se hagan tests, en este caso dos veces
        print('setUp')
        self.driver = webdriver.Chrome('C:\\Program Files (x86)\\chromedriver.exe')
        self.driver.get('http://www.python.org')
    '''
    def test_example(self): #method that tests something
        print('Test')
        assert False #assert says 'see if the condition in the right is true', test case failed or passed

    def test_example_two(self):
        assert True

    def not_a_test(): #doesnt run automatically porq no empieza con test(lowecase)
        print('This wont print')
ejemplo de tests
    '''

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = 'pycon'
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self): #esto runs in the end
        self.driver.close()

if __name__ == '__main__': #this says run all of the unittest
    unittest.main()
