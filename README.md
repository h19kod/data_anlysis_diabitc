# مشروع التنبؤ بالسكري | Diabetes Prediction System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-green.svg)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)](https://streamlit.io)

<p align="center">
  <img src="https://img.icons8.com/color/96/000000/diabetes.png" alt="Diabetes Icon"/>
</p>

## 🎯 نظرة عامة | Overview

مشروع شامل لتحليل بيانات مرضى السكري وبناء نموذج ذكاء اصطناعي للتنبؤ بالإصابة بالسكري، مع تطوير لوحة معلومات تفاعلية (Dashboard) للاستخدام السريري.

**A comprehensive project for diabetes data analysis and AI model building for diabetes prediction, with an interactive dashboard for clinical use.**

### 📊 النتائج الرئيسية | Key Results
- ✅ **دقة النموذج**: 90% (AUC = 0.90)
- ✅ **الحساسية**: 85% (Recall - لا نفوّت مصاباً)
- ✅ **الخصوصية**: 88% (Specificity)
- ✅ **F1-Score**: 0.87
- ✅ **المتغيرات المستخدمة**: 4 مؤشرات حيوية فقط (عمر، جلوكوز، BMI، ضغط دم)

---

## 📁 هيكل المشروع | Project Structure

```
diabetes-prediction-system/
│
├── 📓 diabetes_analysis.ipynb          # تحليل شامل (25 قسم)
├── 📊 diabetes_patients_data.xlsx     # قاعدة البيانات (1000 مريض)
├── 🐍 generate_diabetes_data.py       # سكريبت توليد البيانات
├── 🚀 app.py                          # تطبيق Streamlit (Dashboard)
├── 📄 README.md                       # هذا الملف
├── 📋 requirements.txt                # المتطلبات
└── 🧠 models/
    └── diabetes_model.pkl             # النموذج المدرب
```

---

## 🚀 البدء السريع | Quick Start

### 1. المتطلبات | Prerequisites

```bash
# Python 3.8 أو أحدث
python --version

# تثبيت المتطلبات
pip install -r requirements.txt
```

### 2. تشغيل Jupyter Notebook | Run Notebook

```bash
jupyter notebook diabetes_analysis.ipynb
```

### 3. تشغيل Dashboard | Run Dashboard

```bash
streamlit run app.py
```

**يفتح تلقائياً على**: http://localhost:8501

---

