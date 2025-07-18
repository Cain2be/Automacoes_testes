def login(browser, suffix):
    """
    Browser = Inserir nome da variável do navegador que está sendo utilizado
    Suffix = Sufixo do cliente
    """

    from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, WebDriverException
    from selenium.webdriver.common.by import By


    try:
        browser.find_element(By.ID, 'username').send_keys(f'{suffix}_big2be')
        browser.find_element(By.ID, 'password').send_keys(f'#Big#2$be@{suffix}@@')
        browser.find_element(By.XPATH, '//input[@type = "submit"]').click()
        print('\n✅ Login realizado com Sucesso')

    except NoSuchElementException:
        print('❌ Erro: Campo de login ou senha não encontrado')

    except ElementNotInteractableException:
        print('❌ Erro: Campo de login ou botão de envio não interagível')

    except TimeoutException:
        print('❌ Erro: Tempo excedido ao esperar o elemento de login')

    except WebDriverException as e:
        print(f'❌ Erro no WebDriver{login}: {e}')

    except Exception as e:
        print(f'❌ Erro inesperado: {e}')