@echo off
setlocal enabledelayedexpansion

if not exist ".venv\" (
    echo Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo Failed to create virtual environment
        pause
        exit /b 1
    )
) else (
    echo Virtual environment already exists
)

call .venv\Scripts\activate.bat >nul 2>&1
if errorlevel 1 (
    echo Failed to activate virtual environment
    pause
    exit /b 1
)

echo Installing packages...
pip install -r requirements.txt --quiet --no-warn-conflicts --disable-pip-version-check
if errorlevel 1 (
    echo Failed to install packages from requirements.txt
    pause
    exit /b 1
)

echo Ready! Virtual environment activated
cmd /k