from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import Select

def select_store_in_ecm(browser):
    """Seleciona a loja com value="1" na lista das unidades 'storeDropdown'
    browser: Instância do WebDriver (ex: webdriver.Chrome()). (Depende do navegador usado no teste)
    wait_obj: Instância de WebDriverWait.
    """
    
    espera5 = WebDriverWait(browser, 5)
    
    try:

        select_element = espera5.until(EC.presence_of_element_located((By.ID, "storeDropdown")))
        select = Select(select_element)

        for opt in select.options:
            if "Escolha" not in opt.text:
                select.select_by_visible_text(opt.text)
                print(f"\033[93mLoja selecionada: {opt.text}\033[0m")
                break


    except TimeoutException:
        print('\033[94mSomente uma Unidade, Pulando processo de seleção de Lojas!\033[0m')
    except NoSuchElementException:
         print('\033[91mElemento "storeDropdown" não encontrado. Verifique o ID ou o estado da página.\033[0m')
    except Exception as e:
        print(f'\033[91mOcorreu um erro inesperado ao selecionar a loja!\033[0m')
