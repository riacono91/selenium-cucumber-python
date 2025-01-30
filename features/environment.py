from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Rimuovi --user-data-dir per evitare conflitti nella directory dei dati utente
    # chrome_options.add_argument(f"--user-data-dir={temp_dir}")  # Non necessario

    # Usa webdriver-manager per ottenere automaticamente il ChromeDriver
    service = Service(ChromeDriverManager().install())

    # Inizializza il driver
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    # Stampa le versioni di Chrome e ChromeDriver per debug
    print("Chrome Version:", context.driver.capabilities['browserVersion'])
    print("ChromeDriver Version:", context.driver.capabilities['chrome']['chromedriverVersion'])


def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
