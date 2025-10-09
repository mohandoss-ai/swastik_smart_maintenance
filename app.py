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
# -----------------------------------------------------------
# 🧠 Predictive Maintenance (AI Section)
# -----------------------------------------------------------

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.write("### 🤖 Predictive Maintenance Insights")

# Prepare data for model
X = df[['Hours_Used', 'Machine_Age']]
y = df['Issue_Flag']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a simple AI model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict probability of issues
df['Maintenance_Risk'] = model.predict_proba(X)[:, 1]

# Display predictions
st.write("#### Predicted Maintenance Risk Levels")
st.dataframe(df[['Equipment_ID', 'Equipment_Type', 'Hours_Used', 'Machine_Age', 'Maintenance_Risk']])

# Highlight high-risk equipment
high_risk = df[df['Maintenance_Risk'] > 0.6]
if not high_risk.empty:
    st.warning("⚠️ Machines that may require immediate maintenance:")
    st.table(high_risk[['Equipment_ID', 'Equipment_Type', 'Maintenance_Risk']])
else:
    st.success("✅ All equipment is in good condition for now.")

