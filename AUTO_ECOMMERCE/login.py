from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def login_ecm (browser, url_ecm):

    espera5 = WebDriverWait(browser, 5)
    sub_text_login_element = browser.find_element(By.TAG_NAME, 'sub') # Verifica qual o texto do Login
    sub_text_login = sub_text_login_element.text.strip()
    
    if "Entre" in sub_text_login: # Se o Login não foi feito (Em baixo do Minha Conta está escrito ENTRE)
    
        browser.get(f'{url_ecm}//index.php?route=account/login') # Vai pra tela de login

        espera5.until(EC.element_to_be_clickable((By.ID, 'input-email'))).send_keys('45951270812') # Digita email
        browser.find_element(By.ID, 'input-password').send_keys('++big2be##') # Digita a senha
        espera5.until(EC.element_to_be_clickable((By.NAME, 'login'))).click() # Clica em Continuar

        sleep(0.5)
    
    try:
        alerta = espera5.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "alert-danger")]')))
    
        print('\033[91mCadastro não encontrado! Redirecionando...\033[0m')
        browser.get(f'{url_ecm}/index.php?route=account/register')        



        espera5.until(EC.element_to_be_clickable((By.ID, 'input-custom-field1')))  # Espera primeiro campo ser clicável
        browser.find_element(By.ID, 'input-custom-field1').send_keys('45951270812') # Insere CPF
        browser.find_element(By.ID, 'input-firstname').send_keys('Caio') # Insere Nome
        browser.find_element(By.ID, 'input-lastname').send_keys('Stabile') # Insere Sobrenome
        browser.find_element(By.ID, 'input-email').send_keys('caio.bstabile@hotmail.com') # Insere Email
        browser.find_element(By.ID, 'input-telephone').send_keys('16982660505') # Insere Telefone
        browser.find_element(By.ID, 'input-password').send_keys('123teste123') # Insere Senha
        browser.find_element(By.ID, 'input-confirm').send_keys('123teste123') # Insere Confirmação de Senha
           
        nao_radio = espera5.until(  # Aguarda até a opção "não" estar visível
            EC.presence_of_element_located((By.XPATH, '//input[@name="newsletter" and @value="0"]'))
            )  
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'})", nao_radio)  # Scroll até enxergar  
        browser.execute_script("arguments[0].click();", nao_radio) # Força o click na opção Não, evitando sobreposição
        sleep(0.3)


        try:
            privacy_policy = browser.find_element(By.NAME, 'agree').click() # Se o ecommerce tiver o botão de Aceitar Política de Privacidade, aceita e segue
            sleep(0.3)
        except:
            pass

            # Clica em Continuar
        browser.find_element(By.NAME, 'login').click()

        print('\033[92mCadastro Realizado!\033[0m')



    except:
       print('\033[92mLogin completo\033[0m')