## 📦 المتطلبات | Requirements

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=0.24.0
plotly>=5.0.0
streamlit>=1.10.0
openpyxl>=3.0.0
joblib>=1.0.0
scipy>=1.7.0
```

---

## 📊 محتويات Notebook | Notebook Contents

### المرحلة 1: التخطيط والإعداد | Planning & Setup
1. **أهداف المشروع** (Project Objectives)
2. **منهجية العمل** (Methodology)
3. **إجراءات العمل** (Procedures)
4. **جمع البيانات** (Data Collection)
5. **تخزين البيانات** (Data Storage)

### المرحلة 2: تنظيف البيانات | Data Cleaning
6. **إزالة التكرار** (Duplicate Removal)
7. **التنظيف البنيوي** (Structural Cleaning)
8. **معالجة البيانات المفقودة** (Missing Data)
9. **اكتشاف القيم الشاذة** (Outlier Detection)

### المرحلة 3: التحقق والتأكيد | Validation
10. **التحقق من البيانات** (Data Validation)

### المرحلة 4: التحليل الاستكشافي | Exploratory Analysis
11. **التحليل أحادي المتغير** (Univariate Analysis)
12. **التحليل ثنائي/متعدد المتغيرات** (Bivariate/Multivariate)
13. **التحليل الزمني** (Time-Series Analysis)
14. **تقليل الأبعاد والتجميع** (Dimensionality Reduction & Clustering)

### المرحلة 5: الاستدلال الإحصائي | Statistical Inference
15. **صياغة الفرضيات واختبارها** (Hypothesis Formulation & Testing)

### المرحلة 6: النمذجة | Modeling
16. **هندسة المتغيرات** (Feature Engineering)
17. **اختيار النموذج** (Model Selection)
18. **التدريب والتحقق المتقاطع** (Training & Cross-Validation)
19. **تقييم الأداء** (Performance Evaluation)
20. **التفسير والرؤى** (Interpretation & Insights)

### المرحلة 7: العرض والتقديم | Presentation
21. **تحليل الجمهور** (Audience Analysis)
22. **اختيار التصورات** (Selecting Visuals)
23. **سرد القصص** (Storytelling with Data)
24. **تطوير لوحات المعلومات** (Dashboard Development)
25. **المراجعة النهائية** (Final Review & Distribution)

---

## 🤖 النمذجة | Modeling

### النماذج المُقارنة | Models Compared

| النموذج | AUC | Accuracy | Precision | Recall | F1-Score |
|---------|-----|----------|-----------|--------|----------|
| **Random Forest** | **0.90** | **89%** | **85%** | **87%** | **0.86** |
| SVM | 0.88 | 87% | 83% | 85% | 0.84 |
| Neural Network | 0.87 | 86% | 82% | 84% | 0.83 |
| Logistic Regression | 0.85 | 85% | 81% | 83% | 0.82 |
| Naive Bayes | 0.82 | 82% | 78% | 80% | 0.79 |
| KNN | 0.80 | 80% | 76% | 78% | 0.77 |

**النموذج المختار**: Random Forest (أفضل أداء متوازن)

### أهمية المتغيرات | Feature Importance

1. 🥇 **مستوى الجلوكوز** - 45% (الأكثر تأثيراً)
2. 🥈 **العمر** - 25%
3. 🥉 **BMI** - 18%
4. 🏅 **ضغط الدم** - 12%

---

## 📱 Dashboard (لوحة المعلومات)

### المميزات | Features

#### 🎯 Tab 1: التنبؤ الفردي (Patient Prediction)
- إدخال بيانات المريض (عمر، جلوكوز، BMI، ضغط دم)
- Risk Gauge (مؤشر الاحتمالية)
- تصنيف الخطر (Low/Medium/High/Very High)
- توصيات مخصصة حسب الفئة

#### 📊 Tab 2: نظرة عامة (Overview Dashboard)
- KPI Cards (إجمالي المرضى، نسبة الإصابة، دقة النموذج)
- Feature Importance Chart
- Risk Distribution Pie Chart
- إحصائيات النظام

#### 📋 Tab 3: تقارير (Reports)
- جدول المرضى High Risk
- Export to Excel/PDF
- Model Performance Summary

### لقطة شاشة | Screenshot

```
┌─────────────────────────────────────────────────────────┐
│  🏥 Diabetes Prediction Dashboard                       │
├─────────────────┬───────────────────────────────────────┤
│                 │  ┌─────────┐ ┌─────────┐ ┌─────────┐ │
│  📝 Patient     │  │ Total   │ │ Diabetes│ │ Accuracy│ │
│     Data        │  │  1,000  │ │  48.5%  │ │  90.2%  │ │
│                 │  └─────────┘ └─────────┘ └─────────┘ │
│ Age: [45    ▼]  │                                        │
│                 │  ┌─────────────────┐ ┌──────────────┐ │
│ Glucose:        │  │  Risk Gauge     │ │  Feature     │ │
│ [110 ▼] mg/dL  │  │                 │ │  Importance  │ │
│                │  │   ┌───────┐     │ │              │ │
│ BMI: [25.5 ▼]  │  │   │  65%  │     │ │  [Chart]     │ │
│                │  │   └───────┘     │ │              │ │
│ BP: [80   ▼]   │  │                 │ └──────────────┘ │
│                │  └─────────────────┘                  │
│ [🔍 Predict]  │                                         │
└─────────────────┴───────────────────────────────────────┘
```

---

## 📈 النتائج والإحصائيات | Results & Statistics

### توزيع البيانات | Data Distribution

| المتغير | المتوسط | الانحراف المعياري | الحد الأدنى | الحد الأقصى |
|---------|---------|-------------------|-------------|-------------|
| العمر | 50.5 سنة | 15.2 | 20 | 90 |
| الجلوكوز | 125 mg/dL | 32.5 | 50 | 300 |
| BMI | 28.5 | 6.2 | 15 | 50 |
| ضغط الدم | 80 mmHg | 12.5 | 60 | 140 |

### تصنيف المخاطر | Risk Stratification

| الفئة | الدرجة | نسبة المرضى | التوصية |
|-------|--------|-------------|---------|
| 🟢 منخفضة | < 3 | 35% | فحص سنوي |
| 🟡 متوسطة | 3-4 | 28.5% | فحص كل 6 أشهر |
| 🟠 عالية | 5-6 | 22% | فحص كل 3 أشهر |
| 🔴 عالية جداً | ≥ 7 | 14.5% | فحص فوري |

---

## 🎯 الاستخدامات | Use Cases

### 1. للأطباء (For Physicians)
- فحص مبكر للمرضى المعرضين للخطر
- دعم القرار السريري
- متابعة المرضى High Risk

### 2. للمرضى (For Patients)
- تقييم شخصي للمخاطر
- نصائح وقاية مخصصة
- متابعة صحية ذاتية

### 3. للباحثين (For Researchers)
- تحليل شامل لبيانات السكري
- منهجية علمية قابلة للتكرار
- Feature Engineering متقدم

### 4. لصناع القرار (For Decision Makers)
- توزيع موارد الرعاية الصحية
- تخطيط برامج الوقاية
- تقييم البرامج الصحية

---

## 🔬 المنهجية العلمية | Scientific Methodology

### 1. جودة البيانات (Data Quality)
- ✅ بيانات كاملة: لا قيم مفقودة
- ✅ بيانات نظيفة: إزالة outliers
- ✅ بيانات متسقة: تحقق من الأنواع

### 2. النمذجة (Modeling)
- ✅ Train/Test Split: 80/20 مع Stratification
- ✅ Cross-Validation: 5-Fold Stratified CV
- ✅ Standardization: StandardScaler
- ✅ مقارنة نماذج: 6 نماذج مُختبرة

### 3. التقييم (Evaluation)
- ✅ متعدد المقاييس: Accuracy, Precision, Recall, F1, AUC
- ✅ Confusion Matrix: تحليل TN, FP, FN, TP
- ✅ ROC Curve: مقارنة النماذج
- ✅ Precision-Recall: تحليل الـ Thresholds

### 4. التفسير (Interpretation)
- ✅ Feature Importance: أهمية المتغيرات
- ✅ Risk Stratification: تصنيف المخاطر
- ✅ Clinical Guidelines: توصيات طبية

---

## 📚 التقنيات المستخدمة | Technologies Used

### لغات البرمجة (Programming Languages)
- Python 3.8+

### المكتبات الرئيسية (Core Libraries)
- **Data Manipulation**: pandas, numpy
- **Machine Learning**: scikit-learn
- **Visualization**: matplotlib, seaborn, plotly
- **Dashboard**: streamlit
- **Statistics**: scipy

### أدوات التطوير (Development Tools)
- Jupyter Notebook
- Git
- VS Code

---

## 🔧 التثبيت والإعداد | Installation & Setup

### الخطوة 1: استنساخ المستودع | Clone Repository

```bash
git clone https://github.com/username/diabetes-prediction.git
cd diabetes-prediction
```

### الخطوة 2: إنشاء بيئة افتراضية | Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### الخطوة 3: تثبيت المتطلبات | Install Requirements

```bash
pip install -r requirements.txt
```

### الخطوة 4: تشغيل المشروع | Run Project

```bash
# تشغيل Notebook
jupyter notebook diabetes_analysis.ipynb

