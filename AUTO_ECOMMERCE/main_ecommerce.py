from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException as NSEE
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from login import logar
from abrir_carrinho import open_cart
from accept_cookies import accept_cookies
from close_popup import close_popup
from compre_tambem import buy_also
from finalizar_pedido import finish_orderrrrrrr
from realizar_pagamento import finish_order, finish_merch
from selecionar_produtos import add_products
from select_store_in_ecm import select_store_in_ecm



url_ecm = ('https://consuladoracao.com.br/')
#url_ecm = ('https://compras.supertecha.com.br/')
browser = webdriver.Chrome() # Abrir o navegador
browser.get(url_ecm)  # Abrir um ecommerce 
browser.maximize_window() # Abre tela cheia




select_store_in_ecm(browser) # NOTE Escolhe a Loja para acessar o E-commerce


close_popup(browser) # NOTE Fecha um Pop-up do e-commerce


logar(browser, url_ecm) # NOTE Loga no E-commerce, caso não tenha cadastro, realiza o cadastro


accept_cookies(browser) # NOTE Aceita Cookies do navegador


add_products(browser) # NOTE Adiciona os Produtos ao carrinho


open_cart(browser) # NOTE Abre o carrinho


finish_orderrrrrrr(browser, url_ecm) # NOTE Finalizar Pedido


buy_also(browser) # NOTE Utiliza a ferramenta de compra também


finish_order(browser) # NOTE 


finish_merch(browser) # NOTE 


# def select_store_in_ecm():
#     """Seleciona a loja com value="1" na lista das unidades 'storeDropdown'
#     browser: Instância do WebDriver (ex: webdriver.Chrome()). (Depende do navegador usado no teste)
#     wait_obj: Instância de WebDriverWait.
#     """
    
    
#     try:
#         select_store = espera5.until(EC.visibility_of_element_located((By.ID, 'storeDropdown')))    # Abre a seleção de Lojas
#         select_store.click()
#         select_obj = Select(select_store)
#         select_obj.select_by_value("1")         # Seleciona a Loja 1 (se n tiver loja 1, fudeu)
#         print("\033[93mLoja selecionada com sucesso!\033[")            
#         sleep(2)
#         selected_option = select_obj.first_selected_option
#         print(f"Opção selecionada: {selected_option.text}")        # Printa Loja selecionada

#     except TimeoutException:
#         print('\033[94mSomente uma Unidade, Pulando processo de seleção de Lojas!\033[0m')
#     except NoSuchElementException:
#          print('\033[91mElemento "storeDropdown" não encontrado. Verifique o ID ou o estado da página.\033[0m')
#     except Exception as e:
#         print(f'\033[91mOcorreu um erro inesperado ao selecionar a loja!\033[0m')



# def close_popup():
#         try:
#             popup = espera5.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-close')))
#             print('\033[92mPop-UP Encontrado!\033[0m')
#             popup.click()
#             print('\033[92mPop-UP Fechado!\033[0m')
        
#         except:

#             try:
#                 popup2 = espera5.until(EC.visibility_of_element_located((By.ID, 'edrone-onsite-popup-content')))
#                 print(f'{popup2}\033[91mPop-UP Edrone Encontrado!\033[0m')
# #                popup2.click()
# #                print('\033[91Pop-UP Fechado!\033[0m')

#             except:
#                 print('\033[91mNenhum Pop-UP na página!\033[0m')




# def finish_merch():
#     from selenium.webdriver.support.ui import WebDriverWait


#     espera20 = WebDriverWait(browser, 20)
#     payment_confirm = espera20.until(EC.element_to_be_clickable((By.ID, 'button-confirm')))
#     browser.execute_script("arguments[0].scrollIntoView({block: 'center'})", payment_confirm)

#     payment_confirm.click()






# sub_text_login_element = browser.find_element(By.TAG_NAME, 'sub') # Verifica qual o texto do Login
# sub_text_login = sub_text_login_element.text.strip()



# select_store_in_ecm()
# close_popup()




# if "Entre" in sub_text_login: # Se o Login não foi feito (Em baixo do Minha Conta está escrito ENTRE)
    
