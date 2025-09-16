def config_notification(browser, suffix, cpf, notification_send):

    from time import sleep, time
    from pick_screenhots import screenshots
    from selenium.webdriver.common.alert import Alert
    from datetime import datetime, timedelta
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, WebDriverException
    import os


    if notification_send != 1:
        return

    try:
        espera5 = WebDriverWait(browser, 5)

        date_now = datetime.now()

        data_inicio = date_now.strftime('%d-%m-%Y%H:%M')
        data_fim = (date_now + timedelta (minutes=10)).strftime('%d-%m-%Y%H:%M')
        


        try:
            # NOTE Acessa menu de Notificações
            espera5.until(EC.element_to_be_clickable((By.XPATH, '//i[contains(@class, "nav-icon far fa-comments")]'))).click()
            espera5.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "nav-link") and .//p[contains(text(), "Notificações")]]'))).click()
            print(f'\n✅ Menu Notificações acessado!')
        

        except NoSuchElementException as e:
            print(f'❌ Elemento Notificações não encontrado: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_NOTIFICATION_ACESS')

        except ElementNotInteractableException as e:
            print(f'❌ Elemento Notificações não interagível: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_NOTIFICATION_ACESS')

        except TimeoutException as e:
            print(f'❌ Tempo excedido ao esperar elemento Notificações: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_NOTIFICATION_ACESS')
            
        except WebDriverException as e:
            print(f'❌ Erro no WebDriver ao selecionar Notificações: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_NOTIFICATION_ACESS')

        except Exception as e:
            print(f'❌ Erro inesperado ao acessar Notificações: {e}') 
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_NOTIFICATION_ACESS')



        
        # NOTE Configura o disparo de notificação (COM JS POR SER UM INPUT DE PLUGIN DE EMOJIS)
        notif_title_message = browser.find_elements(By.CSS_SELECTOR, "div.emoji-wysiwyg-editor[contenteditable='true']")
        browser.execute_script("arguments[0].innerText = 'Teste de título automático';", notif_title_message[0])
        browser.execute_script("arguments[0].innerText = 'Teste mensagem automática';", notif_title_message[1])
        notif_title_message[0].click()
        notif_title_message[1].click()
        print(f'\n✅ Título e Mensagem Inseridos!')

        # NOTE Configura data e hora do disparo (10 minutos pra frente de agora)
        espera5.until(EC.element_to_be_clickable((By.ID, 'date_send'))).send_keys(data_inicio)
        espera5.until(EC.element_to_be_clickable((By.ID, 'date_end'))).send_keys(data_fim)



        # Caminho da imagem no mesmo diretório do script
        caminho_absoluto = os.path.abspath("testenotif.png")

        # Localiza o input do tipo file
        campo_upload = browser.find_element(By.ID, "imageInput")

        # Envia o caminho da imagem diretamente
        campo_upload.send_keys(caminho_absoluto)
        print(f'\n✅ Imagem anexada na Notificação!')
        
        sleep(2)

        espera5.until(EC.element_to_be_clickable((By.ID, 'removeBtn'))).click()
        print(f'\n✅ Imagem Removida (Teste botão excluir)!')
        sleep(2)

        campo_upload.send_keys(caminho_absoluto)
        print(f'\n✅ Imagem adicionada novamente!')
        

        # NOTE Preenche o campo CPF com o configurado no header da main
        espera5.until(EC.element_to_be_clickable((By.ID, 'cpf'))).send_keys(f'{cpf}')
        print(f'\n✅ CPF alvo preenchido! {cpf}')



        # NOTE Centraliza o campo de upload de imagem na tela para não haver problema nos cliques 
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'})", campo_upload)
        sleep(0.8)

        browser.execute_script('document.body.style.zoom="67%"')
        sleep(1)

        screenshots(browser, suffix, 'notification')

        browser.execute_script('document.body.style.zoom="100%"')
        print(f"✅ Notificação configurada com sucesso")

        # NOTE Centraliza e clica no botão de enviar notificação
        send_button = browser.find_element(By.CSS_SELECTOR, 'button[name="submit_btn"]')    
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", send_button)
        send_button.click()
        espera5.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.swal2-confirm.swal2-styled'))).click()


    except NoSuchElementException as e:
        print(f'❌ Elemento não encontrado (GERAL): {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_CONFIG_NOTIFICATION')

    except ElementNotInteractableException as e:
        print(f'❌ Elemento não interagível (GERAL): {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_CONFIG_NOTIFICATION')

    except TimeoutException as e:
        print(f'❌ Tempo excedido ao esperar elemento (GERAL): {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_CONFIG_NOTIFICATION')

    except WebDriverException as e:
        print(f'❌ Erro no WebDriver:{config_notification} {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_CONFIG_NOTIFICATION')

    except Exception as e:
        print(f'❌ Erro inesperado (GERAL): {e}') 
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_CONFIG_NOTIFICATION')
