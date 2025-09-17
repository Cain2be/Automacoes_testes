from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException as NSEE
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from login import login_ecm
from open_cart import open_cart
from accept_cookies import accept_cookies
from close_popup import close_popup
from buy_also import buy_also
from delete_prod_in_cart import delete_prod_in_cart
from select_prods_in_ecm import add_products
from select_store_in_ecm import select_store_in_ecm
from choose_delivery_method import choose_delivery
from confirm_order import finish_order



#url_ecm = ('https://consuladoracao.com.br/')
url_ecm = ('https://compras.supertecha.com.br/')
#url_ecm = ('https://online.superitalo.com.br/')
browser = webdriver.Chrome() # Abrir o navegador
browser.get(url_ecm)  # Abrir um ecommerce 
browser.maximize_window() # Abre tela cheia



select_store_in_ecm(browser) # NOTE Escolhe a Loja para acessar o E-commerce


close_popup(browser) # NOTE Fecha um Pop-up do e-commerce


login_ecm(browser, url_ecm) # NOTE Loga no E-commerce, caso não tenha cadastro, realiza o cadastro


accept_cookies(browser) # NOTE Aceita Cookies do navegador


add_products(browser) # NOTE Adiciona os Produtos ao carrinho


open_cart(browser) # NOTE Abre o carrinho


delete_prod_in_cart(browser, url_ecm) # NOTE Remove um dos produtos do carrinho


buy_also(browser) # NOTE Utiliza a ferramenta de compra também


choose_delivery(browser) # NOTE Seleciona o método "Retirar na Loja"


finish_order(browser) # NOTE Avança para a tela de pagamento e finaliza o pedido









sleep(500)


