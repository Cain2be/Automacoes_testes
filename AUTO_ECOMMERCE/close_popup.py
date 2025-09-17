from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException



def close_popup(browser):
        
    espera5 = WebDriverWait(browser, 5)

    try:
        popup = espera5.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-close'))) # Localiza Pop-UP
        print('\033[92mPop-UP Encontrado!\033[0m')
        popup.click() # Fecha Pop-up
        print('\033[92mPop-UP Fechado!\033[0m')
    

    except:
        try:
            popup2 = espera5.until(EC.visibility_of_element_located((By.ID, 'edrone-onsite-popup-content')))
            print(f'\033[93mPop-UP Edrone Encontrado: {popup2}\033[0m')
        except TimeoutException:
            print('\033[91mNenhum Pop-UP na página!\033[0m')
            # Segundo try acontece por alguns sites demorarem para exibirem o pop-up do ecommerce, e outros exibirem duas vezes.