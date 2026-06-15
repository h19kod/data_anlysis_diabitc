@echo off
chcp 65001 >nul
echo ==========================================
echo   رفع المشروع على GitHub | GitHub Push
echo ==========================================
echo.

REM Change to project directory
cd /d "%~dp0"

echo [1/6] إضافة جميع الملفات...
git add .

echo.
echo [2/6] إنشاء commit...
git commit -m "Complete Diabetes Prediction System v1.0.0

Features:
- 25 comprehensive notebook sections
- Interactive Streamlit dashboard
- FastAPI REST API
- Docker containerization
- CI/CD pipeline
- Complete documentation
- 47-item roadmap (Excel)
- Unit tests
- MLOps ready

Model: Random Forest (90% AUC)
Dataset: 1000 patients
Ready for production deployment."

echo.
echo [3/6] تعيين الفرع الرئيسي...
git branch -M main

echo.
echo [4/6] التحقق من الـ Remote...
git remote -v

echo.
echo [5/6] رفع الملفات على GitHub...
git push -u origin main

echo.
echo ==========================================
if %ERRORLEVEL% == 0 (
    echo   ✅ تم الرفع بنجاح!
    echo ==========================================
    echo.
    echo 🔗 Repository: https://github.com/h19kod/data_anlysis_diabitc
    echo.
    echo 📊 الملفات المرفوعة:
    git ls-files | find /c /v ""
) else (
    echo   ❌ حدث خطأ أثناء الرفع
    echo ==========================================
    echo.
    echo 🔐 تحقق من:
    echo    - GitHub Token صحيح
    echo    - الاتصال بالإنترنت
    echo    - صلاحيات المستودع
)

echo.
echo ==========================================
pause
