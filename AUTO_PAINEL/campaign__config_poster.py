def config_poster(browser, suffix, poster):
    
    import os
    from pick_screenhots import screenshots
    from time import sleep
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, WebDriverException
    from selenium.webdriver.common.action_chains import ActionChains


    espera5 = WebDriverWait(browser, 5)
    espera30 = WebDriverWait(browser, 30)

    try:
        actual_window = browser.current_window_handle # NOTE Guarda a janela principal

        if poster == 1:

            # NOTE Acessa a aba "Cartaz"
            poster_tab = espera5.until(EC.element_to_be_clickable((By.ID, 'poster-tab')))
            browser.execute_script("arguments[0].scrollIntoView({block: 'center'})", poster_tab)
            poster_tab.click()
            print(f"\n✅ Aba selecionada: Cartaz")
            sleep(1.5)


            # NOTE Seleciona formato A4
            print('🔧 Configurando Formato Cartaz...')
            browser.find_element(By.ID, 'a4_qty').click() 

            sleep(1.5)

            # NOTE Abre dropdown de quantidade de produtos por cartaz
            print('🔧 Configurando Quantidade de Produtos por Cartaz...')
            acoes = ActionChains(browser)
            elemento = browser.find_element(By.ID, 'select2-perpagePoster-container')
            acoes.click_and_hold(elemento).perform()
            
            sleep(0.5)


            try:
                # NOTE Aguarda e clica na opção "2"
                xpath_select_prod_per_poster = "//li[@class='select2-results__option' and normalize-space(.) = '2']"
                #select_elements_poster = espera5.until(EC.presence_of_all_elements_located((By.XPATH, xpath_select_prod_per_poster)))
                select_element_to_click = espera5.until(EC.element_to_be_clickable((By.XPATH, xpath_select_prod_per_poster)))
                select_element_to_click.click() # td isso pra clicar no 2 nas opções
            


            except Exception as e:
                print(f'❌ Erro ao selecionar quantidade de produtos por cartaz: {e}')
                print(f'Tipo do erro: {type(e).__name__}')
                screenshots(browser, suffix, 'ERROR_POSTER_QTY_PROD')
                


            # NOTE Clica no botão de imprimir
            print('🔧 Imprimindo Cartaz...')
            sleep(1.5)
            browser.find_element(By.ID, 'printPoster').click()
            browser.find_element(By.XPATH, "//button[@class = 'btn btn-outline-primary m-1']").click()
            

            # NOTE Espera a nova aba abrir (evita sleep fixo)
            espera30.until(lambda d: len(d.window_handles) > 1)

            all_windows = browser.window_handles

            if len(all_windows) > 1:
                sleep(8)
                try:
                    print('\033[094mMudando para aba secundária')
                    browser.switch_to.window(all_windows[1])
                    print('\033[094mTirando screenshot do poster')
                    screenshots(browser, suffix, 'poster')

                    print('\033[094mVoltando para aba principal')
                    browser.switch_to.window(actual_window)
                    
                    
                except Exception as e:
                    print(f'Erro ao manipular abas: {str(e)}')
                    # NOTE Tentativa de garantir que voltamos para a janela principal
                    try:
                        browser.switch_to.window(actual_window)
                    except:
                        print(f'❌ Falha ao retornar para a janela principal: {e}')



    except NoSuchElementException as e:
        print(f'❌ Elemento não encontrado ao gerar cartaz: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_POSTER')
        
    except ElementNotInteractableException as e:
        print(f'❌ Elemento não interagível ao gerar cartaz: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_POSTER')

    except TimeoutException as e:
        print(f'❌ Tempo excedido ao gerar cartaz: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_POSTER')
    
    except WebDriverException as e:
        print(f'❌ Erro no WebDriver ao gerar cartaz: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_POSTER')
    
    except Exception as e:
        print(f'❌ Erro inesperado ao gerar cartaz: {e}') 
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_POSTER')