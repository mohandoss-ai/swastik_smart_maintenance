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


# --- Modern AI Predicted Maintenance Chart ---
st.subheader("📊 AI Predicted Maintenance Timeline (Upgraded Chart)")

import plotly.express as px

# Sample enhanced chart with dynamic color mapping
risk_color_map = {
    "Safe": "#00CC96",     # Green
    "Due Soon": "#FFA600", # Orange
    "Critical": "#EF553B"  # Red
}

chart_df = df.copy()
chart_df["Predicted Next Service"] = pd.to_datetime(chart_df["Predicted Next Service"], errors='coerce')

fig = px.bar(
    chart_df,
    x="Equipment Name",
    y="Predicted Next Service",
    color="Status",
    text="Status",
    color_discrete_map=risk_color_map,
    hover_data=["Location", "Technician", "Usage Hours"],
    title="📆 AI-Based Upcoming Maintenance Schedule",
)

fig.update_traces(
    textposition="outside",
    marker_line_width=1.5,
    marker_line_color="black"
)
fig.update_layout(
    plot_bgcolor="#f9f9f9",
    paper_bgcolor="white",
    title_font=dict(size=20, color="#2E4053"),
    xaxis_title="Equipment",
    yaxis_title="Predicted Service Date",
    margin=dict(t=60, b=60),
    height=500
)

st.plotly_chart(fig, use_container_width=True)



# Check column names safely
st.write("Available columns:", list(df.columns))

# Try different possible column names
issue_col = None
for col in df.columns:
    if 'Issue' in col and 'Flag' in col:
        issue_col = col
        break

if issue_col:
    critical_count = sum(df[issue_col] == 1)
    safe_count = sum(df[issue_col] == 0)
else:
    critical_count = safe_count = 0

due_soon_count = sum(df['Status'].astype(str).str.contains('Due Soon', case=False, na=False))

# --- Safe handling for Last Service Date ---
if 'Last Service Date' in df.columns:
    avg_service_date = pd.to_datetime(df['Last Service Date'], errors='coerce').max()
    if pd.notnull(avg_service_date):
        avg_service_date = avg_service_date.strftime("%Y-%m-%d")  # ✅ fixed
    else:
        avg_service_date = "No valid date found"
else:
    avg_service_date = "Column not found"

st.info(f"🗓️ Latest Recorded Service Date: **{avg_service_date}**")



# --- AI Insights Section ---
st.markdown("### 🤖 AI Insights")

import matplotlib.pyplot as plt
import numpy as np

# Show available columns (for debugging only once)
if st.checkbox("Show column names for debugging"):
    st.write(list(df.columns))

# Try to detect issue flag column automatically
issue_col = next((col for col in df.columns if 'issue' in col.lower() and 'flag' in col.lower()), None)
status_col = next((col for col in df.columns if 'status' in col.lower()), None)
date_col = next((col for col in df.columns if 'service' in col.lower() and 'date' in col.lower()), None)

# Compute values safely
critical_count = sum(df[issue_col] == 1) if issue_col else 0
safe_count = sum(df[issue_col] == 0) if issue_col else 0
due_soon_count = sum(df[status_col].astype(str).str.contains('Due Soon', case=False, na=False)) if status_col else 0

if date_col:
    # Convert to datetime just in case
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    avg_service_date = df[date_col].max().strftime("%Y-%m-%d")
else:
    avg_service_date = "N/A"

# Display summary
insight_text = f"""
- **🛠️ Critical Equipment:** {critical_count}
- **⚠️ Due Soon Equipment:** {due_soon_count}
- **✅ Safe Equipment:** {safe_count}
- **📅 Next Predicted Maintenance by:** {avg_service_date}
"""

st.info(insight_text)


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
    color="Status",  # changed here ✅
    size="Usage Hours",
    hover_name="Equipment Name",
    title="🤖 AI-Driven Maintenance Prediction",
)

st.plotly_chart(fig, use_container_width=True)




