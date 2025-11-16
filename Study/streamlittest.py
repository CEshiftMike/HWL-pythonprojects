import streamlit as st
import pandas as pd
import numpy as np


st.title("Simple Data Dashboard")

uploadfile = st.file_uploader("Upload a CSV File", type="csv")

if uploadfile is not None:
    # st.write("File successfully loaded !")
    df = pd.read_csv(uploadfile)

    st.subheader("Data Preview")
    # st.write(df.head())
    st.write(df)

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by",columns)

    distinct = df[selected_column].unique()
    # selected_column = st.selectbox("Select Column to")
    
    selected_value = st.selectbox("Select Value", distinct)
    # listdistinct = st.write(distinct)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
    else:
        st.write("Waiting file upload")