import time
import requests
from tinydb import TinyDB
from datetime import datetime

url = "https://api.coinbase.com/v2/prices/spot"

def extracao_dados_bitcoin():
    response = requests.get(url)
    dados = response.json()
    return dados

def transforma_dados_bitcoin(dados):
    valor = dados["data"]["amount"]
    criptomoeda = dados["data"]["base"]
    moeda = dados["data"]["currency"]
    timestamp = datetime.now().timestamp()

    dados_transformados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": timestamp
    }
    return dados_transformados

def salvar_dados_tinydb(dados, db_name="bitcoin.json"):
    db = TinyDB(db_name)
    db.insert(dados)
    print("dados salvos com sucesso!")

if __name__ == "__main__":
    #extração dos dados de bitcoin
    while True:
        dados_json = extracao_dados_bitcoin()
        dados_tratados = transforma_dados_bitcoin(dados_json)
        salvar_dados_tinydb(dados_tratados)
        time.sleep(15)


