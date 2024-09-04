import time
import os
import argparse
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

    # Selecciona el botón por clase para cerrar el pop-up
    button = driver.find_element(By.CSS_SELECTOR, '.pum-close.popmake-close')
    button.click()
    print('Pop-up closed')

    # Encuentra el campo de búsqueda y introduce la referencia
    search_box = driver.find_element(By.CSS_SELECTOR, 'input[name="s"]')
    search_box.send_keys(refe)
    search_box.send_keys(Keys.RETURN)  # Envía el formulario (presiona Enter)

    print(f'Search for: {refe}')

    # Espera para ver los resultados (ajusta el tiempo según sea necesario)
    time.sleep(10)

finally:
    print('Quitting browser...')
    driver.quit()