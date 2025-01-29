from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
def before_scenario(context, scenario):
    pass  # Configurazioni opzionali prima degli scenari
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service('./chromedriver.exe')  # Percorso relativo nella directory del progetto

    # Inizializza il driver
    context.driver = webdriver.Chrome(service=service, options=chrome_options)

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()

#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
#
# def before_all(context):
#     # Configura il driver di Chrome
#     chrome_options = Options()
#     # Non impostare 'headless' per vedere il browser
#     # chrome_options.add_argument("--headless")  # Commenta questa riga se presente
#     chrome_options.add_argument("--start-maximized")  # Massimizza la finestra
#
#     # Indica il percorso al tuo ChromeDriver
#     context.driver = webdriver.Chrome(service=Service('./chromedriver'), options=chrome_options)
#
# def after_all(context):
#     # Chiudi il browser dopo i test
#     context.driver.quit()
