import streamlit as st
import pandas as pd
 
st.write("""
# Dashboard - Ativos da Redução
""")

df = pd.read_csv("ativos-reducao-tratados.csv")

num_of_rows = len(df)

print(f"The number of rows is {num_of_rows}")