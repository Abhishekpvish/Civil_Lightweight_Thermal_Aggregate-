import streamlit as st
import pandas as pd
import joblib
import os
from sklearn.exceptions import NotFittedError

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best_rf_pipeline.joblib")

INPUT_FIELDS = [
    ("PCM_pct", "PCM percentage"),
    ("Nano_pct", "Nano additive percentage"),
    ("Density_kgm3", "Density in kg/m^3"),
    ("Porosity_pct", "Porosity percentage"),
    ("Thermal_Conductivity_WmK", "Thermal conductivity (W/mK)"),
    ("Specific_Heat_JkgK", "Specific heat (J/kgK)"),
    ("Latent_Heat_kJkg", "Latent heat (kJ/kg)"),
    ("Orientation", "Orientation (e.g. horizontal/vertical)"),
    ("Ambient_Temp_C", "Ambient temperature (°C)")
]

OUTPUT_FIELDS = [
    "Thermal_Delay_min",
    "Attenuation_Rate_pct",
    "Energy_Saving_pct",
    "Compressive_Strength_MPa"
]

st.set_page_config(page_title="Civil Lightweight Aggregate Predictor", layout="centered")
st.title("PCM Impregnated Light weight Aggregate Concrete")

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}")
    return joblib.load(MODEL_PATH)

try:
    model = load_model()
    st.success("Model loaded successfully")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.header("Enter Input Parameters")

with st.form("prediction_form"):
    inputs = {}
    for key, hint in INPUT_FIELDS:
        if key == "Orientation":
            inputs[key] = st.text_input(
                f"{key} – {hint}", "horizontal"
            ).strip().lower()
        else:
            inputs[key] = st.number_input(
                f"{key} – {hint}", value=0.0
            )
    submitted = st.form_submit_button("Predict Outputs")

if submitted:
    X = pd.DataFrame([inputs])
    try:
        preds = model.predict(X)
        pred_dict = dict(zip(OUTPUT_FIELDS, preds[0]))
        st.subheader("Predicted Outputs")
        for k, v in pred_dict.items():
            st.metric(k, f"{v:.4f}")
    except NotFittedError:
        st.error("The loaded model is not fitted.")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

