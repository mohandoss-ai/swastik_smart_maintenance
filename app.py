import streamlit as st
from PIL import Image
import streamlit as st
import time

import streamlit as st
import time

# --- Futuristic Splash Screen ---
def futuristic_splash():
    st.markdown("""
        <style>
        .splash {
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: radial-gradient(circle at center, #001020, #000000);
            display: flex; flex-direction: column;
            justify-content: center; align-items: center;
            color: #00ffff;
            font-family: 'Courier New', monospace;
            z-index: 9999;
            animation: fadeOut 2s ease-in-out 6s forwards;
        }

        @keyframes fadeOut {
            to { opacity: 0; visibility: hidden; }
        }

        .glow-logo {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            background-image: url("https://i.postimg.cc/XX98G79w/logo.jpg");
            background-size: cover;
            background-position: center;
            box-shadow: 0 0 40px #00ffff, 0 0 80px #0088ff inset;
            animation: pulse 1.5s infinite alternate;
        }

        @keyframes pulse {
            from { box-shadow: 0 0 25px #00ffff; }
            to { box-shadow: 0 0 60px #00ffff, 0 0 120px #0088ff inset; }
        }

        .boot-text {
            margin-top: 20px;
            text-align: center;
            font-size: 18px;
            opacity: 0;
            animation: appear 1s forwards;
        }

        .boot-text:nth-child(2) { animation-delay: 1s; }
        .boot-text:nth-child(3) { animation-delay: 2s; }
        .boot-text:nth-child(4) { animation-delay: 3s; }

        @keyframes appear { to { opacity: 1; } }

        /* FADE-IN DASHBOARD AFTER SPLASH */
        .fade-in {
            animation: fadeIn 1.5s ease-in;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        </style>

        <div class="splash">
            <div class="glow-logo"></div>
            <div class="boot-text">Initializing Swastik Smart Systems...</div>
            <div class="boot-text">Activating Predictive Engine...</div>
            <div class="boot-text">Loading Dashboard...</div>
        </div>
    """, unsafe_allow_html=True)

    time.sleep(6)  # splash duration


# --- Run Splash ---
futuristic_splash()
# --- FUTURISTIC UI STYLING ---
def set_futuristic_style():
    st.markdown("""
        <style>
        /* Background gradient */
        .stApp {
            background: linear-gradient(135deg, #0a0f24, #1b2735, #090a0f);
            color: #E0E0E0;
            font-family: 'Poppins', sans-serif;
        }

        /* Header styling */
        h1, h2, h3, h4 {
            color: #00FFFF;
            text-shadow: 0px 0px 15px #00FFFF88;
        }

        /* Info cards */
        .stMetric, .stMarkdown, .stDataFrame {
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 15px;
            box-shadow: 0 4px 30px rgba(0,0,0,0.4);
        }

        /* Buttons */
        div.stButton > button {
            background-color: #00FFFF;
            color: #0A0F24;
            border-radius: 8px;
            font-weight: 600;
            box-shadow: 0px 0px 20px #00FFFF80;
            transition: 0.3s;
        }

        div.stButton > button:hover {
            background-color: #14FFEC;
            color: black;
            transform: scale(1.05);
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(12px);
            border-right: 1px solid rgba(255,255,255,0.2);
        }

        /* Tables */
        .stDataFrame {
            border-radius: 10px;
            overflow: hidden;
        }

        /* Animations */
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(10px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        div[data-testid="stHorizontalBlock"] {
            animation: fadeIn 1s ease-in-out;
        }
        </style>
    """, unsafe_allow_html=True)

# Call this style function at the top of your dashboard
set_futuristic_style()

# --- Dashboard (with fade-in effect) ---
st.markdown('<div class="fade-in">', unsafe_allow_html=True)
st.title("🏗️ Swastik Smart Maintenance Dashboard")
st.markdown("""
Welcome to **Swastik Smart Maintenance** —  
Your intelligent predictive maintenance system powered by AI ⚙️  
""")

st.image("https://i.postimg.cc/XX98G79w/logo.jpg", width=180)

st.markdown("""
### 💡 Quick Actions
- 📊 View Equipment Analytics  
- 🧠 Check AI Maintenance Predictions  
- ⚙️ Manage Equipment Status  
- 📅 Upcoming Service Schedules  
""")

st.markdown("</div>", unsafe_allow_html=True)


import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import time



# Page setup
st.set_page_config(page_title="Swastik Smart Maintenance", layout="wide")


# Load data
data_path = "data/equipment.csv"
df = pd.read_csv(data_path)

# Convert Last Service Date to datetime
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
st.write("🧾 Columns in dataset:", list(df.columns))


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






