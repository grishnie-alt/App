import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Medical Device Quiz", layout="wide")

@st.cache_data
def load_questions(xlsx):
    xl=pd.ExcelFile(xlsx)
    data={}
    for sheet in xl.sheet_names:
        try:
            df=pd.read_excel(xlsx,sheet_name=sheet,header=None)
            data[sheet]=df.fillna("")
        except Exception:
            pass
    return data

st.title("Medical Device Quiz App")
st.write("Foundation version. Upload your question bank workbook.")
file=st.file_uploader("Upload Excel",type=['xlsx'])
if file:
    sheets=load_questions(file)
    st.success(f"Loaded {len(sheets)} tabs")
    topic=st.selectbox("Topic", list(sheets.keys()))
    st.subheader("Sheet Preview")
    st.dataframe(sheets[topic].head(20), use_container_width=True)
    st.info("Next version: automatic question parsing, scoring, explanations, analytics.")
