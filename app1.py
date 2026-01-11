import streamlit as st
import pickle
import pandas as pd
from PIL import Image

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Obesity Prediction System",
    page_icon="🍔",
    layout="centered"
)

# -----------------------------
# Load Model & Files
# -----------------------------
model = pickle.load(open("obesity_model.sav", "rb"))
scaler = pickle.load(open("scaler.sav", "rb"))
features = pickle.load(open("features.sav", "rb"))

# -----------------------------
# Load Banner Safely
# -----------------------------
try:
    banner = Image.open("obesity-eating-illustration-png.jpg")
except:
    banner = None

# -----------------------------
# ADVANCED MEDICAL UI CSS
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #eef2f3, #d9e4f5);
    font-family: 'Segoe UI', sans-serif;
}
.block-container {
    background-color: #ffffff;
    padding: 2.5rem;
    border-radius: 20px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.08);
}
h1 {
    color: #0f4c75;
    text-align: center;
}
.stButton>button {
    background: linear-gradient(to right, #0f4c75, #3282b8);
    color: white;
    font-size: 18px;
    padding: 12px;
    border-radius: 12px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
if banner:
    st.image(banner, use_column_width=True)

st.markdown("""
<h1>🍔 Obesity Prediction System</h1>
<p style="text-align:center;color:#555;">
AI-powered health risk assessment using Machine Learning
</p>
<hr>
""", unsafe_allow_html=True)

# -----------------------------
# User Inputs
# -----------------------------
st.subheader("🧾 Personal Health Information")

col1, col2 = st.columns(2)

with col1:
    Age = st.slider("🎂 Age", 10, 80, 25)
    Height = st.number_input("📏 Height (cm)", 100, 220, 170)
    Weight = st.number_input("⚖️ Weight (kg)", 30, 200, 65)

with col2:
    CAEC = st.selectbox(
        "🍟 Eating Between Meals",
        ["no", "Sometimes", "Frequently", "Always"]
    )
    CALC = st.selectbox(
        "🍺 Alcohol Consumption",
        ["no", "Sometimes", "Frequently", "Always"]
    )
    st.info("💡 Balanced diet + exercise reduce obesity risk.")

# -----------------------------
# Prepare Input Data
# -----------------------------
input_data = pd.DataFrame(0, index=[0], columns=features)

input_data["Age"] = Age
input_data["Height"] = Height
input_data["Weight"] = Weight

for col, val in zip(["CAEC", "CALC"], [CAEC, CALC]):
    col_name = f"{col}_{val}"
    if col_name in input_data.columns:
        input_data[col_name] = 1

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Predict Health Status"):

    input_scaled = pd.DataFrame(
        scaler.transform(input_data),
        columns=features
    )

    prediction = model.predict(input_scaled)[0]

    height_m = Height / 100
    bmi = round(Weight / (height_m ** 2), 2)

    if bmi < 18.5:
        bmi_status = "Underweight"
    elif bmi < 25:
        bmi_status = "Normal"
    elif bmi < 30:
        bmi_status = "Overweight"
    else:
        bmi_status = "Obese"

    st.markdown("---")
    st.subheader("📊 Health Analysis Report")

    colA, colB = st.columns(2)
    with colA:
        st.success(f"**Obesity Level**\n\n{prediction}")
    with colB:
        st.info(f"**BMI Score**\n\n{bmi} ({bmi_status})")

    health_tips = {
        "Insufficient_Weight": "🥗 Increase calorie intake with nutritious food.",
        "Normal_Weight": "✅ Maintain your healthy lifestyle.",
        "Overweight_Level_I": "🚶 Increase daily physical activity.",
        "Overweight_Level_II": "🏃 Diet control and exercise recommended.",
        "Obesity_Type_I": "⚠️ Lifestyle changes needed.",
        "Obesity_Type_II": "❗ Consult a healthcare professional.",
        "Obesity_Type_III": "🚨 Immediate medical attention required."
    }

    st.warning("💡 Personalized Recommendation")
    st.write(health_tips.get(prediction, "Consult a healthcare professional."))

    st.balloons()
