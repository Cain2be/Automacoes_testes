from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException



def finish_order(browser):

    # - - - Escolhendo Retirada - - -

    # try:
    espera5 = WebDriverWait(browser, 5)
    pickup_xpath = '//div[@class="custom-radio" and normalize-space(text())="Retirar na Loja"]'
    pickup_div = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, pickup_xpath)))
    # pickup_in_store = espera5.until(EC.element_to_be_clickable((By.XPATH,'//div[@class="custom-radio" and normalize-space(text())="Retirar na Loja"]/preceding-sibling::input')))
    browser.execute_script("arguments[0].scrollIntoView(true);", pickup_div)

    # Clique via JavaScript
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", pickup_div)
    browser.execute_script("arguments[0].click();", pickup_div)

    sleep(1)


    sleep(5)

    finish_buy = browser.find_element(By.ID, 'button_cart_checkout')
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", finish_buy)
    sleep(2)
    finish_buy.click()



    payment_method = browser.find_elements(By.CSS_SELECTOR, "button.nav-link.pane_tab")

    ids = [button.get_attribute("id") for button in payment_method]      # Extrai os IDs desses botões
    texts = [button.get_attribute("text") for button in payment_method]   # Extrai os Textos de cada método de entrega

    paid = 0

            # - - - FINALIZANDO EM DINHEIRO - - -
    if "cod2-tab" in ids:
        payment_money = browser.find_element(By.ID, 'cod2-tab')        
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", payment_money)
        payment_money.click()
        print('\033[92mMétodo de pagamento Dinheiro selecioando\033[0m')
        paid = 1


    
            # - - - FINALIZANDO CARTÃO NA ENTREGA - - - 
    elif "cod10-tab" in ids and paid == 0:
        payment_card = browser.find_element(By.ID, 'cod10-tab') 
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", payment_card)
        payment_card.click()
        print('\033[92mMétodo de pagamento Cartão na Entrega selecionado\033[0m')
        finish_merch()
        paid = 1

        
    elif paid == 123123:
        print('n vou cadastrar cartão do diow agr') ###################################




    # except NoSuchElementException:
    #     print('Cliente não possui Retirada! Optando por Delivery!')##########################################
    #     pickup = 0 ####################################
    # except TimeoutException: ##########################################
    #     print('Método RETIRADA não encontrado! Optando por Delivery!')##########################################
    #     pickup = 0 ##################################



    # Caso não tenha Retirada, vai pra entrega
        try:
            delivery = espera5.until(EC.element_to_be_clickable((By.ID, 'button_cart_checkout')))
            browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", delivery)
        
            sleep(1)

            delivery.click()

            browser.find_element(By.ID, 'input-cep').send_keys('14057100')

        except:
            print('oi')

    # Finalizando Pedido







def finish_merch(browser):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By


    espera20 = WebDriverWait(browser, 20)
    payment_confirm = espera20.until(EC.element_to_be_clickable((By.ID, 'button-confirm')))
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'})", payment_confirm)

    payment_confirm.click()
