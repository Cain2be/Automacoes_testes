def add_products(browser, suffix, poster):
    """
    Browser = Navegador que está usando
    Suffix = Sufixo do cliente
    Poster = Se tem cartaz ou não (1 = Sim / 0 = Não)
    """
    
    from pick_screenhots import screenshots
    from time import sleep
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, WebDriverException, ElementClickInterceptedException
    from selenium.webdriver.support.ui import Select




    espera5 = WebDriverWait(browser, 5)


    try:
        nmr_prods = 1
        try:
        # NOTE Acessa aba de produtos
            browser.find_element(By.ID, 'products-tab').click()

            sleep(2)

            espera5.until(EC.element_to_be_clickable((By.ID, 'products-tab'))).click()
            espera5.until(EC.element_to_be_clickable((By.ID, 'search_prod')))

            print(f'\n✅ Menu Produtos selecionado!')

            sleep(1)
        except NoSuchElementException as e:
            print(f'❌ Aba Produtos não encontrada: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_ADD_PRODUCTS_ACESS')

        except ElementNotInteractableException as e:
            print(f'f❌ Aba Produtos não interagível: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_ADD_PRODUCTS_ACESS')

        except TimeoutException as e:
            print(f'❌ Tempo excedido ao esperar aba Produtos: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_ADD_PRODUCTS_ACESS')

        except WebDriverException as e:
            print(f'❌ Erro no WebDriver ao selecionar aba Produtos: {e}')
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_ADD_PRODUCTS_ACESS')

        except Exception as e:
            print(f'❌ Erro inesperado ao acessar aba Produtos: {e}') 
            print(f'Tipo do erro: {type(e).__name__}')
            screenshots(browser, suffix, 'ERROR_ADD_PRODUCTS_ACESS')



        for p in range(0, nmr_prods):
            if p == 0:
                print('🔧 Adicionando produtos...')

            try:
                espera5.until(EC.element_to_be_clickable((By.ID, 'search_prod'))).send_keys('7898')
                espera5.until(EC.element_to_be_clickable((By.XPATH, f"//ul[contains(@class, 'results-container')]//li[{p+1}]"))).click()

                browser.find_element(By.ID, 'strat').click()
                browser.find_element(By.ID, 'select_2').click()
                browser.find_element(By.CLASS_NAME, 'add_prod').click()

            except (ValueError, NoSuchElementException, ElementNotInteractableException, TimeoutException, WebDriverException) as e:
                print(f'❌ Erro ao adicionar produtos: {e}')
                print(f'Tipo do erro: {type(e).__name__}')
                screenshots(browser, suffix, 'ERROR_ADD_PRODUCTS_ADD')
                continue

        # NOTE Ajusta preços
        ppor = browser.find_elements(By.XPATH, "//div[contains(., 'Preço por')]/input")
        

        for i in ppor:
            if i == 0:
                print('🔧 Ajustando preços...')
            ppor_str = i.get_attribute("value").replace(',', '.')
            try:

                ppor_float_atual = float(ppor_str)
                new_value = ppor_float_atual - 0.01
                valor_formatado = f"{new_value:.2f}".replace('.', ',')


                browser.execute_script("""
                    arguments[0].value = arguments[1];
                    arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
                """, i, valor_formatado)


            except (ValueError, NoSuchElementException, ElementNotInteractableException, TimeoutException, WebDriverException) as e:
                print(f'❌ Erro ao ajustar preço: {e}')
                print(f'Tipo do erro: {type(e).__name__}')
                screenshots(browser, suffix, 'ERROR_ADD_PRODUCTS_PRICE')
                continue



        # NOTE Ajusta limites
        limit = browser.find_elements(By.XPATH, "//div[contains(., 'Limite')]/input")

        for id, i in enumerate(limit):
            if id == 0:
                print('🔧 Ajustando Limites...')
            limit_str = i.get_attribute("value")
            
            try:
                atual_limit = int(limit_str)
                new_limit = atual_limit + (id + 1)
                i.clear()
                i.send_keys(str(new_limit))

            except (ValueError, NoSuchElementException, ElementNotInteractableException, TimeoutException, WebDriverException) as e:
                print(f'❌ Erro ao ajustar limites: {e}')
                print(f'Tipo do erro: {type(e).__name__}')
                screenshots(browser, suffix, 'ERROR_ADD_PRODUCTS_PRICE')



        # NOTE Ajusta cartaz se necessário
        xpath_select_cartaz = "//select[contains(@class, 'form-control') and contains(@class, 'input-poster')]"
        select_elements_cartaz = espera5.until(EC.presence_of_all_elements_located((By.XPATH, xpath_select_cartaz)))

        if poster == 1:
            print('🔧 Cartaz Identificado! Configurando...')
            try:
                xpath_select_cartaz = "//select[contains(@class, 'form-control') and contains(@class, 'input-poster')]"
                select_elements_cartaz = espera5.until(EC.presence_of_all_elements_located((By.XPATH, xpath_select_cartaz)))
                
                for select_element in select_elements_cartaz:
                    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", select_element)
                    Select(select_element).select_by_value("a4")

            except (ValueError, NoSuchElementException, ElementNotInteractableException, TimeoutException, WebDriverException) as e:
                print(f'❌ Erro ao configurar tamanho do cartaz: {e}')
                print(f'Tipo do erro: {type(e).__name__}')
                screenshots(browser, suffix, 'ERROR_ADD_PRODUCTS_SIZE')
                    


        # NOTE Tira screenshot com zoom
        try:
            browser.execute_script('document.body.style.zoom="67%"')
            screenshots(browser, suffix, 'products')
            sleep(1)
            browser.execute_script('document.body.style.zoom="100%"')
        except (ValueError, NoSuchElementException, ElementNotInteractableException, TimeoutException, WebDriverException) as e:
            print(f'❌ Erro ao tirar print da aba Produtos: {e}')
    


    except NoSuchElementException as e:
        print(f'❌ Elemento não encontrado ao configurar produtos: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_ADD_PRODUCTS')

    except ElementNotInteractableException as e:
        print(f'❌ Elemento não interagível ao configurar produtos: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_ADD_PRODUCTS')

    except TimeoutException as e:
        print(f'❌ Tempo excedido ao esperar elemento ao configurar produtos: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_ADD_PRODUCTS')

    except WebDriverException as e:
        print(f'❌ Erro no WebDriver ao configurar produtos: {e}')
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_ADD_PRODUCTS')

    except Exception as e:
        print(f'❌ Erro inesperado ao configurar produtos: {e}') 
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_ADD_PRODUCTS')

