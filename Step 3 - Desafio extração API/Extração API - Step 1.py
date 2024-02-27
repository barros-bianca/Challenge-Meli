import requests
import csv

def extrair_dados_da_api(url):
    try:
        # Faz a requisição para a API
        response = requests.get(url)
        # Verifica se a requisição foi bem-sucedida (código 200)
        if response.status_code == 200:
            # Extrai os dados da resposta em formato JSON
            dados = response.json()
            # Retorna os dados extraídos
            return dados
        else:
            # Se a requisição não foi bem-sucedida, exibe uma mensagem de erro
            print("Erro ao acessar a API:", response.status_code)
            return None
    except Exception as e:
        # Se ocorrer algum erro durante o processo, exibe a mensagem de erro
        print("Erro:", e)
        return None

def salvar_dados_csv(dados, nome_arquivo):
    try:
        # Abre o arquivo CSV em modo de escrita
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            # Extrai os nomes das colunas a partir dos dados
            colunas = []
            for resultado in dados['results']:
                colunas.extend(resultado.keys())
            colunas = list(set(colunas))  # Remove duplicatas
            # Cria o escritor CSV
            escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=colunas)
            # Escreve o cabeçalho do CSV
            escritor_csv.writeheader()
            # Escreve os dados
            for resultado in dados['results']:
                escritor_csv.writerow(resultado)
        print("Os dados extraídos foram salvos com sucesso no arquivo:", nome_arquivo)
    except Exception as e:
        print("Erro ao salvar os dados no arquivo CSV:", e)

# URL da API
url_da_api = "https://api.mercadolibre.com/sites/MLA/search?q=licuadora&limit=50#json"

# Chama a função para extrair os dados da API
dados_extraidos = extrair_dados_da_api(url_da_api)

# Verifica se os dados foram extraídos com sucesso
if dados_extraidos:
    # Especifica o nome do arquivo para salvar os dados
    nome_arquivo = "dados_extraidos_liquidificador.csv"
    
    # Chama a função para salvar os dados em um arquivo CSV
    salvar_dados_csv(dados_extraidos, nome_arquivo)
else:
    print("Não foi possível extrair os dados da API.")



