import streamlit as st


# --- PAGE HEADER ---
st.markdown("""
# 🏗️ Swastik Smart Maintenance Dashboard
**AI-Powered Predictive Maintenance & Equipment Monitoring**  
*Ensuring uptime, safety, and performance — every day.*
""")

st.markdown("---")

# --- App Header with Logo ---
st.image("swastik_logo.png", width=120)

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Page setup
st.set_page_config(page_title="Swastik Smart Maintenance", layout="wide")


# Load data
data_path = "data/equipment.csv"
df = pd.read_csv(data_path)

# Convert Last_Service_Date to datetime
df['Last_Service_Date'] = pd.to_datetime(df['Last_Service_Date'], errors='coerce')

st.write("### Equipment Maintenance Data")
st.dataframe(df)
# --- 📥 Download Equipment Data Section ---
st.subheader("📥 Download Equipment Data Section")

csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Download Equipment Data (CSV)",
    data=csv,
    file_name="equipment_maintenance_data.csv",
    mime="text/csv",
    key="download_csv"
)


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
# -----------------------------------------------------------
# 🗓️ Smart Maintenance Scheduler
# -----------------------------------------------------------

st.write("### 🗓️ Maintenance Scheduler")

equipment_list = df['Equipment_ID'].tolist()
selected_equipment = st.selectbox("Select Equipment for Scheduling", equipment_list)

selected_date = st.date_input("Select Next Service Date")

if st.button("Schedule Maintenance"):
    st.success(f"✅ Maintenance for **{selected_equipment}** scheduled on **{selected_date}**.")
    st.balloons()

st.write("You can use this tool to plan preventive maintenance based on AI risk predictions.")
# --- AI Maintenance Prediction Section ---
import random
import time

st.header("🔧 AI Predictive Maintenance Assistant")

st.write("""
This smart assistant uses AI to predict **when maintenance is needed**
based on equipment usage and sensor data.  
It helps the service team prevent sudden breakdowns and improve uptime.
""")

# Input fields
hours = st.number_input("⏱️ Equipment Run Hours", min_value=0, max_value=10000, value=1200)
temp = st.number_input("🌡️ Oil Temperature (°C)", min_value=0, max_value=200, value=70)
vibration = st.number_input("💥 Vibration Level (mm/s)", min_value=0, max_value=100, value=15)

# Predict button
if st.button("🚀 Predict Maintenance"):
    with st.spinner("Analyzing with AI..."):
        time.sleep(2)
        risk = (temp * 0.4 + vibration * 0.3 + hours * 0.0005) + random.randint(-5, 5)
        if risk < 50:
            st.success(f"✅ Machine is healthy. Next maintenance due in {random.randint(20,40)} days.")
        elif 50 <= risk < 100:
            st.warning(f"⚠️ Maintenance likely needed in {random.randint(10,20)} days. Schedule inspection soon.")
        else:
            st.error(f"🚨 Immediate attention required! High risk of failure within {random.randint(1,7)} days.")
# --- Maintenance Insights Dashboard ---
import pandas as pd
import matplotlib.pyplot as plt

st.header("📊 Maintenance Insights Dashboard")

# Create sample data (for demo)
data = {
    "Machine": ["Crane A", "Crane B", "Crane C", "Crane D"],
    "Status": ["Healthy", "Needs Attention", "Critical", "Healthy"],
    "Run Hours": [1200, 2100, 3400, 1500],
    "Next Service (Days)": [25, 12, 5, 30]
}

df = pd.DataFrame(data)

# Show data in a nice table
st.dataframe(df)

# Count statuses for visualization
status_counts = df["Status"].value_counts()

# Create a bar chart
fig, ax = plt.subplots()
ax.bar(status_counts.index, status_counts.values)
ax.set_title("Equipment Health Summary")
ax.set_xlabel("Status")
ax.set_ylabel("Number of Machines")

st.pyplot(fig)

# Summary Text
healthy = status_counts.get("Healthy", 0)
attention = status_counts.get("Needs Attention", 0)
critical = status_counts.get("Critical", 0)

st.info(f"✅ {healthy} Machines Healthy | ⚠️ {attention} Need Attention | 🚨 {critical} Critical Condition")
import pandas as pd
from datetime import datetime

st.subheader("🔧 Swastik Service & Maintenance Dashboard")

# --- Swastik-style Maintenance Data ---
data = {
    "Equipment Name": ["Crane A-01", "Crane B-02", "Forklift F-07", "BoomLift B-03", "Tower Crane T-10"],
    "Equipment Type": ["Hydraulic Crane", "Tower Crane", "Forklift", "Boom Lift", "Tower Crane"],
    "Last Service Date": ["2025-09-15", "2025-08-28", "2025-09-10", "2025-09-22", "2025-08-30"],
    "Usage Hours": [410, 520, 280, 300, 600],
    "Location": ["Chennai", "Coimbatore", "Madurai", "Trichy", "Salem"],
    "Technician": ["Ramesh", "Arjun", "Siva", "Manoj", "Prakash"],
    "Predicted Next Service": ["2025-10-30", "2025-10-10", "2025-11-02", "2025-11-15", "2025-10-05"],
    "Status": ["⚠️ Due Soon", "❌ Critical", "✅ Safe", "✅ Safe", "⚠️ Due Soon"]
}

df = pd.DataFrame(data)


# --- Display Dashboard with color highlights ---
def highlight_status(val):
    if "Critical" in val:
        color = 'background-color: #ff4d4d; color: white;'  # Red for critical
    elif "Due Soon" in val:
        color = 'background-color: #ffd633;'  # Yellow for due soon
    elif "Safe" in val:
        color = 'background-color: #b3ffb3;'  # Green for safe
    else:
        color = ''
    return color

st.dataframe(df.style.applymap(highlight_status, subset=["Status"]), use_container_width=True)


# --- AI Summary Section ---
st.markdown("### 🤖 AI Insights")
import matplotlib.pyplot as plt
import numpy as np

st.markdown("### 📊 AI Predicted Maintenance Timeline (Upgraded Chart)")

# Sort by next service date
df_sorted = df.sort_values("Predicted Next Service")

# Set up the figure
fig, ax = plt.subplots(figsize=(8, 4))

# Define colors based on status
colors = df_sorted["Status"].map({
    "✅ Safe": "#00cc66",       # green
    "⚠️ Due Soon": "#ffcc00",   # yellow
    "❌ Critical": "#ff4d4d"    # red
}).fillna("#999999")
# --- Predictive Maintenance Visualization (AI Bubble Chart) ---
st.markdown("### 🤖 Predictive Maintenance Risk Overview")

import plotly.express as px

# Create a sample predictive dataset
df["Predicted Next Service"] = pd.date_range("2025-10-10", periods=len(df), freq="10D")
df["Risk Level"] = df["Status"].map({
    "Good": "Low",
    "Needs Service": "Medium",
    "Critical": "High"
})
df["Risk Color"] = df["Risk Level"].map({
    "Low": "green",
    "Medium": "orange",
    "High": "red"
})

# Add Risk Level for visualization (based on Status)
df["Risk Level"] = df["Status"].map({
    "✅ Safe": "Low",
    "⚠️ Due Soon": "Medium",
    "❌ Critical": "High"
}).fillna("Low")

# Create a modern scatter chart
import plotly.express as px

fig = px.scatter(
    df,
    x="Usage Hours",
    y="Predicted Next Service",
    color="Risk Level",
    size="Usage Hours",
    hover_name="Equipment Name",
    title="🤖 AI-Driven Maintenance Prediction",
)

st.plotly_chart(fig, use_container_width=True)





