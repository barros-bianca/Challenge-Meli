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

def extrair_informacoes_colunas(dados):
    # Extrai apenas as informações das colunas desejadas

    # Extrai as informações de BRAND
    brand = None
    if dados.get("attributes"):
        for attribute in dados["attributes"]:
            if attribute["id"] == "BRAND":
                brand = attribute["value_name"]

    # Extrai as informações de ITEM_CONDITION
    item_condition = dados.get("item_condition")

    # Extrai as informações de WARRANTY_TIME
    warranty_time = None
    if dados.get("attributes"):
        for attribute in dados["attributes"]:
            if attribute["id"] == "WARRANTY_TIME":
                warranty_time = attribute["value_name"]

    informacoes_colunas = {
        "ID": dados.get("id"),
        "BRAND": brand,
        "ITEM_CONDITION": item_condition,
        "title": dados.get("title"),
        "seller_address_state_name": dados.get("seller_address").get("state").get("name"),
        "last_updated": dados.get("last_updated"),
        "date_created": dados.get("date_created"),
        "price": dados.get("price"),
        "WARRANTY_TIME": warranty_time,
        "tags_0": dados.get("tags", [])[0] if dados.get("tags") else None,
        "tags_1": dados.get("tags", [])[1] if len(dados.get("tags", [])) > 1 else None
    }
    return informacoes_colunas

def salvar_dados_csv(dados, nome_arquivo):
    if not dados:
        print("Não há dados para salvar.")
        return
    
    # Cria um conjunto de todas as chaves presentes nos dados
    chaves = set(dados[0].keys())
    
    # Abre o arquivo CSV para escrita
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        # Define o cabeçalho do CSV usando as chaves encontradas
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=sorted(chaves))
        escritor_csv.writeheader()
        
        # Escreve os dados no arquivo CSV
        for dado in dados:
            escritor_csv.writerow(dado)
    
    print("Os dados foram salvos com sucesso no arquivo:", nome_arquivo)

# Lista de IDs dos produtos
lista_ids = [
"MLA848014571", "MLA1365003393", "MLA1605273418", "MLA1402126893", "MLA936000383", "MLA1150996525",
    "MLA1375093303", "MLA1581874852", "MLA926767508", "MLA1535326890", "MLA1374329405", "MLA1468618372",
    "MLA1542209896", "MLA1481574012", "MLA907786534", "MLA1371842025", "MLA1246671369", "MLA1118668428",
    "MLA1471887242", "MLA1147829141", "MLA1411381595", "MLA1387978941", "MLA1574799646", "MLA1121944556",
    "MLA1410806053", "MLA1407247617", "MLA915239295", "MLA1468527882", "MLA1313941664", "MLA1388958159",
    "MLA1315726310", "MLA1543892930", "MLA1144365877", "MLA1148307007", "MLA1266244122", "MLA1136899589",
    "MLA927398569", "MLA1396813635", "MLA1584748484", "MLA1387888599", "MLA913616014", "MLA1487494324",
    "MLA1122596836", "MLA1680928214", "MLA1309714612", "MLA1664682664", "MLA902438921", "MLA1681026140",
    "MLA1387808641", "MLA1394169343"
]

url_base = "https://api.mercadolibre.com/items/"

# Lista para armazenar os dados de todos os produtos
dados_produtos = []

# Itera sobre cada ID na lista
for id_produto in lista_ids:
    # Constrói a URL completa para o produto atual
    url_produto = url_base + id_produto
    # Extrai os dados do produto da API
    dados_produto = extrair_dados_da_api(url_produto)
    # Verifica se os dados foram extraídos com sucesso
    if dados_produto:
        # Extrai as informações das colunas desejadas
        informacoes_colunas = extrair_informacoes_colunas(dados_produto)
        # Adiciona as informações do produto à lista de dados de todos os produtos
        dados_produtos.append(informacoes_colunas)

# Verifica se foram extraídos dados de algum produto
if dados_produtos:
    # Nome do arquivo CSV para salvar as informações das colunas
    nome_arquivo_csv = "tabela_microondas_final.csv"
    # Salva as informações das colunas em um arquivo CSV
    salvar_dados_csv(dados_produtos, nome_arquivo_csv)
else:
    print("Não foi possível extrair dados de nenhum produto.")
