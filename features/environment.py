import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def before_scenario(context, scenario):
    # Crea una directory temporanea unica per ogni esecuzione
    temp_dir = tempfile.mkdtemp()

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument(f"--user-data-dir={temp_dir}")  # Usa una directory unica per i dati utente

    # Usa webdriver-manager per ottenere automaticamente il ChromeDriver
    service = Service(ChromeDriverManager().install())

    # Inizializza il driver
    context.driver = webdriver.Chrome(service=service, options=chrome_options)

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
