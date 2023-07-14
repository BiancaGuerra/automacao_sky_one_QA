"""
Automação de teste: nesse caso, a pesquisa seria "Música" e o site escolhido "YouTube"
Se o site abrir corretamente, o teste deu certo, se não, a frase "Falha ao acessar o site" será exibida
"""

# Importar funções externas
import pytest
from selenium import webdriver

# Inicializar o PyTest
@pytest.fixture(scope="module")

def setup():
    # Inicializar o driver do Selenium, utilizando o caminho do chromedriver.exe
    driver = webdriver.Chrome(r'C:\Users\bibir\Downloads\chromedriver_win32.zip')
    # Pausar a execução e retornar o valor indicado
    yield driver
    # Fechar o navegador após o teste
    driver.quit()

def teste_google(setup):
    # Obter o driver a partir da função 'setup' acima 
    driver = setup
    # Acessar o site
    driver.get('https://www.google.com/')
    # Localizar o campo de pesquisa, definido como 'q' no caso do Google
    campo_pesquisa = driver.find_element_by_name('q')
    # Definindo uma pesquisa
    pesquisa = "Música"
    # Envia a pesquisa para o campo de pesquisa
    campo_pesquisa.send_keys(pesquisa)
    # Submete o formulário de pesquisa
    campo_pesquisa.submit()

    # Atribui um link, dentro dos que apareceram, em uma variável
    site_escolhido = driver.find_element_by_css_selector('div#search div.g a')
    # Clica nessa variável
    site_escolhido.click()

    # Garante que o acesso ao site foi feito com sucesso
    assert "YouTube" in driver.title, "Falha ao acessar o site"