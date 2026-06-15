"""
FastAPI API for Diabetes Prediction System
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import joblib
import os
from typing import Dict, List, Optional
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Diabetes Prediction API",
    description="API for predicting diabetes risk based on patient data",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class PatientData(BaseModel):
    age: int
    glucose: float
    bmi: float
    blood_pressure: int
    
    class Config:
        schema_extra = {
            "example": {
                "age": 45,
                "glucose": 110,
                "bmi": 25.0,
                "blood_pressure": 80
            }
        }

# Response model
class PredictionResponse(BaseModel):
    risk_score: int
    risk_category: str
    probability: float
    recommendations: List[str]
    checkup_frequency: str

# Load model
model = None

def load_model():
    """Load the ML model"""
    global model
    model_path = "models/diabetes_model.pkl"
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        logger.info("Model loaded successfully")
    else:
        logger.warning("Model not found, using rule-based prediction")
        model = None

@app.on_event("startup")
async def startup_event():
    load_model()

@app.get("/")
async def root():
    return {
        "message": "Diabetes Prediction API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model_loaded": model is not None}

@app.post("/predict", response_model=PredictionResponse)
async def predict(patient: PatientData):
    try:
        # Calculate risk score
        risk_score = calculate_risk_score(
            patient.age,
            patient.glucose,
            patient.bmi,
            patient.blood_pressure
        )
        
        # Get prediction
        if model:
            features = np.array([[patient.age, patient.glucose, patient.bmi, patient.blood_pressure]])
            probability = model.predict_proba(features)[0][1]
        else:
            probability = min(risk_score / 12 * 0.95, 0.95)
        
        # Determine category
        category, recommendations, checkup = get_risk_category(risk_score)
        
        return PredictionResponse(
            risk_score=risk_score,
            risk_category=category,
            probability=round(probability, 2),
            recommendations=recommendations,
            checkup_frequency=checkup
        )
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stats")
async def get_stats():
    return {
        "total_patients": 1000,
        "diabetes_rate": 0.485,
        "model_accuracy": 0.902,
        "model_auc": 0.90
    }

def calculate_risk_score(age, glucose, bmi, bp):
    """Calculate risk score"""
    score = 0
    if age >= 65: score += 3
    elif age >= 45: score += 2
    elif age >= 35: score += 1
    
    if glucose >= 200: score += 4
    elif glucose >= 126: score += 3
    elif glucose >= 100: score += 2
    
    if bmi >= 35: score += 3
    elif bmi >= 30: score += 2
    elif bmi >= 25: score += 1
    
    if bp >= 140: score += 2
    elif bp >= 120: score += 1
    
    return score

def get_risk_category(score):
    """Get risk category and recommendations"""
    if score >= 7:
        return (
            "Very High",
            ["Immediate HbA1c test", "Endocrinologist consultation", "Monthly follow-up"],
            "Every 3-4 weeks"
        )
    elif score >= 5:
        return (
            "High",
            ["Check every 3 months", "Diet consultation", "Exercise 150 min/week"],
            "Every 3 months"
        )
    elif score >= 3:
        return (
            "Medium",
            ["Check every 6 months", "Improve diet", "Regular physical activity"],
            "Every 6 months"
        )
    else:
        return (
            "Low",
            ["Annual checkup", "Maintain healthy weight", "Regular exercise"],
            "Annually"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
