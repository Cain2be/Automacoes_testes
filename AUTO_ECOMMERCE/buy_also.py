from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException



def buy_also(browser):
    espera5 = WebDriverWait(browser, 5)
    try:
        espera5 = WebDriverWait(browser, 5)

        also_xpath = '//button[@class="btn rounded-pill product-adicionar"]' # XPATH do Compre Aqui Também
        also_option = espera5.until(EC.element_to_be_clickable((By.XPATH, also_xpath))) # Espera ser clicável o Compre aqui também
        
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", also_option) # Traz o elemento para o centro da tela
        overlay_locator = (By.CSS_SELECTOR, "div.overlay") # Localiza o botão de loading no CSS da tela
        espera5.until(EC.invisibility_of_element_located(overlay_locator))
        also_xpath = '//button[@class="btn rounded-pill product-adicionar"]' # XPATH do Compre Aqui Também

        also_option = espera5.until(EC.element_to_be_clickable((By.XPATH, also_xpath))) # Espera ser clicável o Compre aqui também
        browser.execute_script("arguments[0].click();", also_option) # Clica com JS


    except NoSuchElementException:
        print('\033[94mCliente não possui Compre aqui Também\033[0m')
    except TimeoutException:
      print('\033[94mCliente não possui Compre aqui Também\033[0m')


    sleep(1)
