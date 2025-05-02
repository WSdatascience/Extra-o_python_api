from apiplaceholder import coletar_dados_api_placeholder
from apimeals import coletar_dados_api_meals
import streamlit as st



menu_option = st.sidebar.selectbox(
    "Menu",
    ["Dados - API Placeholder", "Dados - API Meals"]
)

if menu_option == "Dados - API Placeholder":
    coletar_dados_api_placeholder() 

elif menu_option == "Dados - API Meals":
    coletar_dados_api_meals()
    





