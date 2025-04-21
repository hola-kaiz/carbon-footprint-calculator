import streamlit as st
import numpy as np

st.markdown("""
    <style>
        * {
            font-family: 'Consolas', monospace;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 5px;
            box-shadow: 0 5px 15px rgba(0, 128, 0, 0.3);
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .input-container {
            margin-bottom: 20px;
        }
        .stSelectbox, .stNumberInput {
            margin-top: 10px;
        }
        .header {
            color: #2C3E50;
            font-size: 28px;
            font-weight: 600;
        }
        .subheader {
            color: #34495E;
            font-size: 20px;
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 Carbon Footprint Calculator")
st.write("Estimate your monthly **carbon footprint** based on your lifestyle.")

# Collect user inputs with more spacing
Age = st.number_input("Age", min_value=0, max_value=120, value=30, key="age", label_visibility="collapsed")
Gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="gender", label_visibility="collapsed")
Mode_of_transport = st.selectbox("Mode of Transport", ["Car", "Bike", "Public Transport", "Walking", "EV", "Bicycle"], key="transport", label_visibility="collapsed")
Work_Hours = st.number_input("Work Hours", min_value=0, max_value=10, value=0, key="work_hours")
Shopping_Hours = st.number_input("Shopping Hours", min_value=0, max_value=8, value=0, key="shopping_hours")
Entertainment_Hours = st.number_input("Entertainment Hours", min_value=0, max_value=24, value=0, key="entertainment_hours")
Home_Energy_Consumption_kWh = st.number_input("Home Energy Consumption (kWh)", min_value=0.0, max_value=12.0, value=0.0, key="energy_consumption")
Charging_Station_Usage = st.number_input("Charging Station Usage", min_value=0, max_value=1, value=0, key="charging_usage")
Steps_Walked = st.number_input("Steps Walked", min_value=0, max_value=20000, value=0, key="steps_walked")
Calories_Burned = st.number_input("Calories Burned", min_value=300, max_value=15000, value=300, key="calories_burned")
Sleep_Hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, value=6.0, key="sleep_hours")
Social_Media_Hours = st.number_input("Social Media Hours", min_value=0.0, max_value=24.0, value=1.0, key="social_media_hours")
Public_Events_Hours = st.number_input("Public Event Hours", min_value=0.0, max_value=3.0, value=0.0, key="public_events_hours")

# Mapping categorical values
gender_map = {"Male": 0, "Female": 1, "Other": 2}
transport_map = {"Car": 2, "Bike": 1, "Public Transport": 1.5, "Walking": 0.5, "EV": 1, "Bicycle": 0.3}

# "Fake" prediction logic (simple sum of weighted inputs)
if st.button("Submit"):
    score = (
        Home_Energy_Consumption_kWh * 10 +
        Work_Hours * 2 +
        Shopping_Hours * 1.5 +
        Entertainment_Hours * 1.2 +
        transport_map[Mode_of_transport] * 5 +
        Charging_Station_Usage * 3 +
        Social_Media_Hours * 0.5 +
        Public_Events_Hours * 1.0 -
        Steps_Walked * 0.0005 -
        Calories_Burned * 0.001 -
        Sleep_Hours * 0.2
    )
    st.success(f"Estimated Carbon Footprint: {score:.2f} kgCO₂/month")