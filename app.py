import streamlit as st
from predictor import predict_crop
from granite_chat import get_farming_advice

st.set_page_config(
    page_title="Smart Farming AI",
    page_icon="🌾",
    layout="centered"
)

st.title("🌾 Smart Farming AI")
st.write("AI-powered Crop Recommendation and Smart Farming Assistant")

# ======================================================
# CROP RECOMMENDATION
# ======================================================

st.header("🌱 Crop Recommendation")

N = st.number_input(
    "Nitrogen (N)",
    min_value=0,
    max_value=200,
    value=90
)

P = st.number_input(
    "Phosphorus (P)",
    min_value=0,
    max_value=200,
    value=42
)

K = st.number_input(
    "Potassium (K)",
    min_value=0,
    max_value=200,
    value=43
)

temperature = st.number_input(
    "Temperature (°C)",
    value=20.8,
    format="%.2f"
)

humidity = st.number_input(
    "Humidity (%)",
    value=82.0,
    format="%.2f"
)

ph = st.number_input(
    "Soil pH",
    value=6.5,
    format="%.2f"
)

rainfall = st.number_input(
    "Rainfall (mm)",
    value=202.9,
    format="%.2f"
)

if st.button("🌱 Predict Crop"):

    with st.spinner("Predicting best crop..."):

        crop = predict_crop(
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        )

    st.success(f"✅ Recommended Crop: **{crop.capitalize()}**")

    with st.spinner("Generating AI Farming Guide..."):

        question = f"""
The recommended crop is {crop}.

Give a complete farming guide.

Include:

1. Suitable soil
2. Fertilizers
3. Irrigation
4. Diseases
5. Pest control
6. Government schemes
"""

        advice = get_farming_advice(question)

    st.subheader("🤖 AI Farming Guide")
    st.markdown(advice)

# ======================================================
# SMART FARMING CHATBOT
# ======================================================

st.divider()

st.header("💬 Ask Smart Farming AI")

st.write(
    "Ask any farming-related question. "
    "The AI will answer using the uploaded agricultural knowledge base."
)

user_question = st.text_area(
    "Enter your question",
    placeholder="Example: What is rice blast disease?"
)

if st.button("🤖 Ask AI"):

    if user_question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching knowledge base..."):

            answer = get_farming_advice(user_question)

        st.subheader("🌾 AI Answer")

        st.markdown(answer)