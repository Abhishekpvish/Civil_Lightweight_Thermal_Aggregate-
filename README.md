# Lightweight_Thermal_Aggregate-
AI-powered Streamlit web application to predict thermal delay, attenuation rate, energy savings, and compressive strength of civil lightweight thermal aggregates using machine learning.

# Civil Lightweight Thermal Aggregate – AI Prediction System

This project is an **AI-based machine learning system** developed to predict the **thermal and mechanical performance of civil lightweight thermal aggregates** made using **Pima stone, epoxy coating, and paraffin wax (PCM)**.

The system predicts:
- ✅ Thermal Delay (min)
- ✅ Attenuation Rate (%)
- ✅ Energy Saving (%)
- ✅ Compressive Strength (MPa)

based on user-provided material and environmental inputs.

The application is deployed using **Streamlit** for real-time prediction through a web interface.

---

## 🎯 Project Objectives

- To develop a **lightweight aggregate with thermal resistance properties**.
- To analyze the **thermal behavior of Pima stone with PCM and nano-material additives**.
- To build an **AI model that predicts performance characteristics** based on experimental input data.
- To provide a **user-friendly web interface** for easy prediction and validation.

---

## 🧪 Input Parameters

The AI model takes the following inputs:

| Parameter | Description |
|-----------|-------------|
| PCM_pct | Phase Change Material percentage |
| Nano_pct | Nano additive percentage |
| Density_kgm3 | Density (kg/m³) |
| Porosity_pct | Porosity (%) |
| Thermal_Conductivity_WmK | Thermal conductivity (W/mK) |
| Specific_Heat_JkgK | Specific heat (J/kgK) |
| Latent_Heat_kJkg | Latent heat (kJ/kg) |
| Orientation | Orientation of material |
| Ambient_Temp_C | Ambient temperature (°C) |

---

## 📊 Output Parameters (Predictions)

The model predicts:

- **Thermal Delay (minutes)**
- **Attenuation Rate (%)**
- **Energy Saving (%)**
- **Compressive Strength (MPa)**

---

## 🤖 Machine Learning Model

- Algorithm Used: **Random Forest Regressor**
- Type: **Multi-Output Regression**
- Preprocessing:
  - Standard Scaling for numerical features
  - One-Hot Encoding for orientation
- Model is saved as:

  Civil_Lightweight_Thermal_Aggregate/

  │

  ├── app.py # Streamlit web application
  
  ├── requirements.txt # Python dependencies
  
  ├── README.md # Project documentation

  └── models/

     └── best_rf_pipeline.joblib # Trained ML model

---

## ⚙️ Installation & Execution

### ✅ Run Locally

      pip install -r requirements.txt
      streamlit run app.py

------------------------------------------------------

📦 Python Dependencies

Listed in requirements.txt:

streamlit
scikit-learn
pandas
numpy
joblib

-------------------------------------------

🏗️ Application Domain

Civil Engineering

Sustainable Construction Materials

Thermal Energy Storage

Smart Infrastructure

AI in Construction Technology

--------------------------------------------

👨‍💻 Developed By:

Project Developer:

Abhishek P

Artificial Intelligence & Data Science Student

Sethu Institute of Technology

abhishekpvish223@gmail.com

------------------------------------------------------

🏆 Key Features

✅ AI-based prediction

✅ Real-time web interface

✅ Multi-output regression

✅ Experimental validation support

✅ CSV export functionality

✅ Ready for cloud deployment

-----------------------------

📜 License

This project is developed for educational and academic research purposes.

--------------------

🚀 Future Enhancements

Deep Learning integration

IoT-based real-time data collection

Mobile application version

Advanced material optimization

----------------

⭐ If you like this project, give it a star on GitHub!

---

# ✅ How to Add This to GitHub

In Colab (inside your repo):

      %%writefile README.md
      PASTE THE CONTENT ABOVE HERE


Then:

     !git add README.md
     !git commit -m "Add professional project README"
     !git push -u origin main
