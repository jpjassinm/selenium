#para que este proyecto funcione debes instalar pyunitreport y selenium, tambien se debe descargar del chromedrive para selenium.
import unittest #Lo utilizamos para traer todas nuestra pruebas.
from pyunitreport import HTMLTestRunner # Nos ayudar a orquetar cada una de las pruebas, junto con los reportes.
from selenium import webdriver #Importamos el conector con la pagina.


class holaMundo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"C://Users/Colpensiones/Documents/Selenium/chromedriver.exe")
        drive = self.driver
        drive.implicitly_wait(7)


    def testHolaMundo (self): # En esta funcion colocamos todos los paso a ejecutar
        drive = self.driver
        drive.get("http://www.platzi.com")


    def tearDown(self):
        self.driver.quit() #Cierra la ventana una vez finalizada la ejecución

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output = "Reportes", report_name = "Hola_mundo_Reporte"))
