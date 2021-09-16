import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

PORTAL_UNDB_URL_DOCUMENTOS = "https://portal.undb.edu.br/Corpore.net/Source/Rpt-GeradorRelatoriosNet/RM.Rpt.Reports/Anonymous/RptFindReportByGuid.aspx"


class UndbStudentPortalRM(unittest.TestCase):

    def setUp(self):
        driver_options = Options()
        driver_options.add_argument("--headless")
        self.driver = webdriver.Firefox()

    def test_CT_001(self):
        """
        Nome: Validar documento informando identificador inválido
        Resumo: Solicitar uma validação de documento inexistente
        """
        driver = self.driver
        # Passo 01 // Acessar url de validacao de documentos
        driver.get(PORTAL_UNDB_URL_DOCUMENTOS)
        # Passo 02 // Dar foco no input de identificacao do relatorio
        elem = driver.find_element_by_id("txtGuid")
        # Passo 03 // Digitar um valor aleatorio
        elem.clear()
        elem.send_keys("UASHUSHU")
        # Passo 04 // Clicar no botao buscar
        btn = driver.find_element_by_id("btnBuscar")
        btn.click()
        # Passo 05 // Deve informar a mensagem de nao encontrado
        assert "Nenhum relatório encontrado para a identificação informada." in driver.page_source

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
