import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--no-sandbox")  

driver = webdriver.Chrome(options=chrome_options)

def q6_bot_consulta_jurisdicao():
    url = "https://www.tjpb.jus.br/comarcas/lista"
    driver.get(url)
    
    comarcas_data = []

    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    print("Página carregada, procurando por comarcas...")
    
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'link-modal-comarca')))
    print("Comarcas encontradas.")
    
    comarca_elements = driver.find_elements(By.CLASS_NAME, 'link-modal-comarca')
    
    for comarca_element in comarca_elements:
        cidade = comarca_element.find_element(By.TAG_NAME, 'h1').text.strip()
        
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content')))
        
        modal_content = driver.find_element(By.CLASS_NAME, 'modal-content').get_attribute('innerHTML')
        soup = BeautifulSoup(modal_content, 'html.parser')
        
        for jurisdicao in soup.find_all('div', class_='jurisdicao'):
            nome_jurisdicao = jurisdicao.find('span', class_='nome').text.strip()
            nome_juiz = jurisdicao.find('span', class_='juiz').text.strip()
            comarcas_data.append({'Cidade': cidade, 'Jurisdicao': nome_jurisdicao, 'Juiz': nome_juiz})
        
        driver.find_element(By.CLASS_NAME, 'close').click()
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'modal-content')))
    
    driver.quit()
    
    df = pd.DataFrame(comarcas_data)
    return df

resultado = q6_bot_consulta_jurisdicao()
print(resultado)

