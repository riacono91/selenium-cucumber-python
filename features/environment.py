from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):
    print(">>> DEBUG: Entrato in before_scenario")

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless=new")  # Esegue Chrome senza interfaccia grafica
    chrome_options.add_argument("--disable-gpu")  # Evita problemi di rendering
    chrome_options.add_argument("--no-sandbox")  # Necessario per ambienti CI/CD
    chrome_options.add_argument("--disable-dev-shm-usage")  # Evita problemi di memoria condivisa

    try:
        # Usa webdriver-manager per installare automaticamente ChromeDriver
        service = Service(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service, options=chrome_options)

        # Stampa le versioni di Chrome e ChromeDriver per debugging
        print(">>> DEBUG: Chrome Version:", context.driver.capabilities['browserVersion'])
        print(">>> DEBUG: ChromeDriver Version:", context.driver.capabilities['chrome']['chromedriverVersion'])

    except Exception as e:
        print(f"!!! ERRORE: Impossibile avviare Chrome. Messaggio di errore: {e}")
        raise  # Rilancia l'eccezione per segnalare il fallimento


def after_scenario(context, scenario):
    print(">>> DEBUG: Entrato in after_scenario")
    if hasattr(context, 'driver'):
        context.driver.quit()
