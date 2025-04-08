from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

def before_scenario(context, scenario):

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless=new")  # Esegue Chrome senza interfaccia grafica
    chrome_options.add_argument("--disable-gpu")  # Evita problemi di rendering
    chrome_options.add_argument("--no-sandbox")  # Necessario per ambienti CI/CD
    chrome_options.add_argument("--disable-dev-shm-usage")  # Evita problemi di memoria condivisa

    # Creazione cartella report se non esiste
    if not os.path.exists("reports"):
        os.makedirs("reports")

    try:
        # Usa webdriver-manager per installare automaticamente ChromeDriver
        service = Service(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service, options=chrome_options)

    except Exception as e:
        print(f"!!! ERRORE: Impossibile avviare Chrome. Messaggio di errore: {e}")
        raise  # Rilancia l'eccezione per segnalare il fallimento


def after_scenario(context, scenario):  
    if scenario.status == "failed":
        screenshot_dir = "reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        screenshot_path = os.path.join(screenshot_dir, f"{scenario.name}.png")
        context.driver.save_screenshot(screenshot_path)

        print(f"\n📸 Screenshot salvato in: {screenshot_path}")
        
    if hasattr(context, 'driver'):
        context.driver.quit()
