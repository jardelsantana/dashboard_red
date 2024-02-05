import streamlit as st
import pandas as pd
 
st.write("""
# Dashboard - Ativos da Redução
""")

df = pd.read_csv("ativos-reducao-tratados.csv")

areas = df["AREA"].value_counts().index
area = st.sidebar.selectbox("Áreas", areas)
