import pandas as pd
import requests
from bancodedados import inserir_dados_banco, engine, text
dados = []

def coletar_dados_api_meals():

    url = "https://www.themealdb.com/api/json/v1/1/categories.php"
    response = requests.get(url)

    if response.status_code != 200:
        print("Erro na requisição ",response.status_code)   

    try:
        data = response.json()
        for item in data['categories']:
            dados.append({
            "idcategory": item.get("idCategory"),
            "strCategory": item.get("strCategory"),
            "strCategoryThumb" : item.get("strCategoryThumb"),
            "strCategoryDescription" : item.get("strCategoryDescription")  
            })
            
        inserir_dados_banco(dados, engine)
        return pd.DataFrame(dados)
    
    except ValueError as e:
        print("Erro ao processar JSON")





