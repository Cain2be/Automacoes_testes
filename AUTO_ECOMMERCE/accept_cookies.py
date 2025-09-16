from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException



def accept_cookies(browser):

    espera5 = WebDriverWait(browser, 5)

    try:
        cookies_dismiss = espera5.until(EC.element_to_be_clickable((By.ID, 'cookie-dismiss')))
        cookies_dismiss.click()
        print('\033[92mCookies aceitos com Sucesso!\033[0m')

    except TimeoutException:
        print(f'\033[91mTimeout: Ícone de cookie não encontrado ou não clicável.\033[0m')
    except Exception:
        print(f'\033[91mErro ao tentar fechar Cookies\033[0m')