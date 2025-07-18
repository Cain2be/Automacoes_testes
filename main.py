from logger__config import log_config
from logar__painel import login
from adicionar__produtos import add_products
from campaign__config_campaign import config_campaign
from campaign__config_app import config_app
from campaign__config_journal import config_journal
from campaign__config_poster import config_poster
from campaign__config_whatsapp import config_whatsapp
from notification_send import config_notification
from whatsapp_send import config_disparo
from time import sleep, time
import sys
import atexit
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait





# SECTION - Serviços a serem testados: (1 = SIM / 0 = NÃO) 
suffix = 'techa'
app = 0
whatsapp = 0
journal = 0
poster = 0
ecommerce= 0
email = 0
cpf = '45951270812'
phone = '5516982660505'



# SECTION - Execução do navegador
browser = webdriver.Chrome() # Abrir o navegador
espera5 = WebDriverWait(browser, 5)
browser.get(f'https://cliente.big2be.com/login/{suffix}')  # Abrir um painel
browser.maximize_window() # Abre tela cheia



def safe_close():
    if hasattr(sys.stdout, 'close'):
        sys.stdout.close()

atexit.register(safe_close)



try:

    log_config(suffix) # NOTE Abre o Log


    login(browser, suffix)  # NOTE Loga no painel
    

    config_campaign(browser, suffix, app, whatsapp, journal, poster, ecommerce, email) # NOTE Configura Informações (Título, datas, unidades válidas e serviços que serão adicionados)


    add_products(browser, suffix, poster) # NOTE Adiciona os produtos na campanha 


    config_app(browser, suffix, app, ecommerce) # NOTE Configura aba APP


    config_journal(browser, suffix, journal) # NOTE Configura aba Jornal


    config_whatsapp(browser, suffix, whatsapp) # NOTE Configura aba WhatsAPP 


    config_poster(browser, suffix, poster) # NOTE Configura aba Cartaz


    config_disparo(browser, suffix, phone) # NOTE Configura Disparo no WhatsAPP
    

    config_notification(browser, suffix, cpf) # NOTE Configura disparo de Notificação

finally:
    safe_close()
    print('✅ Arquivo de log fechado com sucesso!')


print('SISTEMA FINALIZADO, LOG GRAVADO')



sleep(500)