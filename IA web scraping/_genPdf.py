# https://www.youtube.com/watch?v=Oo8-nEuDBkk&t=454s
import time
import os
import argparse
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Configura argparse para manejar argumentos de línea de comandos
parser = argparse.ArgumentParser(description='Extraer datos del producto.')
parser.add_argument('referencia', type=str, help='Número de referencia del producto')
args = parser.parse_args()

# Obtiene la referencia del producto del argumento de línea de comandos
refe = args.referencia

os.system('cls')

print("Iniciando chrome...")

driver_path = 'C:\\Users\\Economizadores\\Documents\\chromedriver-win64\\chromedriver.exe'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(driver_path), options=options)

try:
    time.sleep(10)

    driver.get('https://economizadores.net/')
    print("Page loaded...")

    # Selecciona el botón por clase
    button = driver.find_element(By.CSS_SELECTOR, '.pum-close.popmake-close')
    button.click()
    print('Click')

finally:
    time.sleep(10)
    print('Error...')
    driver.quit()