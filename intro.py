import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello World!")
st.title("SAP SAM Log Parser")
st.header("Header")
st.text("general text")
st.markdown("**bold text** *italic text*")
st.markdown("---")
st.metric(label="speed", value=100, delta=10)

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
st.table(df)
st.dataframe(df)

st.checkbox( )