#     browser.get(f'{url_ecm}//index.php?route=account/login') # Vai pra tela de login

#     espera5.until(EC.element_to_be_clickable((By.ID, 'input-email'))).send_keys('45951270812') # Digita email
#     browser.find_element(By.ID, 'input-password').send_keys('++big2be##') # Digita a senha
#     espera5.until(EC.element_to_be_clickable((By.NAME, 'login'))).click() # Clica em Continuar

#     sleep(0.5)
    
#     try:
#         alerta = espera5.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "alert-danger")]')))
    
#         print('\033[91mCadastro não encontrado! Redirecionando...\033[0m')
#         browser.get(f'{url_ecm}/index.php?route=account/register')        



#         espera5.until(EC.element_to_be_clickable((By.ID, 'input-custom-field1')))  # Espera primeiro campo ser clicável
#         browser.find_element(By.ID, 'input-custom-field1').send_keys('45951270812') # Insere CPF
#         browser.find_element(By.ID, 'input-firstname').send_keys('Caio') # Insere Nome
#         browser.find_element(By.ID, 'input-lastname').send_keys('Stabile') # Insere Sobrenome
#         browser.find_element(By.ID, 'input-email').send_keys('caio.bstabile@hotmail.com') # Insere Email
#         browser.find_element(By.ID, 'input-telephone').send_keys('16982660505') # Insere Telefone
#         browser.find_element(By.ID, 'input-password').send_keys('123teste123') # Insere Senha
#         browser.find_element(By.ID, 'input-confirm').send_keys('123teste123') # Insere Confirmação de Senha
#             # Aguarda até a opção "não" estar visível
#         nao_radio = espera5.until(
#             EC.presence_of_element_located((By.XPATH, '//input[@name="newsletter" and @value="0"]')))
#             # Scroll até enxergar
#         browser.execute_script("arguments[0].scrollIntoView({block: 'center'})", nao_radio)
#             # Força o click na opção Não, evitando sobreposição
#         browser.execute_script("arguments[0].click();", nao_radio)
#         sleep(0.3)

#         try:
#             privacy_policy = browser.find_element(By.NAME, 'agree').click()
#             sleep(0.3)
#         except:
#             pass

#             # Clica em Continuar
#         browser.find_element(By.NAME, 'login').click()

#         print('\033[92mCadastro Realizado!\033[0m')



#     except:
#        print('\033[92mLogin completo\033[0m')




# close_popup()




# # - - - ACEITANDO COOKIES - - -
# try:
#     cookies_dismiss = espera5.until(EC.element_to_be_clickable((By.ID, 'cookie-dismiss')))
#     cookies_dismiss.click()
#     print('\033[92mCookies aceitos com Sucesso!\033[0m')

# except TimeoutException:
#     print(f'\033[91mTimeout: Ícone de cookie não encontrado ou não clicável.\033[0m')
# except Exception:
#     print(f'\033[91mErro ao tentar fechar Cookies\033[0m')





# try:
#     # Seleciona todos os campos da Home onde classe seja Adicionar Produto
#     add_products = espera5.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@class='btn rounded-pill product-adicionar']")))
    
#     # Seleciona 10 produtos para adicionar ao carrinho
#     for prod in add_products[:10]:
#         browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", prod)
#         sleep(0.4)
#         prod.click()
        
         
# except NoSuchElementException:
#     print('\033[91mElemento "product-adicionar" não encontrado. Verifique o ID ou o estado da página.\033[0m')
# except TimeoutException:
#     print('\033[91mNenhum ou poucos Produto(s) Encontrado(s)!\033[0m')




# # - - - ABRINDO DROPDOWN DO CARRINHO - - -

# try:
#     print('\033[94mTentando localizar e clicar no ícone do carrinho para abrir o mini-carrinho...\033[0m')
#     # É um 'i' com a classe 'fa-cart-shopping' e geralmente dentro de um 'div.header-action-icon-2'
#     xpath_cart_icon = '//div[@class="header-action-icon-2"]//i[contains(@class, "fa-cart-shopping")]'

#     cart_icon = espera5.until(EC.element_to_be_clickable((By.XPATH, xpath_cart_icon)))
#     cart_icon.click()
    
