from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

def get_value_by_label(driver, label):
    try:
        xpath = f"//td[starts-with(normalize-space(.), \"{label}\")]/following-sibling::td[1]//span"
        el = driver.find_element(By.XPATH, xpath)
        return el.text.strip()
    except NoSuchElementException:
        return None
    

def get_all_dirigeants(driver):
    dirigeants = []
    try:
        time.sleep(1)
        rows = driver.find_elements(By.XPATH, "//tbody/tr[contains(@class, '_row_sjr4l_19')]")
        for row in rows:
            role_cell = row.find_element(By.XPATH, "./td[1]")
            role = role_cell.get_attribute("textContent").replace("Role :", "").replace("\xa0", " ").strip()

            details_cell = row.find_element(By.XPATH, "./td[2]")
            details_text = details_cell.get_attribute("textContent").replace("Details :", "").replace("\xa0", " ").strip()

            dirigeants.append({"role": role, "details": details_text})
    except NoSuchElementException as e:
        print(f"DEBUG: exception -> {e}")
    return dirigeants


driver = webdriver.Chrome()

df = pd.read_csv("../entreprises.csv", delimiter='|')
resultats = []
for row in df["siren"]:

    url = "https://annuaire-entreprises.data.gouv.fr"
    driver.get(url)

    time.sleep(1) # ! important

    champ_input = driver.find_element(by=By.ID, value ='search-input-input')
    time.sleep(1) # ! important
    champ_input.clear()

    siren = row
    champ_input.send_keys(siren)
    time.sleep(1) # ! important
    envoyer = driver.find_element(by=By.CLASS_NAME, value="fr-btn")
    time.sleep(1) # ! important
    envoyer.click()

    time.sleep(1) # ! important

    # le nom
    h1 = driver.find_element(By.TAG_NAME, "h1")
    nom = h1.find_element(By.TAG_NAME, "a").text
    print("NOM : ",nom)

    #siren / siret

    siren = get_value_by_label(driver, "SIREN")
    siret = get_value_by_label(driver, "SIRET du siège social")
    adresse_postale = get_value_by_label(driver, "Adresse postale")
    print ("SIREN : ",siren)
    print("SIRET : ",siret)
    # @
    print ("ADRESSE POSTALE : ", adresse_postale)
    # secteur d'activité
    time.sleep(1)
    activite = get_value_by_label(driver, "Activité principale")
    print("ACTIVITÉ : ",activite)

    # capital
    time.sleep(1)
    capital = get_value_by_label(driver, "Capital")
    print("CAPITAL : ", capital if capital else "Non renseigné")



    # nb salaries

    try:
        time.sleep(1)
        effectifs = driver.find_element(By.XPATH, "/html/body/main/div/div[2]/div/div[2]/table/tbody/tr[13]/td[2]/div/span").text
        print("EFFECTIF SALARIÉ : ", effectifs)
    except NoSuchElementException:
        print("EFFECTIF SALARIÉ : Non renseigné")

    # dirigeants

    try:
        time.sleep(1)
        dirigeant_link = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[3]/div/a[2]")
        dirigeant_link.click()
        time.sleep(1)
        all_dirigeants = get_all_dirigeants(driver)
        if all_dirigeants:
            print("DIRIGEANTS :")
            for d in all_dirigeants:
                print(f"  - {d['role']} : {d['details']}")
        else:
            print("DIRIGEANTS : Non renseigné")
    except NoSuchElementException:
        print("DIRIGEANTS : Non renseigné")
    
    
    print("**************************************************************************************************************************************")
    print()

    dirigeants_str = "; ".join(
        f"{d['role']} - {d['details']}" for d in all_dirigeants
    )

    resultats.append({
        "Nom": nom,
        "Siren": siren,
        "Siret": siret,
        "Adresse Postale": adresse_postale,
        "Secteur d'activité": activite,
        "Capital": capital,
        "Nombres d'effectifs": effectifs,
        "Dirigeants": dirigeants_str
    })


    time.sleep(1)


df = pd.DataFrame(resultats)
df.to_csv("entreprises_enrichies.csv", index=False, encoding="utf-8")
driver.quit()


# import json
# df = pd.read_csv("entreprises_enrichies.csv")
# df["Dirigeants"] = df["Dirigeants"].apply(json.loads)


