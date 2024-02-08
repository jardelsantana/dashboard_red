import streamlit as st
import pandas as pd
 

st.write("""
# Dashboard - Ativos da Redução
""")

df = pd.read_csv("ativos-reducao-tratados.csv")
df.set_index("ASSET TYPE",inplace=True )

st.area_chart(df["INSPECTION DATE"]).value_counts().index
df