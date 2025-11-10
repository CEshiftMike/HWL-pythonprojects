import streamlit as st
import pandas as pd

filpath = r"C:\Work Repo\HWL-pythonprojects\AP Log Summary_2025.xlsx"

df = pd.read_excel(filpath, sheet_name='1 Append')

print(df.head(10).to_string(index=False))