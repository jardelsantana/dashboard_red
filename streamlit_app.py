import streamlit as st
import pandas as pd
 
st.write("""
# Dashboard - Ativos da Redução
""")

df = pd.read_csv("ativos-reducao-tratados.csv", index_col=0)
df
#areas = df["AREA"]

#areas