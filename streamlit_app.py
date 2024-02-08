import streamlit as st
import pandas as pd
 

st.write("""
# Dashboard - Ativos da Redução
""")

df = pd.read_csv("ativos-reducao-tratados.csv")
df.set_index("INSPECTION DATE",inplace=True )

st.line_chart(df["INSPECTION DATE"] != None)
df