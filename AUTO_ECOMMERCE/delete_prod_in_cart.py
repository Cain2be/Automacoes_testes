from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



def delete_prod_in_cart(browser, url_ecm):


    browser.get(f'{url_ecm}/index.php?route=checkout/cart')


    espera5 = WebDriverWait(browser, 5)
    
    try:
        delete_icon = espera5.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='col-1 action remove_pc']")))
        
        
        for dlts in delete_icon[:1]:
            browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", dlts)
            sleep(0.3)
            dlts.click()


    except TimeoutException:
        print(f'\033[91mTimeout: Ícone de deletar produtos não encontrado ou não clicável.\033[0m')
    except Exception:
        print(f'\033[91mErro ao tentar deletar um produto\033[0m')
