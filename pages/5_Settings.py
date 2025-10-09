import streamlit as st

st.markdown("<h1 style='text-align:center;'>⚙️ Settings</h1>", unsafe_allow_html=True)
st.write("Upload new equipment data or modify dashboard settings here.")

uploaded = st.file_uploader("Upload Equipment CSV", type=["csv"])
if uploaded:
    st.success("✅ File uploaded successfully!")

