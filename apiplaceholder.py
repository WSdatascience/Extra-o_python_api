import pandas as pd
import requests
import streamlit as st

dados = []

def coletar_dados_api_placeholder():
    base_url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(base_url)

    if response.status_code != 200:
        print(f"Erro na requisição {response.status_code}")

    try:
        data = response.json()

        for item in data:
            dados.append({
                "id": item.get("id"),
                "titulo": item.get("title"),
                "mensagem": item.get("body")
            })
        
        return st.dataframe(dados)
        
        if not data:
            print("Nenhum dado retornado.")
        
    except ValueError as e:
        print("Erro ao processar JSON")
    



    