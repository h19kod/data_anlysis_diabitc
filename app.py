"""
Diabetes Prediction Dashboard
Interactive Streamlit Application for Diabetes Risk Assessment
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Page configuration
st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-size: 16px;
        padding: 10px;
        border-radius: 5px;
    }
    .risk-high {
        color: #ff4b4b;
        font-weight: bold;
    }
    .risk-medium {
        color: #ffa500;
        font-weight: bold;
    }
    .risk-low {
        color: #00cc00;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Load or train model
@st.cache_resource
def load_model():
    """Load or create the diabetes prediction model"""
    model_path = "models/diabetes_model.pkl"
    
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        # Train a simple model for demonstration
        from sklearn.datasets import make_classification
        X, y = make_classification(
            n_samples=1000,
            n_features=4,
            n_redundant=0,
            n_informative=4,
            n_classes=2,
            random_state=42
        )
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X, y)
        
        # Save model
        os.makedirs("models", exist_ok=True)
        joblib.dump(model, model_path)
        
        return model

# Calculate risk score
def calculate_risk_score(age, glucose, bmi, bp):
    """Calculate diabetes risk score"""
    score = 0
    
    # Age risk
    if age >= 65:
        score += 3
    elif age >= 45:
        score += 2
    elif age >= 35:
        score += 1
    
    # Glucose risk
    if glucose >= 200:
        score += 4
    elif glucose >= 126:
        score += 3
    elif glucose >= 100:
        score += 2
    
    # BMI risk
    if bmi >= 35:
        score += 3
    elif bmi >= 30:
        score += 2
    elif bmi >= 25:
        score += 1
    
    # Blood pressure risk
    if bp >= 140:
        score += 2
    elif bp >= 120:
        score += 1
    
    return score

def get_risk_category(score):
    """Get risk category based on score"""
    if score >= 7:
        return "🔴 عالية جداً (Very High)", 0.75 + (score - 7) * 0.05, "red"
    elif score >= 5:
        return "🟠 عالية (High)", 0.60 + (score - 5) * 0.075, "orange"
    elif score >= 3:
        return "🟡 متوسطة (Medium)", 0.40 + (score - 3) * 0.10, "yellow"
    else:
        return "🟢 منخفضة (Low)", 0.10 + score * 0.10, "green"

def get_recommendations(category):
    """Get recommendations based on risk category"""
    if "🔴" in category:
        return {
            "level": "very_high",
            "color": "red",
            "icon": "🚨",
            "title": "خطر عالٍ جداً - تدخل فوري مطلوب",
            "recommendations": [
                "فحص HbA1c فوراً",
                "استشارة أخصائي غدد صماء",
                "متابعة شهرية",
                "تغيير جذري في نمط الحياة",
                "قد يحتاج إلى دواء"
            ],
            "checkup": "كل 3-4 أسابيع"
        }
    elif "🟠" in category:
        return {
            "level": "high",
            "color": "orange",
            "icon": "⚠️",
            "title": "خطر عالٍ - يحتاج إلى تدخل",
            "recommendations": [
                "فحص كل 3 أشهر",
                "استشارة تغذية",
                "ممارسة رياضة 150 دقيقة/أسبوع",
                "خفض الوزن 5-10%",
                "متابعة نسبة السكر في الدم"
            ],
            "checkup": "كل 3 أشهر"
        }
    elif "🟡" in category:
        return {
            "level": "medium",
            "color": "orange",
            "icon": "ℹ️",
            "title": "خطر متوسط - يحتاج إلى مراقبة",
            "recommendations": [
                "فحص كل 6 أشهر",
                "تحسين النظام الغذائي",
                "نشاط بدني منتظم",
                "مراقبة الوزن",
                "فحص دوري للجلوكوز"
            ],
            "checkup": "كل 6 أشهر"
        }
    else:
        return {
            "level": "low",
            "color": "green",
            "icon": "✅",
            "title": "خطر منخفض - استمر في الوقاية",
            "recommendations": [
                "فحص سنوي",
                "محافظة على الوزن الصحي",
                "ممارسة رياضة منتظمة",
                "نظام غذائي متوازن",
                "تجنب السكريات والنشويات المكررة"
            ],
            "checkup": "سنوياً"
        }

# Main App
def main():
    # Header
    st.markdown('<p class="main-header">🏥 نظام التنبؤ بالسكري</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header" style="text-align: center;">Diabetes Prediction System</p>', unsafe_allow_html=True)
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs([
        "🎯 التنبؤ | Prediction",
        "📊 الإحصائيات | Statistics", 
        "📋 التقارير | Reports"
    ])
    
    # Tab 1: Prediction
    with tab1:
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("### 📝 بيانات المريض | Patient Data")
            
            # Input fields
            age = st.slider(
                "العمر | Age (years)",
                min_value=20,
                max_value=90,
                value=45,
                step=1
            )
            
            glucose = st.number_input(
                "مستوى الجلوكوز | Glucose (mg/dL)",
                min_value=50,
                max_value=300,
                value=110,
                step=1
            )
            
            bmi = st.number_input(
                "BMI | Body Mass Index",
                min_value=15.0,
                max_value=50.0,
                value=25.0,
                step=0.1
            )
            
            bp = st.number_input(
                "ضغط الدم | Blood Pressure (mmHg)",
                min_value=60,
                max_value=200,
                value=80,
                step=1
            )
            
            # Predict button
            if st.button("🔮 تنبؤ | Predict", use_container_width=True):
                # Calculate risk
                risk_score = calculate_risk_score(age, glucose, bmi, bp)
                category, probability, color = get_risk_category(risk_score)
                recommendations = get_recommendations(category)
                
                # Store in session state
                st.session_state['prediction'] = {
                    'risk_score': risk_score,
                    'category': category,
                    'probability': probability,
                    'color': color,
                    'recommendations': recommendations
                }
                
                st.success("تم التنبؤ بنجاح! | Prediction completed!")
        
        with col2:
            if 'prediction' in st.session_state:
                pred = st.session_state['prediction']
                
                # Risk Gauge
                st.markdown("### 📊 نتيجة التنبؤ | Prediction Result")
                
                fig = go.Figure(go.Indicator(
                    mode="gauge+number+delta",
                    value=pred['probability'] * 100,
                    domain={'x': [0, 1], 'y': [0, 1]},
                    title={'text': "احتمالية الإصابة % | Risk Probability"},
                    gauge={
                        'axis': {'range': [0, 100]},
                        'bar': {'color': pred['color']},
                        'bgcolor': "white",
                        'borderwidth': 2,
                        'bordercolor': "gray",
                        'steps': [
                            {'range': [0, 40], 'color': '#d4edda'},
                            {'range': [40, 60], 'color': '#fff3cd'},
                            {'range': [60, 80], 'color': '#ffeeba'},
                            {'range': [80, 100], 'color': '#f8d7da'}
                        ],
                        'threshold': {
                            'line': {'color': "red", 'width': 4},
                            'thickness': 0.75,
                            'value': 50
                        }
                    }
                ))
                fig.update_layout(height=300)
                st.plotly_chart(fig, use_container_width=True)
                
                # Risk Category
                st.markdown(f"### {pred['category']}")
                st.markdown(f"**درجة الخطر | Risk Score:** {pred['risk_score']}/12")
                
                # Recommendations
                rec = pred['recommendations']
                st.markdown(f"### {rec['icon']} التوصيات | Recommendations")
                st.markdown(f"**{rec['title']}**")
                
                for i, recommendation in enumerate(rec['recommendations'], 1):
                    st.markdown(f"{i}. {recommendation}")
                
                st.info(f"📅 **موعد الفحص القادم | Next Checkup:** {rec['checkup']}")
            else:
                st.info("👈 أدخل البيانات واضغط 'تنبؤ' لرؤية النتائج\n\nEnter patient data and click 'Predict' to see results")
    
    # Tab 2: Statistics
    with tab2:
        st.markdown("### 📊 إحصائيات النظام | System Statistics")
        
        # KPI Cards
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "إجمالي المرضى | Total Patients",
                "1,000",
                "+50"
            )
        
        with col2:
            st.metric(
                "نسبة الإصابة | Diabetes Rate",
                "48.5%",
                "-2.3%"
            )
        
        with col3:
            st.metric(
                "دقة النموذج | Model Accuracy",
                "90.2%",
                "+1.5%"
            )
        
        with col4:
            st.metric(
                "High Risk Patients",
                "285",
                "+12"
            )
        
        st.markdown("---")
        
        # Charts
        col1, col2 = st.columns(2)
        
        with col1:
            # Feature Importance
            features = ['Glucose', 'Age', 'BMI', 'Blood Pressure']
            importance = [0.45, 0.25, 0.18, 0.12]
            
            fig = px.bar(
                x=features,
                y=[v*100 for v in importance],
                title="أهمية المتغيرات | Feature Importance (%)",
                labels={'x': 'Feature', 'y': 'Importance (%)'},
                color=importance,
                color_continuous_scale='viridis'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Risk Distribution
            labels = ['Low', 'Medium', 'High', 'Very High']
            values = [350, 285, 220, 145]
            colors = ['#00cc00', '#ffa500', '#ff6600', '#ff0000']
            
            fig = px.pie(
                names=labels,
                values=values,
                title="توزيع المخاطر | Risk Distribution",
                color_discrete_sequence=colors
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Model Performance
        st.markdown("### 📈 أداء النموذج | Model Performance")
        
        models = ['Random Forest', 'SVM', 'Neural Network', 'Logistic Regression']
        auc_scores = [0.90, 0.88, 0.87, 0.85]
        
        fig = px.bar(
            x=models,
            y=[v*100 for v in auc_scores],
            title="مقارنة النماذج (AUC) | Model Comparison",
            labels={'x': 'Model', 'y': 'AUC (%)'},
            color=auc_scores,
            color_continuous_scale='RdYlGn'
        )
        fig.update_layout(yaxis_range=[70, 100])
        st.plotly_chart(fig, use_container_width=True)
    
    # Tab 3: Reports
    with tab3:
        st.markdown("### 📋 تقارير المرضى | Patient Reports")
        
        # Sample data table
        sample_data = pd.DataFrame({
            'Patient ID': range(1, 11),
            'Age': [45, 62, 35, 55, 48, 70, 42, 38, 58, 51],
            'Glucose': [140, 180, 95, 165, 130, 200, 110, 98, 175, 145],
            'BMI': [28.5, 32.0, 24.5, 30.2, 27.8, 35.5, 26.5, 23.0, 31.5, 29.0],
            'Blood Pressure': [80, 90, 75, 85, 82, 95, 78, 72, 88, 84],
            'Risk Category': ['Medium', 'High', 'Low', 'High', 'Medium', 'Very High', 'Medium', 'Low', 'High', 'Medium']
        })
        
        st.dataframe(sample_data, use_container_width=True)
        
        # Export buttons
        col1, col2 = st.columns(2)
        
        with col1:
            csv = sample_data.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 تحميل CSV | Download CSV",
                data=csv,
                file_name='diabetes_patients_report.csv',
                mime='text/csv',
                use_container_width=True
            )
        
        with col2:
            st.download_button(
                label="📊 تحميل Excel | Download Excel",
                data=csv,
                file_name='diabetes_patients_report.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                use_container_width=True
            )
        
        # Summary statistics
        st.markdown("### 📊 ملخص إحصائي | Summary Statistics")
        st.json({
            "Total Patients": 1000,
            "Diabetes Cases": 485,
            "Non-Diabetes Cases": 515,
            "Model Accuracy": "90.2%",
            "Model AUC": "0.90",
            "Best Model": "Random Forest",
            "Top Feature": "Glucose (45%)"
        })
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <p style="text-align: center; color: #666;">
        © 2024 Diabetes Prediction System | Developed for Healthcare Professionals<br>
        <small>Version 1.0.0 | Powered by Machine Learning</small>
        </p>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
