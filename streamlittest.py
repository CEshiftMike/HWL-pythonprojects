import streamlit as st
import pandas as pd
import numpy as np

st.write("Streamlit is working!")

all_users = ["Alice","bob","charlie","david"]
with st.container(border=True):
    users = st.multiselect("Select users", options=all_users, default=all_users)
    rolling_average = st.toggle("Rolling Average")

    np.random.seed(42)
    data = pd.DataFrame(np.random.randn(20, len(users)), columns=users)
    if rolling_average:
        data = data.rolling(7).mean().dropna()


tab1, tab2 = st.tabs(["Chart","Dataframe"])
tab1.line_chart(data, height=250)
tab2.dataframe(data, height=250, use_container_width=True)