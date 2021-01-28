#esto es lo que se hace primero
from selenium import webdriver

PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
driver = webdriver.Chrome(PATH)
#ahora ya podemos hacer script, por ejemplo :
driver.get('https://techwithtim.net') #esto me abre la pagina
print(driver.title) #me da el title
driver.close() #close the tab que abrimos
driver.quit() #close the window que abrimos
