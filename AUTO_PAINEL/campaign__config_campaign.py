def config_campaign(browser, suffix, app = 1, whatsapp = 1, journal = 1, poster = 1, ecommerce = 1, email = 1):
    """
    Browser = Inserir nome da variável do navegador que está sendo utilizado
    APP = 1 Se quiser criar oferta para o APP, 0 caso não queira
    WHATSAPP: 1 Se quiser criar disparo para o WPP, 0 caso não queira
    JOURNAL = 1 Se quiser criar jornal, 0 caso não queira
    POSTER = 1 Se quiser criar jornal, 0 caso não queira
    ECOMMERCE = 1 Se quiser criar jornal, 0 caso não queira
    EMAIL = 1 Se quiser criar jornal, 0 caso não queira
    """



    from time import sleep
    from pick_screenhots import screenshots
    from datetime import datetime, timedelta
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, WebDriverException


    
    espera5 = WebDriverWait(browser, 5)


    try:
        date_now = datetime.now()

        data_inicio = date_now.strftime('%d-%m-%Y')
        data_fim = date_now.strftime('%d-%m-%Y')
        hora_inicio = date_now.strftime('%H:%M')
        hora_fim = (date_now + timedelta(minutes=20)).strftime('%H:%M')

        # NOTE Acessa menu da campanha
        try:
            espera5.until(EC.element_to_be_clickable((By.XPATH, '//i[contains(@class, "nav-icon fas fa-fire")]'))).click()
            espera5.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "nav-link") and .//p[contains(text(), "Campanha Rápida")]]'))).click()
            print(f'\n✅ Menu Campanha Rápida acessado!')

        except NoSuchElementException as e:
            print(f'❌ Elemento Campanha Rápida não encontrado: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_ACESS')

        except ElementNotInteractableException as e:
            print(f'❌ Elemento Campanha Rápida não interagível: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_ACESS')

        except TimeoutException as e:
            print(f'❌ Tempo excedido ao esperar elemento Campanha Rápida: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_ACESS')
            
        except WebDriverException as e:
            print(f'❌ Erro no WebDriver ao selecionar Campanha Rápida: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_ACESS')

        except Exception as e:
            print(f'❌ Erro inesperado ao acessar Campanha Rápida: {e}') 
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_ACESS')

        try:
            espera5.until(EC.element_to_be_clickable((By.ID, 'btn_new_campaign'))).click()

        except NoSuchElementException as e:
            print(f'❌ Botão de Nova Campanha não encontrado: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_ACESS')

        except ElementNotInteractableException as e:
            print(f'❌ Elemento Nova Campanha não interagível: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_ACESS')

        except TimeoutException as e:
            print(f'❌ Tempo excedido ao esperar elemento Nova Campanha: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_ACESS')
            
        except WebDriverException as e:
            print(f'❌ Erro no WebDriver ao selecionar Nova Campanha: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_ACESS')

        except Exception as e:
            print(f'❌ Erro inesperado ao acessar Nova Campanha: {e}') 
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_ACESS')


        # NOTE Preenche dados da campanha
        try:
            espera5.until(EC.element_to_be_clickable((By.ID, 'description'))).send_keys('Teste Auto')
            browser.find_element(By.ID, 'date_begin').send_keys(f'{data_inicio}')
            browser.find_element(By.ID, 'date_end').send_keys(f'{data_fim}')
            # browser.find_element(By.ID, 'time_begin').send_keys(f'{hora_inicio}')
            # browser.find_element(By.ID, 'time_end').send_keys(f'{hora_fim}')
            print(f'✅ Dados da campanha preenchidos!')
        
        except NoSuchElementException as e:
            print(f'❌ Erro ao preencher dados da campanha: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_DATA')

        except ElementNotInteractableException as e:
            print(f'❌ Dados da campanha não interagíveis: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_DATA')

        except TimeoutException as e:
            print(f'❌ Tempo excedido ao esperar Descrição da Campanha: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_DATA')

        except WebDriverException as e:
            print(f'❌ Erro no WebDriver ao preencher dados da campanha: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_DATA')
            
        except Exception as e:
            print(f'❌ Erro inesperado ao acessar preencher dados da campanha: {e}') 
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_DATA')



        # NOTE Ativa e desativa oferta geral (padrão do sistema)
        try:
            browser.find_element(By.XPATH, "//label[@for='switchGeneralOffer']").click() 
            sleep(0.3)
            browser.find_element(By.XPATH, "//label[@for='switchGeneralOffer']").click() 
            sleep(0.3)
            

        # NOTE Remove e adiciona loja
            browser.find_element(By.XPATH, '//*[@class = "select2-selection__choice__remove"]').click()
            sleep(0.3)
            browser.find_element(By.CLASS_NAME, 'select2-results__option').click()
        
        
        except NoSuchElementException as e:
            print(f'❌ Erro ao finalizar configurações da campanha: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_DATA')

        except ElementNotInteractableException as e:
            print(f'❌ Dados finais da campanha não interagíveis: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_DATA')

        except WebDriverException as e:
            print(f'❌ Erro no WebDriver ao finalizar configuração da campanha: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_DATA')

        except Exception as e:
            print(f'❌ Erro inesperado ao terminar de preencher dados da campanha: {e}') 
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_CAMPAIGN_DATA')
        
        # NOTE Ativa ferramentas de acordo com a seleção no topo do código
        ferramentas = {
        'switchApp': app,
        'switchWhatsapp': whatsapp,
        'switchJournal': journal,
        'switchPoster': poster,
        'switchEcommerce': ecommerce,
        'switchEmail': email,}

        
        for nome, ativo in ferramentas.items():
            if ativo == 1:
                browser.find_element(By.XPATH, f'//label[@for= "{nome}"]').click()

                # print(f'✅ Ferramenta ativada: {nome}')

                # Encontra o elemento checkbox
                checkbox = browser.find_element(By.ID, f'{nome}')
                # Verifica se o atributo "disabled" existe
                is_disabled = checkbox.get_attribute("disabled") is not None
                is_checked = checkbox.is_selected()
                if not is_disabled and is_checked:
                    print(f"✅ Ferramenta ativada: {nome}")
                else:
                    print(f"❌ Ferramenta não está ativado ou está desabilitado: {nome}")
            
    except NoSuchElementException as e:
        print(f'❌ Elemento não encontrado (GERAL): {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_CAMPAIGN')

    except ElementNotInteractableException as e:
        print(f'❌ Elemento não interagível (GERAL): {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_CAMPAIGN')

    except TimeoutException as e:
        print(f'❌ Tempo excedido ao esperar elemento (GERAL): {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_CAMPAIGN')

    except WebDriverException as e:
        print(f'❌ Erro no WebDriver:{config_campaign} {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_CAMPAIGN')

    except Exception as e:
        print(f'❌ Erro inesperado (GERAL): {e}') 
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_CAMPAIGN')
        