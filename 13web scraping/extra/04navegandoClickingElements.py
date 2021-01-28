from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#--------esto es para que espere para pasar pagina ---------- https://selenium-python.readthedocs.io/index.html (documentation)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------------------
import time

PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')

link = driver.find_element_by_link_text('Python Programming') #esto directamente te agarra el link usando el como se llama en vez de tener que inspeccionar la pagina
link.click()
#hay que acordarse que hay cuando entramos a una nueva pagina tenemos que esperar a que carguen las cosas antes de clickear (tienen que existir para que se puedan clickear)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    driver.back() #goes back to the previos page
    driver.back()
    driver.forward() #va para delante, lo contrario a .back
    driver.back()


except: #cambio el finally por except porq no quiero que se cierre si esto no funciona
    driver.quit()


#element.clear() se usa por ejemplo en buscadores para que no quede texto interfiriendo
