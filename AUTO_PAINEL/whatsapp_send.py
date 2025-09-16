def config_disparo(browser, suffix, phone, whatsapp_send):

    from time import sleep
    from pick_screenhots import screenshots
    from selenium.webdriver.common.alert import Alert
    from datetime import datetime, timedelta
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, WebDriverException


    if whatsapp_send != 1:
        return

    try:
        espera5 = WebDriverWait(browser, 5)

        date_now = datetime.now()

        data_inicio = date_now.strftime('%d-%m-%Y%H:%M')
        data_fim = date_now.strftime('%d-%m-%Y%H:%M')
        hora_inicio = date_now.strftime('%H:%M')
        hora_fim = (date_now + timedelta(minutes=20)).strftime('%H:%M')

        
        # NOTE Acessa menu do WhatsAPP
        espera5.until(EC.element_to_be_clickable((By.XPATH, '//i[contains(@class, "nav-icon far fa-comments")]'))).click()
        espera5.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "nav-link") and .//p[contains(text(), "WhatsApp")]]'))).click()
        espera5.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "nav-link") and .//p[contains(text(), "Disparar Ofertas")]]'))).click()
        print(f'\n✅ Menu WhatsAPP acessado!')



        # NOTE Configura título, phone de destino e mensagem do disparo
        try:
            espera5.until(EC.element_to_be_clickable((By.ID, "message_title"))).send_keys('Teste Disparo')
            espera5.until(EC.element_to_be_clickable((By.XPATH, "//select[@name='stores[]']/option[@value and normalize-space(text()) != '']"))).click()
            print(f'\n✅ Título inserido!')


            espera5.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "emoji-picker-container")]'))).send_keys('Teste Automático de Disparo!')
            print(f'\n✅ Mensagem preenchida!')


            single_phone = browser.find_element(By.ID, 'phone_number')
            browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", single_phone)
            espera5.until(EC.element_to_be_clickable((By.ID, 'phone_number'))).send_keys(phone)
            print(f'\n✅ Número alvo preenchido! {phone}')

        
            
            espera5.until(EC.element_to_be_clickable((By.ID, 'sendIndividual'))).click()
        except:
            print('oi')


        sleep(2)
        

        # NOTE Fecha o Alert de confirmação ou erro do disparo 
        try:
            alert = Alert(browser)  
            alert_text = alert.text
            alert.accept()

        except NoSuchElementException as e:
            print(f'❌ Alerta não encontrado na tela: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'EWHATSAPP_ALERT_ERROR')

        except ElementNotInteractableException as e:
            print(f'❌ Elemento Alerta não interagível: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'WHATSAPP_ALERT_ERROR')

        except TimeoutException as e:
            print(f'❌ Tempo excedido ao esperar Alerta na tela: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'WHATSAPP_ALERT_ERROR')
            
        except WebDriverException as e:
            print(f'❌ Erro no WebDriver ao selecionar Alerta: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'WHATSAPP_ALERT_ERROR')

        except Exception as e:
            print(f'❌ Erro inesperado ao acessar Alerta: {e}') 
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'WHATSAPP_ALERT_ERROR')




        if "Número não cadastrado" in alert_text:
            print(f'Disparo enviado para o número de teste: {phone}')

        else:
            print('envio feito')





    except NoSuchElementException as e:
        print(f'❌ Elemento não encontrado ao gerar cartaz: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_WHATSAPP_SEND')
        
    except ElementNotInteractableException as e:
        print(f'❌ Elemento não interagível ao gerar cartaz: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_WHATSAPP_SEND')

    except TimeoutException as e:
        print(f'❌ Tempo excedido ao gerar cartaz: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_WHATSAPP_SEND')
    
    except WebDriverException as e:
        print(f'❌ Erro no WebDriver ao gerar cartaz: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_WHATSAPP_SEND')
    
    except Exception as e:
        print(f'❌ Erro inesperado ao gerar cartaz: {e}') 
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_WHATSAPP_SEND')



