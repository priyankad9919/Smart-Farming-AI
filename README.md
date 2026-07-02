# 🌾 Smart Farming AI

An AI-powered Smart Farming Assistant that combines **Machine Learning**, **IBM watsonx.ai**, and **Retrieval-Augmented Generation (RAG)** to help farmers make informed agricultural decisions.

The application predicts the most suitable crop based on soil and environmental parameters and provides document-grounded farming guidance using IBM watsonx.ai and a SmartFarmingVectorIndex.

---

## 🚀 Features

- 🌱 Crop Recommendation using Machine Learning (Random Forest)
- 🤖 AI-powered Farming Assistant using IBM watsonx.ai
- 📚 Retrieval-Augmented Generation (RAG)
- 🔍 SmartFarmingVectorIndex for document retrieval
- 🌾 Detailed farming guide after crop prediction
- 🦠 Pest and disease management recommendations
- 💧 Irrigation guidance
- 🌿 Fertilizer recommendations
- 🏛️ Government agricultural schemes
- 🖥️ Interactive Streamlit web application

---

## 🏗️ System Architecture

```text
Farmer
   │
   ▼
Enter Soil Parameters
(N, P, K, Temperature, Humidity, pH, Rainfall)
   │
   ▼
Random Forest Model
   │
   ▼
Recommended Crop
   │
   ▼
User Query
   │
   ▼
SmartFarmingVectorIndex
(32 Agricultural Documents)
   │
   ▼
Retrieval-Augmented Generation (RAG)
   │
   ▼
IBM watsonx.ai
(Meta Llama 3.3 70B Instruct)
   │
   ▼
Grounded Farming Advice
```

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Machine Learning
- Random Forest Classifier
- Scikit-learn
- Pandas
- NumPy

### IBM Cloud
- IBM watsonx.ai
- SmartFarmingVectorIndex
- AI Service Deployment
- IBM Cloud Lite

### AI
- Meta Llama 3.3 70B Instruct
- Retrieval-Augmented Generation (RAG)

### Python Libraries
- ibm-watsonx-ai
- python-dotenv
- requests
- joblib

---

## 📂 Project Structure

```
Smart-Farming-AI/
│
├── app.py
├── predictor.py
├── granite_chat.py
├── train_model.py
├── weather.py (optional)
├── model.pkl
├── scaler.pkl
├── crop_recommendation.csv
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Farming-AI.git
```

Navigate to the project

```bash
cd Smart-Farming-AI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file

```env
IBM_API_KEY=YOUR_API_KEY

IBM_PROJECT_ID=YOUR_PROJECT_ID

IBM_SPACE_ID=YOUR_SPACE_ID

IBM_DEPLOYMENT_ID=YOUR_DEPLOYMENT_ID

IBM_URL=https://us-south.ml.cloud.ibm.com
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. User enters soil parameters.
2. Machine Learning model predicts the best crop.
3. The predicted crop is sent to IBM watsonx.ai.
4. SmartFarmingVectorIndex retrieves relevant agricultural documents.
5. Retrieval-Augmented Generation (RAG) supplies contextual information to the foundation model.
6. Meta Llama 3.3 generates grounded farming recommendations.
7. The AI response is displayed inside the Streamlit application.

---

## 🎯 Future Enhancements

- 🌦️ Real-time Weather API Integration
- 🗣️ Multilingual Support
- 🎤 Voice-Based Farming Assistant
- 📱 Android Application
- 🛰️ Satellite-Based Crop Monitoring
- 💹 Live Mandi Price Integration
- 📸 Crop Disease Detection using Deep Learning

---

## 🌟 Key Highlights

- IBM watsonx.ai Integration
- Retrieval-Augmented Generation (RAG)
- SmartFarmingVectorIndex
- AI Service Deployment
- Machine Learning Crop Prediction
- Interactive Streamlit UI
- Document-Grounded AI Responses

---

## 👩‍💻 Author

**Priyanka Dey**

---

## 📜 License

This project is developed for educational and hackathon purposes.