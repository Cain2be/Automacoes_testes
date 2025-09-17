from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def go_to_payment(browser):
    espera5 = WebDriverWait(browser, 5)
    finish_buy = browser.find_element(By.ID, 'button_cart_checkout')
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", finish_buy)
    sleep(1)
    overlay_locator = (By.CSS_SELECTOR, "div.overlay") # Localiza o botão de loading no CSS da tela
    espera5.until(EC.invisibility_of_element_located(overlay_locator)) # Espera o botao ficar invisível na tela
    finish_buy.click()




def choose_delivery(browser):
    espera5 = WebDriverWait(browser, 5)

    # - - - Escolhendo Retirada - - -
    try:
        # Seleciona "Retirar na Loja"
        pickup_xpath = '//div[@class="custom-radio" and normalize-space(text())="Retirar na Loja"]'
        pickup_option = espera5.until(EC.element_to_be_clickable((By.XPATH, pickup_xpath)))
        # Clique via JavaScript
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", pickup_option)
        browser.execute_script("arguments[0].click();", pickup_option)
        print("\033[92mOpção 'Retirar na Loja' selecionada!\033[0m")
        go_to_payment(browser)
        return
    except:
        print("\033[91mOpção 'Retirar na Loja' não encontrada!\033[0m")
    


    # Caso não tenha Retirada, vai pra entrega
    # try:
    #     espera5 = WebDriverWait(browser, 5)
    #     pickup_xpath = '//div[@class="custom-radio" and normalize-space(text())="Entrega"]' # Encontra o método de entrega "Entrega"
    #     pickup_option = espera5.until(EC.element_to_be_clickable((By.XPATH, pickup_xpath))) # Aguarda ficar clicável
    #     browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", pickup_option) # Centraliza o elemento
    #     browser.execute_script("arguments[0].click();", pickup_option) # Clica com JavaScript
    #     overlay_locator = (By.CSS_SELECTOR, "div.overlay") # Localiza o botão de loading no CSS da tela
    #     espera5.until(EC.invisibility_of_element_located(overlay_locator)) # Espera o botao ficar invisível na tela
    #     cep_input = browser.find_element(By.NAME, "CEP") # Encontra o campo de cep
    #     cep_input.clear() # Limpa a info que estiver no campo CEP
    #     cep_input.send_keys("14057100") # Preenche o CEP padrão
    #     #entregas = [browser.find_elements(By.XPATH, "//input[@name = 'shipping_method']")]
    #     entregas = espera5.until(EC.presence_of_all_elements_located((By.XPATH, "//label[@class = 'form-check-label']"))) # Encontra todos os métodos de entrega
    #     try:
    #         for m in entregas[:1]: # Percorre o primeiro método de entrega cadastrado e o seleciona para ser o método utilizado
    #             browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", m)
    #             sleep(0.3)
    #             m.click()
    #             name_method = m.text
    #             print(f"\033[92mOpção {name_method} selecionada!\033[0m")
    #     except:
    #         print(f'\033[91mNenhum Método de entrega cadastrado, ou não encontrado na página\033[0m')
    # except:
        # print("\033[91mNenhuma opção de entrega encontrada!\033[0m")


    # Finalizando Pedido








