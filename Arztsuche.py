import selenium                                             # Das Programm soll das Suchfeld nach bestimmten Postleitzahlen mit dem dazgehörigen Ort suchen und dann alle Ergebnisse in einem Dokument speichern
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pf #Mit dem "pf" sagen wir dem Script, wie wir das Importierte Framework aufrufen wollen

driver = webdriver.Chrome()
driver.get ("https://www.kvwl.de/arztsuche")
driver.implicitly_wait(5)

#Cookie-Banner akzeptieren
try: 

    accept_cookies = driver.find_element(By.XPATH,"//span[text()='Alles akzeptieren']/ancestor::button") 
    accept_cookies.click()
    print("Cookie-Banner akzeptiert")

except:

    print("Kein Cookie-Banner gefunden oder bereits geschlossen.")

#Das Suchfeld finden, Daten einfügen, den Vorschlag finden und Auswählen
try:

    Suchfeld = driver.find_element(By.XPATH, "//input[@placeholder='PLZ und Ort']")
    Suchfeld.send_keys("48145")
    Vorschlag = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), '48145 Münster')]"))
    )
    Vorschlag.click()
    print("Erfolg")

except:

     print("Keinen Erfolg")

#Suchfeld Button suchen und klicken 
try:

    Such_button = driver.find_element(By.XPATH, "//span[text()='Suchen']/ancestor::button")
    Such_button.click()
    print("Suchbutton Erfolgreich geklickt")

except:

    print("Suchbutton nicht Erfolgreich")

#Ein Listen Element finden
try:

    data=[] #Hiermit teilen wir mit das alles was jetzt folgt eine Liste seien wird
    Listeneinträge = driver.find_elements(By.CLASS_NAME, "c-react-list__item")
    for index, item in enumerate (Listeneinträge): 
                             

        Dr_name=item.find_element(By.CLASS_NAME, "c-react-list__item-header-title")
        print(Dr_name.text)
        data.append (Dr_name.text)
        
    
    
    print("Eintrag gefunden")
    
    dataframe= pf.DataFrame(data,columns=["Arztname"])
    dataframe.to_csv("Arzt_Liste.csv")

except Exception as error:

    print("Eintrag nicht gefunden",error)









driver.quit()
