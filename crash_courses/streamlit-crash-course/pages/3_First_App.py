import streamlit as st
import pandas as pd

st.title("3. First App")

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
}

df = pd.DataFrame(data)

st.dataframe(df)