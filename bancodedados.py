from sqlalchemy import create_engine, text
import psycopg2 
import pandas as pd
import requests

engine = create_engine('postgresql://postgres:123456@localhost:5432/DADOS')

criar_sql_dadosapiplaceholder= """
            CREATE TABLE IF NOT EXISTS dados_apiplaceholder (
            id SERIAL PRIMARY KEY,
            titulo VARCHAR(255),
            mensagem VARCHAR(255)
        );        
            """

criar_sql_dadosapimeals = """
            CREATE TABLE IF NOT EXISTS dados_apimeals (
            idcategory SERIAL PRIMARY KEY,
            strCategory TEXT,
            strCategoryThumb TEXT,
            strCategoryDescription TEXT
        );        
            """


def inserir_dados_banco(dados, engine):
    df = pd.DataFrame(dados)
    if not df.empty:
#       with engine.begin() as conn:
#           conn.execute(text("DROP TABLE IF EXISTS dados_apiplaceholder;"))
#           conn.execute(text(criar_sql_dadosapiplaceholder))
#
#       df.to_sql("dados_apiplaceholder", con=engine, index=False, if_exists="append", method="multi")

        with engine.begin() as conn:

            conn.execute(text("DROP TABLE IF EXISTS dados_apimeals;"))
            conn.execute(text(criar_sql_dadosapimeals))

        df.columns = df.columns.str.lower().str.strip()     
        df.to_sql("dados_apimeals", con=engine, index=False, if_exists="append", method="multi")
        
        print("🛠️ Tabela verificada/criada com sucesso.")
        print(f"📥 Inseridos {len(df)} registros no banco de dados.")
    else:
        print("⚠️ Nenhum dado para inserir.")




