import streamlit as st
import pandas as pd
 
st.write("""
# Dashboard - Ativos da Redução
""")

df = pd.read_csv("ativos-reducao-tratados.csv")

num_of_rows = len(df)

st.write(num_of_rows)