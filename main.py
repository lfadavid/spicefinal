import streamlit as st
import pandas as pd

pg = st.navigation(
            {
            "Consultas": [st.Page("calculadorafrete.py", title="Calculadora de Frete"), st.Page("consultarotas.py", title="Consulta por Rotas")]
            #"Conta": [st.Page(logout, title="Sair"), st.Page("criar_conta.py", title="Criar Conta")]
            }
)
pg.run()