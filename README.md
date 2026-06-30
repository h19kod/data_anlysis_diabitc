# 🏥 Diabetes Prediction System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-green.svg)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<p align="center">
  <img src="https://img.icons8.com/color/96/000000/diabetes.png" alt="Diabetes Icon"/>
</p>

## 🎯 نظرة عامة | Overview

مشروع شامل للتنبؤ بمرض السكري باستخدام تقنيات التعلم الآلي، مع تحليل متقدم للبيانات السريرية ونموذج دقيق للكشف عن خطر الإصابة بالسكري.

**A comprehensive diabetes prediction project using Machine Learning, with advanced clinical data analysis and an accurate model for diabetes risk detection.**

---

## 📊 النتائج الرئيسية | Key Results

- ✅ **دقة النموذج**: 92.3% (Accuracy)
- ✅ **الحساسية**: 84.6% (Recall - لا نفوّت مصاباً)
- ✅ **ROC-AUC**: 0.956
- ✅ **F1-Score**: 0.79
- ✅ **تحسين الـ Recall**: +23.1% بعد SMOTE
- ✅ **المتغيرات المستخدمة**: 14 مؤشر سريري

---

## 📁 هيكل المشروع | Project Structure

```
diabetes-prediction-system/
│
├── 📓 notebooks/
│   └── diabetes_analysis.ipynb          # تحليل شامل (26 خلية)
│
├── 📊 data/                              # مجلد البيانات
│   └── diabetes.csv                     # البيانات الأصلية
│
├── 🤖 models/                            # مجلد النماذج
│   ├── diabetes_scaler.pkl              # Scaler المدرب
│   └── tuned_diabetes_model.pkl         # النموذج المدرب
│
├── 📄 README.md                         # هذا الملف
├── 📋 requirements.txt                  # المتطلبات
└── 🚀 .gitignore                        # استبعاد الملفات
```

---

## 🚀 البدء السريع | Quick Start

### 1. المتطلبات | Prerequisites

```bash
# Python 3.8 أو أحدث
python --version

# تثبيت المكتبات
pip install -r requirements.txt
```

### 2. تشغيل الـ Notebook

```bash
# تشغيل Jupyter Notebook
jupyter notebook notebooks/diabetes_analysis.ipynb
```

### 3. استخدام النموذج

```python
import joblib
import pandas as pd

# تحميل النموذج والـ Scaler
model = joblib.load('models/tuned_diabetes_model.pkl')
scaler = joblib.load('models/diabetes_scaler.pkl')

# بيانات مريض جديد
patient_data = {
    'chol': 180, 'stab.glu': 85, 'hdl': 55, 'ratio': 3.2, 'age': 28,
    'gender': 'female', 'height': 65, 'weight': 130, 'frame': 'medium',
    'bp.1s': 115, 'bp.1d': 75, 'bp.2s': 112, 'bp.2d': 74,
    'waist': 28, 'hip': 36, 'time.ppn': 120
}

# التنبؤ
prediction = predict_patient_diabetes(patient_data, model, scaler)
```

---

## 📋 المتطلبات | Requirements

```txt
numpy>=1.21.0
pandas>=1.3.0
scikit-learn>=0.24.0
matplotlib>=3.4.0
seaborn>=0.11.0
xgboost>=1.5.0
imbalanced-learn>=0.8.0
shap>=0.41.0
joblib>=1.0.0
jupyter>=1.0.0
ipykernel>=6.0.0
```

---

## 📓 محتويات الـ Notebook | Notebook Contents

### الخلايا الرئيسية:

1. **تحميل البيانات** - استيراد dataset UVA Diabetes
2. **فحص البيانات** - Shape، Data Types، Missing Values
3. **توزيع النتائج** - Countplot للـ Outcome
4. **هندسة الميزات** - حساب BMI، معالجة Missing Values
5. **التصور البياني** - Histograms، Boxplots
6. **تدريب النموذج الأساسي** - Random Forest Baseline
7. **أهمية الميزات** - Feature Importance Plot
8. **مصفوفة الارتباك** - Confusion Matrix
9. **منحنى ROC** - ROC Curve & AUC
10. **تحسين النموذج** - Grid Search Hyperparameter Tuning
11. **مقارنة النماذج** - Random Forest vs Logistic Regression vs XGBoost
12. **دالة التنبؤ** - Inference Pipeline
13. **تحليل الأخطاء** - False Negatives & False Positives
14. **توازن الفئات** - SMOTE Oversampling
15. **تحليل SHAP** - Model Interpretability

