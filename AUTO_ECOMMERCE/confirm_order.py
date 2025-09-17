from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep



def click_payment_option(browser, element_id, label):
    """Rola até o botão e clica nele"""
    try:
        btn = browser.find_element(By.ID, element_id)
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        btn.click()
        print(f'\033[92mMétodo de pagamento {label} selecionado\033[0m')
        return True
    except TimeoutException:
        print(f'\033[91mNão foi possível clicar em {label}\033[0m')
        return False




def finish_order(browser):
    espera5 = WebDriverWait(browser, 5)


    # Espera os botões de método de pagamento aparecerem
    payment_buttons = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.nav-link.pane_tab"))
    )
    ids = [btn.get_attribute("id") for btn in payment_buttons]

    # Escolhe o primeiro método disponível na ordem de preferência
    if "cod2-tab" in ids:  # dinheiro
        click_payment_option(browser, 'cod2-tab', 'Dinheiro')
    elif "cod10-tab" in ids:  # cartão na entrega
        click_payment_option(browser, 'cod10-tab', 'Cartão na Entrega')
    else:
        print('\033[91mNenhum método de pagamento suportado encontrado\033[0m')
        return

    # Confirma o pedido
    confirm_btn = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.ID, 'button-confirm'))
    )
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'})", confirm_btn)
    confirm_btn.click()
    print('\033[92mPedido finalizado com sucesso!\033[0m')
    
    sleep(2)
    # nmr_ped = browser.find_element(EC.text_to_be_present_in_element(By.ID, 'order_id'))
    order_id_locator = (By.ID, 'order_id')
    espera5.until(EC.presence_of_element_located(order_id_locator))
    order_id_element = browser.find_element(*order_id_locator)
    print(f'Número do Pedido: {order_id_element.text}')
    