import streamlit as st
import pandas as pd
 
st.write("""
# Dashboard - Ativos da Redução
""")

df = pd.read_csv("ativos-reducao-tratados.csv")

areas = df["AREA"].value_counts().index
area = st.sidebar.selectbox("Áreas", areas)
df_asset_type = df[(df["AREA"] == area)]

asset_types = df_asset_type["ASSET TYPE"].value_counts().index
asset_type = st.sidebar.selectbox("Asset Types", asset_types)

asset_status = df[df["ASSET TYPE"] == asset_type]