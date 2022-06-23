#Importamos las librerias 
import time
from dataclasses import replace
from telnetlib import EC
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# Segun un articulo de internet se modificaron funciones a partir de la v4 
# Razon por la cual es necesario importa las siguientes librerias
# Mas Informacion: https://itsmycode.com/executable-path-has-been-deprecated/
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Llamamos al directorio donde se encuentra el ejecutable
driver_path = 'C:\\Users\\Pedro\\Downloads\\chromedriver\\chromedriver.exe'

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()))

#Inicia la pagina
driver.get('https://www.epicgames.com/site/es-ES/home')

#Selecciona el boton de inicia sesion
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'div.sc-cOFTSb eYgsmV'.replace(' ','.'))))\
    .click()


element = driver.find_element(By.CSS_SELECTOR, "h6.MuiTypography-root sc-dmlqKv gKbqoA sc-hHfuMS epIHKZ MuiTypography-subtitle2 MuiTypography-colorTextPrimary MuiTypography-alignCenter").text
assert element == "Recordarme"

#Seleccionar la opcion con la cual iniciaremos Sesion
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'div.MuiButtonBase-root MuiListItem-root sc-eHfRjS jxyytG MuiListItem-gutters MuiListItem-button'.replace(' ','.'))))\
    .click()
   
#Seleccionara cuadro texto para ingresar nuestro email
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        
                                    'input#email')))\
    .send_keys('pedlui17@gmail.com')

#Hace click en el boton Cursos
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,          
                                    'input#password')))\
    .send_keys('soyelrey10')


WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'button#sign-in')))\
    .click()
                            
time.sleep(20)

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'a.talon_close_button')))\
    .click()
    
#time.sleep(100)
elementp = driver.find_element(By.CSS_SELECTOR, "p").text

#Utilizando el assert, primero con el resultado correcto
assert elementp == "Recordarme"

#Utilizando el assert, ahora con un resultado incorrecto
#assert elementp == "Recordarme!!!"

print(elementp)

driver.quit()

