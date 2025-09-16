def config_whatsapp(browser, suffix, whatsapp):

    from pick_screenhots import screenshots
    from datetime import datetime
    from time import sleep
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, WebDriverException
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.common.keys import Keys



    espera5 = WebDriverWait(browser, 5)

    try:
        if whatsapp == 1:


            date_now = datetime.now()
            data_inicio = date_now.strftime("%d%m%Y")
            hora_inicio = date_now.strftime("%H%M")
            
            
            try:

                whats_tab = browser.find_element(By.ID, 'whatsapp-tab')
                browser.execute_script("arguments[0].scrollIntoView({block: 'center'})", whats_tab)
                espera5.until(EC.element_to_be_clickable(whats_tab))
                whats_tab.click()

                print(f"\n✅ Aba selecionada: WhatsAPP")
            
            except TimeoutException as e:
                print(f'❌ Erro ao selecionar Aba WhatsAPP!: {e}')
                print(f'Tipo do erro: {type(e).__name__}')
                screenshots(browser, suffix, 'ERROR_WHATSAPP_ACESS')
                return

            except Exception as e:
                print(f'❌ Erro inesperado ao selecionar Aba WhatsAPP1: {e}') 
                print(f'Tipo do erro: {type(e).__name__}')
                screenshots(browser, suffix, 'ERROR_WHATSAPP_ACESS')
                return

            except NoSuchElementException as e:
                print(f'❌ Elemento não encontrado (Aba WhatsAPP): {e}')
                print(f'Tipo do erro: {type(e).__name__}')
                screenshots(browser, suffix, 'ERROR_WHATSAPP_ACESS')
                return

            except WebDriverException as e:
                print(f'❌ Erro no WebDriver ao selecionar Aba WhatsAPP: {e}')
                print(f'Tipo do erro: {type(e).__name__}')
                screenshots(browser, suffix, 'ERROR_WHATSAPP_ACESS')
                return
            



            sleep(0.2)


            try:
                print('🔧 Configurando Disparo...')
                espera5.until(EC.element_to_be_clickable((
                    By.XPATH, '//input[@class="form-control" and @name="title_whatsapp"]'))
                    ).send_keys('teste')

                sleep(0.2)

                espera5.until(EC.element_to_be_clickable((
                    By.XPATH, '//input[@class="form-control" and @name="date_whatsapp"]'))
                    ).send_keys(data_inicio, Keys.TAB, hora_inicio)

                sleep(0.2)

                select_element = browser.find_element("xpath", "//select[@name='transmission_whatsapp']")
                select = Select(select_element)
                select.select_by_value("20")

                espera5.until(EC.element_to_be_clickable((
                    By.XPATH, '//textarea[@class="form-control" and @name="message_whatsapp"]'))
                    ).send_keys('Teste de disparo WhatsAPP')

                screenshots(browser, suffix, 'config_whatsapp')
                sleep(1)

                print(f"✅ Configurações dos disparos preenchidas com sucesso!")


            except TimeoutException as e:
                print(f'❌ Erro ao preencher dados do disparo!: {e}')
                print(f'Tipo do erro: {type(e).__name__}')
                screenshots(browser, suffix, 'ERROR_WHATSAPP_DATA')
                
            except Exception as e:
                print(f'❌ Erro inesperado ao preencher dados do disparo: {e}') 
                print(f'Tipo do erro: {type(e).__name__}')
                screenshots(browser, suffix, 'ERROR_WHATSAPP_DATA')
                
            except NoSuchElementException as e:
                print(f'❌ Elemento não encontrado (Campo de preenchimento dados do disparo): {e}')
                print(f'Tipo do erro: {type(e).__name__}')
                screenshots(browser, suffix, 'ERROR_WHATSAPP_DATA')

            except WebDriverException as e:
                print(f'❌ Erro no WebDriver ao preencher dados do disparo: {e}')
                print(f'Tipo do erro: {type(e).__name__}')
                screenshots(browser, suffix, 'ERROR_WHATSAPP_DATA')




    except NoSuchElementException as e:
        print(f'❌ Elemento não encontrado: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_WHATSAPP')

    except ElementNotInteractableException as e:
        print(f'❌ Elemento não interagível: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_WHATSAPP')

    except TimeoutException as e:
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_WHATSAPP')
        print(f'❌ Tempo excedido ao esperar elemento: {e}')

    except WebDriverException as e:
        print(f'❌ Erro no WebDriver: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_WHATSAPP')        

    except Exception as e:
        print(f'❌ Erro inesperado: {e}') 
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_WHATSAPP')
