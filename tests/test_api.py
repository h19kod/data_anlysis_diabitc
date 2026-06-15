"""
Tests for API endpoints
"""
import pytest
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


class TestRoot:
    """Test root endpoint"""
    
    def test_root(self):
        """Test root endpoint returns correct data"""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json()["message"] == "Diabetes Prediction API"
    
    def test_health_check(self):
        """Test health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"


class TestPrediction:
    """Test prediction endpoint"""
    
    def test_valid_prediction(self):
        """Test valid prediction request"""
        data = {
            "age": 45,
            "glucose": 110,
            "bmi": 25.0,
            "blood_pressure": 80
        }
        response = client.post("/predict", json=data)
        assert response.status_code == 200
        
        result = response.json()
        assert "risk_score" in result
        assert "risk_category" in result
        assert "probability" in result
        assert 0 <= result["probability"] <= 1
    
    def test_invalid_age(self):
        """Test prediction with invalid age"""
        data = {
            "age": 150,  # Invalid
            "glucose": 110,
            "bmi": 25.0,
            "blood_pressure": 80
        }
        response = client.post("/predict", json=data)
        # Should still work but with high risk
        assert response.status_code == 200
    
    def test_missing_field(self):
        """Test prediction with missing field"""
        data = {
            "age": 45,
            "glucose": 110
            # Missing bmi and blood_pressure
        }
        response = client.post("/predict", json=data)
        assert response.status_code == 422  # Validation error
    
    def test_stats_endpoint(self):
        """Test stats endpoint"""
        response = client.get("/stats")
        assert response.status_code == 200
        assert "total_patients" in response.json()


class TestDocs:
    """Test documentation endpoints"""
    
    def test_swagger_ui(self):
        """Test Swagger UI is accessible"""
        response = client.get("/docs")
        assert response.status_code == 200
    
    def test_redoc(self):
        """Test ReDoc is accessible"""
        response = client.get("/redoc")
        assert response.status_code == 200
