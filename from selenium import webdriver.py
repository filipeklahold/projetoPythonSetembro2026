from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def buscar_altura(nome_famoso):
    # Inicializa o navegador Chrome
    driver = webdriver.Chrome()
    
    try:
        # Abre o site do Google
        driver.get("https://google.com")
        
        # Encontra a barra de pesquisa do Google
        caixa_busca = driver.find_element(By.NAME, "q")
        
        # Digita o termo de pesquisa e aperta Enter
        termo_pesquisa = f"altura de {nome_famoso}"
        caixa_busca.send_keys(termo_pesquisa)
        caixa_busca.send_keys(Keys.RETURN)
        
        # Aguarda 3 segundos para a página carregar os resultados
        time.sleep(3)
        
        # Tenta capturar o bloco de resposta rápida do Google (focado em altura)
        # O Google costuma usar a classe 'Z0LcW' ou atributos de dados para respostas diretas
        try:
            altura = driver.find_element(By.CSS_SELECTOR, "div.Z0LcW, div.kp-hc, div.BNeawe.iBp4i.AP7Wnd").text
            print(f"\nA altura de {nome_famoso} é: {altura}")
        except Exception:
            print(f"\nNão consegui encontrar a altura exata no bloco de destaque para {nome_famoso}.")
            print("Verifique a janela do navegador aberta.")
            
        # Mantém o navegador aberto por mais alguns segundos para você visualizar
        time.sleep(5)
        
    finally:
        # Fecha o navegador de forma segura
        driver.quit()

# --- Execução do programa ---
if __name__ == "__main__":
    famoso = input("Digite o nome do famoso que deseja buscar: ")
    buscar_altura(famoso)