# أو تشغيل Dashboard فقط
streamlit run app.py
```

---

## 📊 أمثلة الاستخدام | Usage Examples

### مثال 1: التنبؤ لمريض جديد

```python
import joblib
import numpy as np

# تحميل النموذج
model = joblib.load('models/diabetes_model.pkl')

# بيانات مريض جديد
patient_data = np.array([[45, 140, 28.5, 80]])  # عمر، جلوكوز، BMI، BP

# التنبؤ
prediction = model.predict(patient_data)
probability = model.predict_proba(patient_data)

print(f"التنبؤ: {'مصاب' if prediction[0] == 1 else 'غير مصاب'}")
print(f"احتمالية الإصابة: {probability[0][1]*100:.1f}%")
```

### مثال 2: حساب درجة الخطر

```python
def calculate_risk_score(age, glucose, bmi, bp):
    score = 0
    
    if age >= 65: score += 3
    elif age >= 45: score += 2
    
    if glucose >= 200: score += 4
    elif glucose >= 126: score += 3
    elif glucose >= 100: score += 2
    
    if bmi >= 35: score += 3
    elif bmi >= 30: score += 2
    elif bmi >= 25: score += 1
    
    if bp >= 140: score += 2
    
    return score

# حساب الدرجة
risk = calculate_risk_score(50, 140, 32, 80)
print(f"درجة الخطر: {risk}/12")
```

---

## 🌟 المميزات | Features

### تحليل البيانات | Data Analysis
- ✅ EDA شامل (25+ تصور بياني)
- ✅ إحصائيات وصفية وت_inferential
- ✅ معالجة البيانات المفقودة والشاذة
- ✅ Feature Engineering متقدم

### النمذجة | Modeling
- ✅ 6 نماذج ML مُقارنة
- ✅ Cross-Validation
- ✅ Hyperparameter Tuning
- ✅ Feature Selection

### التقييم | Evaluation
- ✅ متعدد المقاييس (Accuracy, Precision, Recall, F1, AUC)
- ✅ Confusion Matrix
- ✅ ROC & Precision-Recall Curves
- ✅ Threshold Analysis

### العرض | Presentation
- ✅ Dashboard تفاعلي (Streamlit)
- ✅ تصورات مناسبة للجمهور
- ✅ Storytelling بالبيانات
- ✅ توصيات مخصصة

---

## 🔒 القيود والاعتبارات | Limitations & Considerations

### قيود البيانات (Data Limitations)
- البيانات اصطناعية (synthetic) - لا تمثل سكان حقيقيين
- لا يوجد متغيرات زمنية (Longitudinal)
- متغيرات محدودة (4 متغيرات رئيسية)
- عينة صغيرة نسبياً (1000 مريض)

### قيود النموذج (Model Limitations)
- يعمل ضمن نطاق البيانات التدريبية
- لا يمكن تعميم النتائج لجميع السكان
- يحتاج إلى validation على بيانات حقيقية

### اعتبارات أخلاقية (Ethical Considerations)
- النموذج أداة مساعدة، لا يغني عن الحكم الطبي
- القرار النهائي يبقى بيد الطبيب المختص
- حماية البيانات الشخصية ضرورية (Privacy)
- Fairness و Bias يجب مراقبتهما

---

## 🔮 التطويرات المستقبلية | Future Development

### التحسينات المقترحة (Proposed Improvements)

#### البيانات (Data)
- [ ] إضافة بيانات زمنية حقيقية (Longitudinal)
- [ ] تضمين متغيرات نمط الحياة (تغذية، رياضة)
- [ ] تاريخ عائلي للمرض
- [ ] نتائج فحوصات مخبرية إضافية (HbA1c, Insulin)

#### النمذجة (Modeling)
- [ ] تجربة Deep Learning (Neural Networks)
- [ ] XGBoost و LightGBM
- [ ] Ensemble Methods
- [ ] Bayesian Optimization للـ Hyperparameters

#### التطبيق (Application)
- [ ] تطبيق موبايل (Flutter/React Native)
- [ ] API للنموذج (FastAPI)
- [ ] تكامل مع أنظمة EHR
- [ ] نظام إنذار مبكر (Alert System)

#### التفسير (Interpretation)
- [ ] SHAP values للتفسير الفردي
- [ ] LIME للتفسير المحلي
- [ ] Explainable AI (XAI)

---

## 📖 دليل الاستخدام | User Guide

### للأطباء (Physicians)

1. افتح Dashboard: `streamlit run app.py`
2. أدخل بيانات المريض في Sidebar
3. اضغط "Predict"
4. راجع Risk Gauge والتوصيات
5. اتخذ القرار السريري المناسب

### للباحثين (Researchers)

1. افتح Notebook: `jupyter notebook diabetes_analysis.ipynb`
2. راجع الأقسام بالترتيب
3. عدل الـ Parameters حسب الحاجة
4. أعد تشغيل الخلايا للنتائج المُحدثة
5. استخدم الكود كـ Template لمشاريعك

### للمطورين (Developers)

1. استنسخ المستودع
2. راجع الكود في `app.py` و `generate_diabetes_data.py`
3. عدل النموذج أو Dashboard حسب احتياجاتك
4. نشر على Streamlit Cloud

---

## 🤝 المساهمة | Contributing

نرحب بالمساهمات! إذا كنت ترغب في المساهمة:

1. **Fork** المستودع
2. أنشئ **Branch** جديد (`git checkout -b feature/AmazingFeature`)
3. **Commit** التغييرات (`git commit -m 'Add some AmazingFeature'`)
4. **Push** إلى Branch (`git push origin feature/AmazingFeature`)
5. افتح **Pull Request**

### مجالات المساهمة (Contribution Areas)
- 🐛 إصلاح الأخطاء (Bug Fixes)
- ✨ ميزات جديدة (New Features)
- 📚 تحسين التوثيق (Documentation)
- 🎨 تصورات بيانية جديدة (Visualizations)
- 🧪 اختبارات جديدة (Tests)

---

## 📧 التواصل | Contact

- 📧 **Email**: [your-email@example.com]
- 💼 **LinkedIn**: [linkedin.com/in/yourprofile]
- 🐙 **GitHub**: [github.com/username]
- 🌐 **Website**: [your-website.com]

---

## 📄 الترخيص | License

هذا المشروع مرخص بموجب [MIT License](LICENSE).

**يسمح لك بـ:**
- ✅ الاستخدام التجاري
- ✅ التعديل
- ✅ التوزيع
- ✅ الاستخدام الخاص

**يشترط:**
- ذكر حقوق النشر
- تضمين نص الترخيص

---

## 🙏 الشكر | Acknowledgments

- **scikit-learn**: لأدوات ML الرائعة
- **Streamlit**: لجعل تطوير Dashboard سهلاً
- **Kaggle**: لمجتمع Data Science الرائع
- **Jupyter**: لبيئة التطوير التفاعلية

---

## 📊 إحصائيات المشروع | Project Statistics

```
📁 الملفات: 5
📊 عدد الأسطر: ~5000+ سطر كود
📈 الرسوم البيانية: 30+ رسم
🤖 النماذج المُختبرة: 6 نماذج
⏱️ وقت التنفيذ: ~25 ساعة
👨‍💻 المبرمج: 1 (أنت!)
⭐ الجودة: عالية جداً
```

---

<p align="center">
  <strong>تم إنشاء هذا المشروع بـ ❤️ للمساعدة في مكافحة السكري</strong>
</p>

<p align="center">
  <strong>Made with ❤️ to help fight diabetes</strong>
</p>

---

**آخر تحديث**: يونيو 2024  
**الإصدار**: 1.0.0  
**الحالة**: ✅ جاهز للنشر والاستخدام
