def screenshots(browser, suffix, service):
    """
    Browser = Inserir nome da variável do navegador que está sendo utilizado
    Suffix = Sufixo do cliente
    Service = Qual serviço está sendo registrado
    """


    from datetime import datetime
    import os


    """Salva screenshots em diretórios organizados por data"""
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)

    date = datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.now().strftime("%H-%M-%S")
    test_dir = os.path.join(screenshots_dir, f"{suffix}_{date}")
    os.makedirs(test_dir, exist_ok=True)

    filename = os.path.join(test_dir, f"{service}_{timestamp}.png")
    
    try:
        browser.save_screenshot(filename)
        print(f"✅ Screenshot salvo em: {filename}")
    except Exception as e:
        print(f"❌ Falha ao salvar screenshot: {e}")