"""
Script to train and save the diabetes prediction model
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os
import yaml
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_config():
    """Load configuration from YAML file"""
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)


def load_data(config):
    """Load and preprocess data"""
    logger.info("Loading data...")
    data_path = config['data']['path']
    df = pd.read_excel(data_path)
    
    # Extract features and target
    features = config['data']['features']
    target = config['data']['target']
    
    X = df[features]
    y = df[target]
    
    logger.info(f"Data loaded: {len(df)} samples")
    return X, y


def train_model(X, y, config):
    """Train the model"""
    logger.info("Training model...")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=config['model']['test_size'],
        random_state=config['model']['random_state'],
        stratify=y
    )
    
    # Initialize model
    model = RandomForestClassifier(
        n_estimators=config['model']['n_estimators'],
        random_state=config['model']['random_state'],
        n_jobs=-1
    )
    
    # Train
    model.fit(X_train, y_train)
    
    # Cross-validation
    cv_scores = cross_val_score(
        model, X_train, y_train,
        cv=config['model']['cv_folds'],
        scoring='roc_auc'
    )
    
    logger.info(f"CV AUC: {cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")
    
    # Evaluate on test set
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    logger.info(f"Test Accuracy: {accuracy:.3f}")
    logger.info("\nClassification Report:")
    logger.info(classification_report(y_test, y_pred))
    
    return model


def save_model(model, config):
    """Save the trained model"""
    model_path = os.path.join(config['paths']['models'], 'diabetes_model.pkl')
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    
    joblib.dump(model, model_path)
    logger.info(f"Model saved to {model_path}")


def main():
    """Main training pipeline"""
    logger.info("=" * 50)
    logger.info("Diabetes Prediction Model Training")
    logger.info("=" * 50)
    
    # Load config
    config = load_config()
    
    # Load data
    X, y = load_data(config)
    
    # Train model
    model = train_model(X, y, config)
    
    # Save model
    save_model(model, config)
    
    logger.info("=" * 50)
    logger.info("Training completed successfully!")
    logger.info("=" * 50)


if __name__ == "__main__":
    main()
