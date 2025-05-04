from sqlalchemy import create_engine, text
import psycopg2 
import pandas as pd
import requests

engine = create_engine('postgresql://postgres:123456@localhost:5432/DADOS')

criar_sql = """
            CREATE TABLE IF NOT EXISTS dados_apiplaceholder (
            id SERIAL PRIMARY KEY,
            titulo VARCHAR(255),
            mensagem VARCHAR(255)
        );        
            """

def inserir_dados_banco(dados, engine):
    df = pd.DataFrame(dados)
    if not df.empty:
        with engine.begin() as conn:
            conn.execute(text("DROP TABLE IF EXISTS dados_apiplaceholder;"))
            conn.execute(text(criar_sql))

        df.to_sql("dados_apiplaceholder", con=engine, index=False, if_exists="append", method="multi")

        print("🛠️ Tabela verificada/criada com sucesso.")
        print(f"📥 Inseridos {len(df)} registros no banco de dados.")
    else:
        print("⚠️ Nenhum dado para inserir.")




