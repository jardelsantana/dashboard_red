import streamlit as st
import pandas as pd
 
st.write("""
# Dashboard - Ativos da Redução
""")

df = pd.read_csv("ativos-reducao-tratados.csv")
#df.set_index("AREA", inplace= True)
st.line_chart(df["AREA"])
