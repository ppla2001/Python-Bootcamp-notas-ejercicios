#aprendo todo tipo click, click and drop, double click, etc. esta en la parte llamada action chains de https://selenium-python.readthedocs.io/index.html (documentation)
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #necesario para action chains

PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://orteil.dashnet.org/cookieclicker/')

driver.implicitly_wait(5) #no vamos a pasar esta linea de codigo hasta que esperemos x segundos

#va a haber un problema si ejecuto todo esto sin esperar un toque porq cuando entramos a la pagina hay un loading que tarda un toque en cargar las cookies, entonces vamos a tener que meter un wait, lo podemos hacer de la forma try,finally o de la forma de arriba
cookie = driver.find_element_by_id('bigCookie')
cookie_count = driver.find_element_by_id('cookies')
items = [driver.find_element_by_id('productPrice' + str(i)) for i in range(1,-1,-1)] #estoy diciendo que i va a empezar en 1 y va a ir a 0 terminando en 0, lo hacemos asi porq queremos q se mejoren las cosas mas caras antes de las mas baratas, se puede cambiar


actions = ActionChains(driver) #esto dice hagamos un objeto de action chain q actua en el web driver y lo guardamos en actions
#podemos crear una secuencia de como queremos que sea el action chain
actions.click(cookie)
#actions.perform() #es necesario el perform porq el script va a esperar a que aparezca para empezar a hacer los actions en la queue
for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(' ')[0]) #estamos agarrando de consola '0 cookies per second : 0', con el split(' ') se separa todos los espacios por una coma, y agarramos el indice 0 que es el numero, por lo que nos lleva la cuenta de cuantas cookies tenemos
    print(count)
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
