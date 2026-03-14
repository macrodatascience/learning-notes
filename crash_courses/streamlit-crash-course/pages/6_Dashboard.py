import streamlit as st
from utils import random_df

st.title("6. Dashboard")

df = random_df(50, 3)

st.line_chart(df)

col1, col2, col3 = st.columns(3)

col1.metric("Users", 120)
col2.metric("Revenue", 540)
col3.metric("Growth", "12%")

st.success("Dashboard running")