from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException



def buy_also(browser):
    try:

        espera5 = WebDriverWait(browser, 5)


        # Seleciona todos os campos da Home onde classe seja Adicionar Produto
        add_products = espera5.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@class='btn rounded-pill product-adicionar']")))
        
        # Seleciona 10 produtos para adicionar ao carrinho
        for prod in add_products[:1]:
            browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", prod)
            sleep(3)
        add_products = espera5.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn rounded-pill product-adicionar']")))
        add_products.click()



            
    except NoSuchElementException:
        print('\033[94mCliente não possui Compre aqui Também\033[0m')
    except TimeoutException:
        print('\033[94mCliente não possui Compre aqui Também\033[0m')



    sleep(1)