import streamlit as st
import pandas as pd

st.markdown("<h1 style='text-align:center;'>📊 Equipment Dashboard</h1>", unsafe_allow_html=True)

data = {
    "Equipment": ["Crane", "Boom Lift", "Forklift", "Truck Crane"],
    "Hours Used": [450, 320, 280, 610],
    "Last Service": ["2025-09-10", "2025-08-15", "2025-09-01", "2025-07-25"],
    "Health %": [85, 90, 75, 60]
}
df = pd.DataFrame(data)
st.dataframe(df)

st.bar_chart(df.set_index("Equipment")["Health %"])

