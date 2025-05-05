import pandas as pd
import requests
from bancodedados import inserir_dados_banco,engine,text
import pandas as pd


def coletar_dados_api_placeholder():
    dados = []
    base_url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(base_url)

    if response.status_code != 200:
        print(f"Erro na requisição {response.status_code}")

    try:
        data = response.json()

        if not data:
            print("Nenhum dado retornado.")

        for item in data:
            dados.append({
                "id": item.get("id"),
                "titulo": item.get("title"),
                "mensagem": item.get("body")
            })

        #inserir_dados_banco(dados, engine)
        return pd.DataFrame(dados)
        
        
        
    except ValueError as e:
        print("Erro ao processar JSON")
    



    