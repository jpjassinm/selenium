import pandas as pd
from time import sleep
from selenium import webdriver

csv = open('./ENTRADA/versiculos.xls','w')
csv.close()

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://www.biblegateway.com/passage/?search=Juan%203%3A16&version=RVR1960')

datos = pd.read_csv('./ENTRADA/versiculos.csv',header=0)
print(datos)

for versiculo in datos.values:
    sleep(1)

    consulta = versiculo
    ingreso_versiculo = driver.find_element_by_xpath('/html/body/div[2]/div/section/div[1]/div/form/div[1]/div[1]/input')
    ingreso_versiculo.send_keys(consulta)
    
    sleep(1)