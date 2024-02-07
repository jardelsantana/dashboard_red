import streamlit as st
import pandas as pd
 

st.write("""
# Dashboard - Ativos da Redução
""")

df = pd.read_csv("ativos-reducao-tratados.csv")

temporaria = df["INSPECTOR"].value_counts() == "DAYVID E RAUL"
temporaria
df