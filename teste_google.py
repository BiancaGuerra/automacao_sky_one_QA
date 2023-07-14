import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def setup():
    # Inicializar o driver do Selenium (ajuste o caminho para o local do driver em seu sistema)
    driver = webdriver.Chrome('/caminho/para/o/chromedriver')
    yield driver
    # Fechar o navegador após o teste
    driver.quit()

def test_google_search(setup):
    driver = setup

    # 1. Acessar o site https://www.google.com/
    driver.get('https://www.google.com/')

    # 2. Fazer uma pesquisa de algo que você gosta
    campo_pesquisa = driver.find_element_by_name('q')
    pesquisa = "Automação de testes"
    campo_pesquisa.send_keys(pesquisa)
    campo_pesquisa.submit()

    # 3. Clicar no site escolhido
    link_resultado = driver.find_element_by_css_selector('#search .g:first-child a')
    link_resultado.click()

    # 4. Garantir que o acesso ao site foi feito com sucesso
    titulo_pagina = driver.title
    assert "Nome do Site" in titulo_pagina, "Falha ao acessar o site"