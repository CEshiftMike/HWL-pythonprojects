import streamlit as st
import pandas as pd
import numpy as np


st.title("Simple Data Dashboard")

uploadfile = st.file_uploader("Upload a CSV File", type="csv")

if uploadfile is not None:
    # st.write("File successfully loaded !")
    df = pd.read_csv(uploadfile)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by",columns)

    distinct = df[selected_column].unique()
    selected_column = st.selectbox("Select Column to")
    
    selected_column = st.selectbox("Select Value", selected_column)

    