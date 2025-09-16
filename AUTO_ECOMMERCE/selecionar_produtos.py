from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def add_products(browser):

    espera5 = WebDriverWait(browser, 5)

    try:
        # Seleciona todos os campos da Home onde classe seja Adicionar Produto
        add_products = espera5.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@class='btn rounded-pill product-adicionar']")))
        
        # Seleciona 10 produtos para adicionar ao carrinho
        for prod in add_products[:10]:
            browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", prod)
            sleep(0.4)
            prod.click()
        
         
    except NoSuchElementException:
        print('\033[91mElemento "product-adicionar" não encontrado. Verifique o ID ou o estado da página.\033[0m')
    except TimeoutException:
        print('\033[91mNenhum ou poucos Produto(s) Encontrado(s)!\033[0m')