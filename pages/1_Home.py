import streamlit as st
import time

# --- SPLASH SCREEN ---
st.markdown("""
    <style>
        .splash-container {
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background-color: #0E1117;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: white;
            z-index: 9999;
        }
        .logo {
            font-size: 60px;
            margin-bottom: 20px;
        }
        .app-name {
            font-size: 28px;
            font-weight: bold;
        }
    </style>
    <div class="splash-container" id="splash">
        <div class="logo">🔧</div>
        <div class="app-name">Swastik Smart Maintenance</div>
        <p>Loading your dashboard...</p>
    </div>
    <script>
        setTimeout(function(){
            document.getElementById('splash').style.display='none';
        }, 2000);
    </script>
""", unsafe_allow_html=True)

time.sleep(2)

import streamlit as st

st.markdown("<h1 style='text-align:center;'>🏠 Swastik Smart Maintenance Dashboard</h1>", unsafe_allow_html=True)
st.write("Welcome to the Swastik Smart Maintenance system — your AI-powered assistant for predictive maintenance.")

st.markdown("---")
st.info("Use the sidebar to explore Dashboard, AI Insights, Maintenance Logs, and Settings.")
