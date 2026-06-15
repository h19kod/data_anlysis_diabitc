"""
Source code package for Diabetes Prediction System
"""

from .utils import calculate_risk_score, get_risk_category
from .data_loader import load_data, preprocess_data
from .model import train_model, predict, evaluate_model

__all__ = [
    'calculate_risk_score',
    'get_risk_category',
    'load_data',
    'preprocess_data',
    'train_model',
    'predict',
    'evaluate_model'
]

__version__ = "1.0.0"
