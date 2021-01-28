from selenium import webdriver
from selenium.webdriver.common.keys import Keys #nos da acceso a enter key,escape key, etc para que podamos escribir cosas y darle al enter y que nos den resultados
#--------esto es para que espere para pasar pagina ---------- https://selenium-python.readthedocs.io/index.html (documentation)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------------------------------------------------------------------------------
import time

PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')

search = driver.find_element_by_name('s') #find element hay un monton, en este caso como lo saque del html con name, lo voy a usar asi aca pero tambien hay por id y class etc
search.send_keys('test')
search.send_keys(Keys.RETURN) #return significa enter

#quiero tener accesso de toda la pagina en la que entre, osea quiero tener acceso a todo el html
#print(driver.page_source)
'''
main = driver.find_element_by_id('main')
print(main.text)
con esto lo que estoy haciendo es agarrando todo pero quizas haya un problema porq hay mas de una pagina y puede llegar a pasar pagina antes de que agarre toda la info, para que espere a agarrar la info para pasar pagina se va a usar lo siguiente
'''
#todo esto de try y finally es para q espere para pasar pagina
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    print(main.text)
except: #cambio el finally por except porq si no te lo cierra pase lo q pase, en cambio con except espera a que te de el resultado y despues lo cierra
    driver.quit()

#lo que dice el coso de arriba el element(main) es = a la espera (10 segundos maximo) que hace el driver para encontrar la presencia de lo que estamos pidiendo (en este caso byID pero puede ser by name class etc)


#ahora vamos con los headers
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements_by_tag_name('article')

    for article in articles:
        header = article.find_element_by_class_name('entry-summary')
        print(header.text)

finally:
    driver.quit()

#time.sleep(5) #delays program for five seconds

#driver.quit()
