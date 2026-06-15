@echo off
chcp 65001 >nul
echo ========================================
echo   GitHub Push Script
echo ========================================
echo.

REM Change to project directory
cd /d "%~dp0"

echo Step 1: Initializing Git...
git init

echo.
echo Step 2: Configuring user...
git config user.email "user@example.com"
git config user.name "User"

echo.
echo Step 3: Adding remote origin...
git remote remove origin 2>nul
git remote add origin https://github.com/h19kod/data_anlysis_diabitc.git

echo.
echo Step 4: Staging files...
git add .

echo.
echo Step 5: Creating commit...
git commit -m "Initial commit: Complete diabetes prediction system with 25 sections, README, and requirements"

echo.
echo Step 6: Setting branch to main...
git branch -M main

echo.
echo ========================================
echo   Repository ready for push!
echo ========================================
echo.
echo Now run: git push -u origin main
echo.
echo IMPORTANT: When prompted for password,
echo use your GitHub Personal Access Token!
echo.
echo Get your token from:
echo https://github.com/settings/tokens
echo.
echo ========================================

pause
