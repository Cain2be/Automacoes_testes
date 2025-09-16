def config_app(browser, suffix, app, ecommerce):
    """
    Browser = Navegador que está usando
    APP = 1 Se quiser criar oferta para o APP, 0 caso não queira
    ECOMMERCE = 1 Se quiser criar jornal, 0 caso não queira
    """



    from time import sleep
    from pick_screenhots import screenshots
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from datetime import datetime, timedelta
    from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, WebDriverException, ElementClickInterceptedException




    espera5 = WebDriverWait(browser, 5)

    if app != 1:
        return  # Sai se o app não estiver ativado

    try:

        date_now = datetime.now()

        data_inicio = date_now.strftime('%d-%m-%Y')
        data_fim = date_now.strftime('%d-%m-%Y')
        hora_inicio = date_now.strftime('%H:%M')
        hora_fim = (date_now + timedelta(minutes=20)).strftime('%H:%M')


        # NOTE Acessa aba do APP
        espera5.until(EC.element_to_be_clickable((By.ID, 'app-tab'))).click()
        print(f'\n✅ Menu APP acessado!')



        # NOTE Ativa botão de ativação
        espera5.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="switchActivateButton"]'))).click()
        print('🔧 App ativado')


        # NOTE Se ecommerce estiver ativado, ativa o botão do carrinho
        if ecommerce == 1:
            espera5.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="switchCartButton"]'))).click()
            print('🛒 Carrinho ativado')
            


        # NOTE Seleciona "Home" na posição de exibição
        espera5.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(@class, "select2-selection__rendered") and contains(text(), "Home")]')))
        print('🏠 Página Home selecionada')


        # NOTE Clica no botão de pré-visualização
        espera5.until(EC.element_to_be_clickable((By.ID, 'previewApp'))).click()


        # NOTE Espera o overlay de visualização aparecer
        espera5.until(EC.visibility_of_element_located((By.ID, 'canvas-overlay-app')))
        print('✅ App configurado com sucesso!')

        sleep(2)

        # NOTE Tira screenshot com zoom

        screenshots(browser, suffix, 'app_config')


    except NoSuchElementException as e:
        print(f'❌ Elemento não encontrado ao configurar aba APP: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_APP')

    except ElementClickInterceptedException as e:
        print(f'❌ Elemento foi interceptado por outro ao configurar aba APP: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_APP')

    except ElementNotInteractableException as e:
        print(f'❌ Elemento não interagível ao configurar aba APP: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_APP')

    except TimeoutException as e:
        print(f'❌ Tempo excedido esperando elemento ao configurar aba APP: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_APP')

    except WebDriverException as e:
        print(f'❌ Erro no WebDriver ao configurar aba APP: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_APP')

    except Exception as e:
        print(f'❌ Erro inesperado ao configurar aba APP: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_APP')