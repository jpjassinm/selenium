import unittest #Lo utilizamos para traer todas nuestra pruebas.
from pyunitreport import HTMLTestRunner # Nos ayudar a orquetar cada una de las pruebas, junto con los reportes.
from selenium import webdriver #Importamos el conector con la pagina.


class holaMundo(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def testHolaMundo (self): # En esta funcion colocamos todos los paso a ejecutar
        pass

    def tearDown(self):
        self.driver.quit() #Cierra la ventana una vez finalizada la ejecución

if name == "__main__":
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output = "Reportes", report_name = "Hola_mundo_Reporte"))