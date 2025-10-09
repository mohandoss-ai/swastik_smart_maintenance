import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Page setup
st.set_page_config(page_title="Swastik Smart Maintenance", layout="wide")

st.title("🏗️ Swastik Smart Maintenance")
st.subheader("AI-powered Service & Maintenance Dashboard")

# Load data
data_path = "data/equipment.csv"
df = pd.read_csv(data_path)

# Convert Last_Service_Date to datetime
df['Last_Service_Date'] = pd.to_datetime(df['Last_Service_Date'], errors='coerce')

st.write("### Equipment Maintenance Data")
st.dataframe(df)

# Maintenance Insights
st.write("### 📊 Maintenance Summary")

avg_hours = df['Hours_Used'].mean()
avg_age = df['Machine_Age'].mean()
issues = df['Issue_Flag'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Avg Hours Used", f"{avg_hours:.1f}")
col2.metric("Avg Machine Age (yrs)", f"{avg_age:.1f}")
col3.metric("Active Issues", int(issues))

# Visualization
st.write("### 🧠 Hours Used vs Machine Age")
fig = px.scatter(df, x="Machine_Age", y="Hours_Used", color="Equipment_Type", size="Hours_Used", hover_data=["Equipment_ID"])
st.plotly_chart(fig, use_container_width=True)

st.success("✅ Dashboard loaded successfully!")
