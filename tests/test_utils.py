"""
Tests for utility functions
"""
import pytest
from src.utils import calculate_risk_score, get_risk_category


class TestRiskCalculation:
    """Test risk score calculation"""
    
    def test_low_risk(self):
        """Test low risk patient"""
        score = calculate_risk_score(age=25, glucose=90, bmi=22, bp=70)
        assert score < 3
    
    def test_medium_risk(self):
        """Test medium risk patient"""
        score = calculate_risk_score(age=45, glucose=110, bmi=28, bp=80)
        assert 3 <= score < 5
    
    def test_high_risk(self):
        """Test high risk patient"""
        score = calculate_risk_score(age=65, glucose=160, bmi=32, bp=90)
        assert 5 <= score < 7
    
    def test_very_high_risk(self):
        """Test very high risk patient"""
        score = calculate_risk_score(age=70, glucose=220, bmi=38, bp=150)
        assert score >= 7
    
    def test_edge_cases(self):
        """Test boundary values"""
        # Minimum values
        score_min = calculate_risk_score(age=20, glucose=50, bmi=15, bp=60)
        assert score_min >= 0
        
        # Maximum values
        score_max = calculate_risk_score(age=90, glucose=300, bmi=50, bp=200)
        assert score_max <= 12


class TestRiskCategory:
    """Test risk category classification"""
    
    def test_low_category(self):
        """Test low risk category"""
        category, prob, color = get_risk_category(2)
        assert "Low" in category
        assert color == "#00cc00"
    
    def test_medium_category(self):
        """Test medium risk category"""
        category, prob, color = get_risk_category(4)
        assert "Medium" in category
    
    def test_high_category(self):
        """Test high risk category"""
        category, prob, color = get_risk_category(6)
        assert "High" in category
    
    def test_very_high_category(self):
        """Test very high risk category"""
        category, prob, color = get_risk_category(8)
        assert "Very High" in category
        assert color == "#ff0000"
    
    def test_probability_range(self):
        """Test probability is within valid range"""
        for score in range(0, 13):
            _, prob, _ = get_risk_category(score)
            assert 0 <= prob <= 1
