"""
Automação de teste: nesse caso, o site seria da Sky.One, no ícone "Cases" e o segmento "Jump Digital"
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope = "module")
def setup():
    driver = webdriver.Chrome(r"C:\Users\bibir\Downloads\chromedriver_win32.zip")
    yield driver
    driver.quit()

def teste_skyone(setup):
    driver = setup
    driver.get("https://skyone.solutions/")

    cases = driver.find_element_by_link_test("Cases")
    cases.click()

    # Garantir que, primeiramente, a página "Cases" está abrindo corretamente
    assert "Cases" in driver.title, "Falha ao acessar a página de Cases"

    segmento = driver.find_element_by_link_teste("Jump Digital")
    segmento.click()

    # Garantir que o segmento escolhido está sendo exibido na tela
    assert "Jump Digital" in driver.title, "Falha ao acessar o segmento escolhido"


