# import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# xlFile = pd.read_excel("AP Log Summary_2025.xlsx", sheet_name='1 Append')

def example_func(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

example_func(1, 2, 3, name="Test", value=42)