---

## 🤖 النماذج المستخدمة | Models Used

| النموذج | الدقة | Recall | ROC-AUC |
|---------|-------|--------|---------|
| **Random Forest (Tuned)** | 92.3% | 84.6% | 0.956 |
| **Random Forest (Baseline)** | 91.0% | 61.5% | 0.956 |
| **XGBoost** | 92.3% | 69.2% | 0.955 |
| **Logistic Regression** | 89.7% | 53.8% | 0.929 |

---

## 🔬 المنهجية | Methodology

### 1. **جمع البيانات**
- Dataset: UVA Diabetes Dataset
- الحجم: 403 مريض
- المتغيرات: 14 مؤشر سريري

### 2. **معالجة البيانات**
- إزالة القيم المفقودة (Median Imputation)
- حساب BMI من الوزن والطول
- One-Hot Encoding للمتغيرات التصنيفية
- Standard Scaling

### 3. **تدريب النموذج**
- Train/Test Split (80/20)
- Stratified Sampling
- Cross-Validation (5-fold)
- Hyperparameter Tuning (Grid Search)

### 4. **تحسين الأداء**
- SMOTE Oversampling لمعالجة Class Imbalance
- تحسين Recall من 61.5% إلى 84.6%
- تحسين F1-Score من 0.70 إلى 0.79

### 5. **تفسير النموذج**
- SHAP Values لتفسير التنبؤات
- Feature Importance Analysis
- Error Analysis (False Negatives)

---

## 📈 النتائج التفصيلية | Detailed Results

### قبل SMOTE:
```
Accuracy: 91.0%
Recall: 61.5%
F1-Score: 0.70
False Negatives: 5
```

### بعد SMOTE:
```
Accuracy: 92.3%
Recall: 84.6%
F1-Score: 0.79
False Negatives: 2
```

### التحسين:
- ✅ **Recall**: +23.1%
- ✅ **Caught Cases**: من 8 إلى 11 من 13
- ✅ **F1-Score**: +0.09

---

## 🎯 حالات الاستخدام | Use Cases

1. **الكشف المبكر** - تحديد المرضى المعرضين للخطر
2. **الرعاية الوقائية** - تخصيص خطط العلاج
3. **الأبحاث السريرية** - تحليل العوامل المؤثرة
4. **تعليم الأطباء** - فهم أهمية المؤشرات

---

## 🛠️ التقنيات المستخدمة | Technologies

- **Python 3.8+**
- **Jupyter Notebook**
- **scikit-learn** - Machine Learning
- **XGBoost** - Gradient Boosting
- **imbalanced-learn** - SMOTE
- **SHAP** - Model Interpretability
- **pandas** - Data Manipulation
- **matplotlib/seaborn** - Visualization

---

## 📊 الميزات الرئيسية | Key Features

- ✅ تحليل شامل للبيانات السريرية
- ✅ مقارنة متعددة النماذج
- ✅ معالجة Class Imbalance
- ✅ تفسير النموذج باستخدام SHAP
- ✅ تحليل الأخطاء (Error Analysis)
- ✅ دالة تنبؤ جاهزة للاستخدام

---

## 🚧 القيود | Limitations

- Dataset صغير (403 مريض فقط)
- يحتاج إلى بيانات أكبر للتحقق
- النموذج يحتاج إلى تحديث دوري
- يجب التحقق من قبل أطباء قبل الاستخدام السريري

---

## 🔮 التطورات المستقبلية | Future Developments

- [ ] إضافة المزيد من البيانات
- [ ] تطوير Dashboard تفاعلي
- [ ] نشر كـ REST API
- [ ] تطبيق موبايل
- [ ] التكامل مع EHR Systems

---

## 📝 الترخيص | License

MIT License - انظر ملف LICENSE للتفاصيل

---

## 👨‍💻 المؤلف | Author

H19KOD

---

## 🙏 شكر وتقدير | Acknowledgments

- UVA Diabetes Dataset
- scikit-learn Team
- Kaggle Community

---

## 📞 التواصل | Contact

للاستفسارات والمساهمات، يرجى فتح Issue في المستودع.

---

**🎉 شكراً لاستخدامك مشروع التنبؤ بالسكري!**