#     print('\033[92mClicado no ícone do carrinho.\033[0m')
#     sleep(1)# Espera um pouco para o dropdown do carrinho aparecer

# except TimeoutException:
#     print(f'\033[91mTimeout: Ícone do carrinho não encontrado ou não clicável.\033[0m')
# except Exception:
#     print(f'\033[91mErro ao tentar abrir o mini-carrinho\033[0m')




# # - - - CLICANDO EM FINALIZAR PEDIDO (GAMBS kkk) - - - 

# browser.get(f'{url_ecm}/index.php?route=checkout/cart')



# try:
#     delete_icon = espera5.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='col-1 action remove_pc']")))
    
    
#     for dlts in delete_icon[:1]:
#         browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", dlts)
#         sleep(0.4)
#         dlts.click()


# except TimeoutException:
#     print(f'\033[91mTimeout: Ícone de deletar produtos não encontrado ou não clicável.\033[0m')
# except Exception:
#     print(f'\033[91mErro ao tentar deletar um produto\033[0m')




# # - - - Adicionando Produtos no Compre aqui também - - - 

# try:
#     # Seleciona todos os campos da Home onde classe seja Adicionar Produto
#     add_products = espera5.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@class='btn rounded-pill product-adicionar']")))
    
#     # Seleciona 10 produtos para adicionar ao carrinho
#     for prod in add_products[:1]:
#         browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", prod)
#         sleep(3)
#     add_products = espera5.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn rounded-pill product-adicionar']")))
#     add_products.click()



          
# except NoSuchElementException:
#      print('\033[94mCliente não possui Compre aqui Também\033[0m')
# except TimeoutException:
#     print('\033[94mCliente não possui Compre aqui Também\033[0m')



# sleep(1)



# # - - - Escolhendo Retirada - - -

# try:
#     pickup_in_store = espera5.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='custom-radio' and contains(text(), 'Retirar na Loja')]")))
#     browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", pickup_in_store)

#     sleep(1)

#     pickup_in_store.click()
#     sleep(5)
#     finish_buy = browser.find_element(By.ID, 'button_cart_checkout')
#     browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", finish_buy)
#     sleep(2)
#     finish_buy.click()



#     payment_method = browser.find_elements(By.CSS_SELECTOR, "button.nav-link.pane_tab")

#     ids = [button.get_attribute("id") for button in payment_method]      # Extrai os IDs desses botões
#     texts = [button.get_attribute("text") for button in payment_method]   # Extrai os Textos de cada método de entrega

#     paid = 0

#             # - - - FINALIZANDO EM DINHEIRO - - -
#     if "cod2-tab" in ids:
#         payment_money = browser.find_element(By.ID, 'cod2-tab')        
#         browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", payment_money)
#         payment_money.click()
#         print('\033[92mMétodo de pagamento Dinheiro selecioando\033[0m')
#         finish_merch()
#         paid = 1


    
#             # - - - FINALIZANDO CARTÃO NA ENTREGA - - - 
#     elif "cod10-tab" in ids and paid == 0:
#         payment_card = browser.find_element(By.ID, 'cod10-tab') 
#         browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", payment_card)
#         payment_card.click()
#         print('\033[92mMétodo de pagamento Cartão na Entrega selecionado\033[0m')
#         finish_merch()
#         paid = 1

        
#     elif paid == 123123:
#         print('n vou cadastrar cartão do diow agr') ###################################




# except NoSuchElementException:
#     print('Cliente não possui Retirada! Optando por Delivery!')##########################################
#     pickup = 0 ####################################
# except TimeoutException: ##########################################
#     print('Método RETIRADA não encontrado! Optando por Delivery!')##########################################
#     pickup = 0 ##################################



# # Caso não tenha Retirada, vai pra entrega
#     try:
#         delivery = espera5.until(EC.element_to_be_clickable((By.ID, 'button_cart_checkout')))
#         browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", delivery)
    
#         sleep(1)

#         delivery.click()

#         browser.find_element(By.ID, 'input-cep').send_keys('14057100')

#     except:
#         print('oi')

# # Finalizando Pedido




sleep(500)


