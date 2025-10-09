import streamlit as st
import pandas as pd

st.markdown("<h1 style='text-align:center;'>🧾 Maintenance Logs</h1>", unsafe_allow_html=True)

logs = {
    "Date": ["2025-09-01", "2025-08-22", "2025-08-10"],
    "Equipment": ["Boom Lift", "Truck Crane", "Forklift"],
    "Issue": ["Hydraulic Leak", "Engine Noise", "Battery Replacement"],
    "Action Taken": ["Seal replaced", "Engine tuned", "Battery replaced"]
}
df = pd.DataFrame(logs)
st.dataframe(df)

