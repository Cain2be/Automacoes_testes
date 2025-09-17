from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


def open_cart(browser):

    espera5 = WebDriverWait(browser, 5)
    
    try:
        # Localiza o ícone usado no carrinho da tela
        xpath_cart_icon = '//div[@class="header-action-icon-2"]//i[contains(@class, "fa-cart-shopping")]'

        cart_icon = espera5.until(EC.element_to_be_clickable((By.XPATH, xpath_cart_icon)))
        cart_icon.click()
        
        print('\033[92mClicado no ícone do carrinho.\033[0m')
        sleep(1)# Espera um pouco para o dropdown do carrinho aparecer

    except TimeoutException:
        print(f'\033[91mTimeout: Ícone do carrinho não encontrado ou não clicável.\033[0m')
    except Exception:
        print(f'\033[91mErro ao tentar abrir o mini-carrinho\033[0m')