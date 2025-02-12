# Import required modules for Selenium and other utilities
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time # For delays

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Helper function to select elements with error handling
def try_select_element(xpath):
    try:
        # Wait until the element is present in the DOM
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return driver.find_elements(By.XPATH, xpath)
    except:
        # Retry finding the element after a delay
        time.sleep(1)
        return driver.find_elements(By.XPATH, xpath)

try:
    print("Apro il sito...")
    driver.get("https://marcheroma.contram.it/home/index")  # Navigate to the website
    driver.maximize_window()                                # Maximize the browser window
    time.sleep(3)

    # Fill in the departure field
    print("Compilo il campo di partenza...")
    partenza = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-partenza-flexdatalist"))
    )
    partenza.clear()                                        # Clear any pre-filled text
    partenza.send_keys("Camerino")                          # Input departure location
    time.sleep(1)

    # Load and select departure options
    risultati = try_select_element("//ul[@id='input-partenza-flexdatalist-results']/li")
    for risultato in risultati:
        if "Camerino Terminal" in risultato.text:           # Match desired option
            risultato.click()
            break
    print("Compilato il campo di partenza.")

    # Fill in the destination field
    print("Compilo il campo di destinazione...")
    destinazione = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-destinazione-flexdatalist"))
    )
    destinazione.clear()                                    # Clear any pre-filled text
    destinazione.send_keys("Porto San Giorgio")             # Input destination location
    time.sleep(1)

    # Load and select destination options
    risultati_destinazione = try_select_element("//ul[@id='input-destinazione-flexdatalist-results']/li")
    for risultato in risultati_destinazione:
        if "Porto San Giorgio" in risultato.text:           # Match desired option
            risultato.click()
            break
    print("Compilato il campo di destinazione.")

    # Fill in the travel date
    data = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-data-andata"))
    )
    data.clear()                                             # Clear any pre-filled text
    data.send_keys("29/11/2024")                             # Input travel date
    time.sleep(1)
    
    # Select passenger options
    print("Passeggeri...")
    passeggeri_box = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "input-passeggeri"))
    )

    passeggeri_box.click()                                  # Open the passenger options dropdown
    time.sleep(2)

    # Reduce the number of adults
    for _ in range(1):                                      # Modifica il range se necessario
        meno_adulti_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "btn-meno-adulto"))
        )
        meno_adulti_button.click()
        time.sleep(3)

    # Increase the number of students at 1
    for _ in range(1):                                      # Cambia il numero di click secondo necessità
        piu_studenti_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "btn-più-studente"))
        )
        piu_studenti_button.click()
        time.sleep(3)

    # Find and click on the "search" button
    cerca_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    cerca_button.click()
    time.sleep(3)

    # Select the booking option
    print("Selecting a booking option...")
    prenota_form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//form[@action='Prenota']"))
    )

    # Trova il pulsante all'interno del form e cliccaci sopra
    prenota_button = prenota_form.find_element(By.XPATH, ".//button[@type='submit']")
    prenota_button.click()
    time.sleep(3)

    # Trova e clicca sul pulsante "Conferma prenotazioni"
    conferma_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//form[@action='/Home/RitornaCarrello']//button[@type='submit' and contains(@class, 'btn-primary')]"))
    )
    conferma_button.click()
    time.sleep(3)

    print("Compilo l'email...")
    try:
        email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='email' and @name='EmailAcquirente']"))
        )
        email.clear()
        email.send_keys("INSERT HERE YOUR E-MAIL")
        time.sleep(3)
        print("EMAIL compilata ok")
    except Exception as e:
        print("ERRORE COMP: {e}")

    print("Compilo il nome...")
    try:
        nome = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @name='Nominativi[0].Nome']"))
        )
        nome.clear()
        nome.send_keys("Nicola")
        time.sleep(3)
        print("Nome ok")
    except Exception as e:
        print("ERRORE COMP: {e}")
    
        print("Compilo il cognome...")
    try:
        cognome = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @name='Nominativi[0].Cognome']"))
        )
        cognome.clear()
        cognome.send_keys("Capancioni")
        time.sleep(3)
        print("Cognome ok")
    except Exception as e:
        print("ERRORE COMP: {e}")
    
        print("Compilo la mail...")
    try:
        mail = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='email' and @name='Nominativi[0].Email']"))
        )
        mail.clear()
        mail.send_keys("INSERT HERE YOUR E-MAIL")
        time.sleep(3)
        print("mail2 ok")
    except Exception as e:
        print("ERRORE COMP: {e}")
    
        print("Compilo tel...")
    try:
        tel = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @name='Nominativi[0].Telefono']"))
        )
        tel.clear()
        tel.send_keys("3911388220")
        time.sleep(3)
        print("tel ok")
    except Exception as e:
        print("ERRORE COMP: {e}")
    
    # Trova e clicca sul pulsante "Conferma prenotazioni"
    try:
        b1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-success btn-lg mt-3' and @type='submit']"))
        )
        b1.click()
        time.sleep(3)
    except Exception as e:
        print("ERRORE COMP: {e}")

    # Chiudi il banner dei cookie se presente
    try:
        cookie_banner = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='dismiss cookie message' and contains(@class, 'cc-btn cc-dismiss')]"))
        )
        cookie_banner.click()
    except Exception as e:
        print("Banner dei cookie non trovato o già chiuso.")

    # Clicca il bottone "Conferma acquisto"
    b2 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-pagamento' and @class='btn btn-primary' and @type='submit']"))
    )
    b2.click()
    time.sleep(3)

except Exception as e:
    print("Errore:", e)



finally:
    print("Chiudo il browser...")
    time.sleep(30)
    driver.quit()
