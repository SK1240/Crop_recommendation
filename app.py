import streamlit as st
import pickle
import numpy as np

with open("D:\ds projects\crop_recommendation\knn_crop_model.pkl","rb") as model_file:
    model = pickle.load(model_file)


st.set_page_config(
    page_title="Crop Recommendation",
    page_icon="🌱",
    layout="wide"
)


st.markdown("""
    <style>
        /* Background Gradient */
        body {
            background: linear-gradient(to right, #e3f2fd, #ffffff);
        }
        /* Main Content Box */
        .main {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
            margin: auto;
            max-width: 700px;
        }
        /* Title Styling */
        .title {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: #2c3e50;
            font-family: 'Arial', sans-serif;
        }
        /* Sidebar Input Fields */
        .sidebar .stTextInput, .sidebar .stNumberInput {
            background: rgba(255, 255, 255, 0.8);
            border-radius: 8px;
            border: 1px solid #dfe6e9;
        }
        /* Small Styled Button */
        .stButton>button {
            background: linear-gradient(to right, #2ecc71, #27ae60);
            color: white !important;
            font-size: 16px !important;
            font-weight: bold !important;
            padding: 8px 14px !important;
            border-radius: 8px !important;
            transition: 0.3s ease-in-out;
            border: none !important;
            text-align: center;
            width: auto !important;
            display: block;
            margin: auto;
        }
        .stButton>button:hover {
            transform: scale(1.08);
            background: linear-gradient(to right, #27ae60, #2ecc71);
            box-shadow: 0px 3px 8px rgba(46, 204, 113, 0.3);
        }
        /* Result Box */
        .result-box {
            margin-top: 20px;
            padding: 15px;
            background: #e8f5e9;
            border-left: 6px solid #2ecc71;
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            color: #2c3e50;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>🌾 Crop Recommendation System</h1>", unsafe_allow_html=True)
st.write("🔍 **Enter the soil conditions below to find the best suitable crop for farming.**")

st.sidebar.header("📝 Enter Soil Conditions")

N = st.sidebar.number_input("Nitrogen (N)", min_value=0, max_value=150, value=50, step=1)
P = st.sidebar.number_input("Phosphorus (P)", min_value=0, max_value=150, value=50, step=1)
K = st.sidebar.number_input("Potassium (K)", min_value=0, max_value=150, value=50, step=1)
temperature = st.sidebar.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0, step=0.1)
humidity = st.sidebar.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0, step=0.1)
ph = st.sidebar.number_input("pH Level", min_value=0.0, max_value=14.0, value=6.5, step=0.1)
rainfall = st.sidebar.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=200.0, step=0.1)

def predict_crop():
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    predicted_crop = model.predict(input_data)[0]
    return predicted_crop

if st.button("🌱 Recommend Crop"):
    crop_result = predict_crop()
    st.markdown(f"<div class='result-box'>✅ Recommended Crop: <b>{crop_result.upper()}</b></div>", unsafe_allow_html=True)


st.markdown("<br><br><center>⚡ Powered by <b>Machine Learning</b></center>", unsafe_allow_html=True)
