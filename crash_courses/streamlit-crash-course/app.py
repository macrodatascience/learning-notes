import streamlit as st

st.set_page_config(
    page_title="Streamlit Crash Course",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Streamlit Crash Course")

st.markdown(
    """
Welcome to the Streamlit Crash Course.

Use the sidebar to navigate between lessons.

This project demonstrates:

✔ Multi-page apps  
✔ Widgets  
✔ Charts  
✔ DataFrames  
✔ Dashboard layout  
"""
)

st.success("Select a page from the sidebar")