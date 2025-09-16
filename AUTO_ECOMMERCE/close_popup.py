from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



def close_popup(browser):
        
    espera5 = WebDriverWait(browser, 5)

    try:
        popup = espera5.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-close')))
        print('\033[92mPop-UP Encontrado!\033[0m')
        popup.click()
        print('\033[92mPop-UP Fechado!\033[0m')
    
    except:

        try:
            popup2 = espera5.until(EC.visibility_of_element_located((By.ID, 'edrone-onsite-popup-content')))
            print(f'{popup2}\033[91mPop-UP Edrone Encontrado!\033[0m')
#                popup2.click()
#                print('\033[91Pop-UP Fechado!\033[0m')

        except:
            print('\033[91mNenhum Pop-UP na página!\033[0m')