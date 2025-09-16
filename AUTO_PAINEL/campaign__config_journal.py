def config_journal(browser, suffix, journal):

    from pick_screenhots import screenshots
    from time import sleep
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, WebDriverException


    espera5 = WebDriverWait(browser, 5)


    if journal != 1:
        return
    

    try:
        attempt = 1
        browser.find_element(By.ID, 'journal-tab').click()
        espera5.until(EC.element_to_be_clickable((By.XPATH, '//label[@for= "consider_pagination"]'))).click()
        print(f'\n✅ Menu Jornal acessado!')


        while True:
            try:
                preview = browser.find_element(By.ID, 'canvas-overlay-journal-1')
                if preview.is_displayed():
                    print('✅ Preview Gerado!')
                    break
            except NoSuchElementException:
                pass
            except Exception as e:
                print(f"❌ Erro ao verificar preview: {e}")
                print(f'Tipo do erro: {type(e).__name__}')
                screenshots(browser, suffix, 'ERROR_JOURNAL_PREVIEW')

            try:
                print('🔧 Configurando Área do Jornal...')
                browser.find_element(By.XPATH, '//a[@class = "btn btn-block btn-primary addArea"]').click()

                h = browser.find_element(By.ID, f'journal_margin_h-1-{attempt}')
                v = browser.find_element(By.ID, f'journal_margin_v-1-{attempt}')
                h.clear()
                h.send_keys('0')
                v.clear()
                v.send_keys('0')

                a = browser.find_element(By.ID, f'journal_row-1-{attempt}')
                l = browser.find_element(By.ID, f'journal_col-1-{attempt}')
                a.clear()
                a.send_keys('2')
                l.clear()
                l.send_keys('4')

                browser.find_element(By.XPATH, '//a[@class = "btn btn-block btn-primary previewJournal"]').click()

                sleep(2)

                attempt += 1
                sleep(1)
            except (NoSuchElementException, ElementNotInteractableException) as e:
                print(f"❌ Erro ao adicionar área: {e}")
                print(f'Tipo do erro: {type(e).__name__}')
                screenshots(browser, suffix, 'ERROR_JOURNAL_DATA')
                break
            except Exception as e:
                print(f"❌ Erro inesperado ao configurar jornal: {e}")
                print(f'Tipo do erro: {type(e).__name__}')
                screenshots(browser, suffix, 'ERROR_JOURNAL_DATA')
                break


        sleep(7)

        browser.execute_script("arguments[0].scrollIntoView({block: 'center'})", preview)
        sleep(0.8)

        browser.execute_script('document.body.style.zoom="67%"')
        sleep(3)

        screenshots(browser, suffix, 'journal')

        browser.execute_script('document.body.style.zoom="100%"')
        print(f"✅ Jornal configurado com sucesso")

    except TimeoutException as e:
        print(f"❌ Timeout ao configurar jornal: {e}")
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_JOURNAL')

    except WebDriverException as e:
        print(f"❌ Erro de WebDriver ao configurar jornal: {e}")
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_JOURNAL')

    except Exception as e:
        print(f"❌ Erro inesperado ao configurar jornal: {e}")   
        print(f'Tipo do erro: {type(e).__name__}')
        screenshots(browser, suffix, 'ERROR_JOURNAL')