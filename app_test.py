import streamlit as st
import pandas as pd


df = pd.DataFrame({
    'SKU': ['G2G-803', 'G2G-234', 'G2G-232', 'G2G-07', 'G2G-3103'],
    'QTY': [288, 96, 96, None, 288]
})

print(df)
st.write(df)