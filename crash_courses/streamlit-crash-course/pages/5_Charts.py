import streamlit as st
import matplotlib.pyplot as plt
from utils import people_df

st.title("5. Charts")

df = people_df()

fig, ax = plt.subplots()

ax.bar(df["Name"], df["Age"])

st.pyplot(fig)