import streamlit as st
from utils import people_df

st.title("4. Widgets")

df = people_df()

age = st.slider(
    "Select age",
    0,
    60,
    (20, 40)
)

filtered = df[
    (df["Age"] >= age[0]) &
    (df["Age"] <= age[1])
]

st.dataframe(filtered)