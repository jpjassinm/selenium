#con este se saca la imagenes grandes de CLC con el isbn


import pandas as pd
from time import sleep
from selenium import webdriver

csv = open('./isbnCLC/Imagenes_URL.xls','w')
csv.close()

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://www.clccolombia.com/product/biblia-rvrcolor-maderala-verdad-para-las-generacionesrustica')


datos = pd.read_csv('./ENTRADA/versiculos.csv',header=0)
print(datos)

for isbn in datos.values:

    sleep(1)
    
    consulta = int(isbn)
    ingreso_producto = driver.find_element_by_xpath('//input[@class="search-text-input"]')
    ingreso_producto.send_keys(consulta)
    sleep(1)

    click_producto = driver.find_element_by_xpath('//input[@class="button search-button expanded"]')
    click_producto.click()
    sleep(1)

    try:
        click_producto = driver.find_element_by_xpath('//img[@id="ctl00_pimg_imgProduct"]')
        click_producto.click()
        sleep(1)

        nombre = driver.find_element_by_xpath('//div[@class="large-6 small-6 columns"]//h1').text
        print(nombre)


        precio = driver.find_element_by_xpath('//span[@class="your-price"][1]').text
        print(precio)


        disponible = driver.find_element_by_xpath('//div[@id="ctl00_ppricecartajx_divStockAvailability"][1][text()]').text
        print(disponible)

        img = driver.find_element_by_xpath('//img[@id="ctl00_pimg_imgOrig"]').get_attribute('src')
        print(img)
        sleep(1)

        click_producto = driver.find_element_by_xpath('//button[@class="close-button"]')
        click_producto.click()

        ingreso_producto = driver.find_element_by_xpath('//input[@class="search-text-input"]')
        ingreso_producto.clear()

        registro = ""+str(consulta)+";"+nombre+";"+img+""

        csv = open('./isbnCLC/Imagenes_URL.csv','a')
        importacion = str(registro)
        csv.write(importacion + "\n")
        csv.close()

    except:

        nombre ='No tiene'
        Precio = 'No tiene'
        disponible = 'No tiene'
        img = 'No tiene'
        consulta = consulta

        ingreso_producto = driver.find_element_by_xpath('//input[@class="search-text-input"]')
        ingreso_producto.clear()


        registro = ""+str(consulta)+";"+nombre+";"+img+""


        csv = open('Imagenes_URL.csv','a')
        importacion = str(registro)
        csv.write(importacion+"\n")
        csv.close()