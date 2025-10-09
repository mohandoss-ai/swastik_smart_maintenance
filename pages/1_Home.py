import streamlit as st

# ✅ Set page style and configuration
st.set_page_config(page_title="Home - Swastik Smart Maintenance", page_icon="🏠", layout="wide")

st.markdown(
    """
    <style>
    .main {
        background-color: #F9FAFB;
        padding: 2rem;
    }
    h1 {
        color: #1E3A8A;
        font-weight: 800;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ Add the Home Page heading
st.title("🏠 Home Page")
st.markdown("Welcome to the **Swastik Smart Maintenance Dashboard!** 👋")

st.markdown("Use the sidebar on the left to navigate between different sections.")
st.divider()

