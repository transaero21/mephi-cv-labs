@echo off
setlocal enabledelayedexpansion

FSUTIL DIRTY query %SystemDrive% >NUL || (
    PowerShell "Start-Process -FilePath cmd.exe -Args '/C CHDIR /D %CD% & ""%0" %*"' -Verb RunAs"
    EXIT
)

if not exist "img" (
    mkdir "img"
    break> "img\.gitkeep"
)

for /l %%i in (1,1,16) do (
    set "folder=%%i"
    if %%i lss 10 set "folder=0%%i"

    if not exist "!folder!" (
        mkdir "!folder!"
    )

    if exist "!folder!" (
        pushd "!folder!"
        
        dir /b /a | findstr /v "img" | findstr /v ".gitkeep" >nul
        if errorlevel 1 (
            break> .gitkeep
        ) else (
            if exist ".gitkeep" (
                del .gitkeep
            )
        )

        if not exist "img" (
            mklink /D "img" "..\img" >nul 2>&1
        )
        
        popd
    )
)

echo Folder structure created

call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo Failed to activate virtual environment
    pause
    exit /b 1
)

pip install autopep8 >nul 2>&1
if errorlevel 1 (
    echo Failed to install autopep8
    pause
    exit /b 1
)

for /f "delims=" %%i in ('dir /b /s *.py ^| findstr /v /i "\\.venv\\"') do (
    echo Formatting: %%i
    python -m autopep8 --in-place --aggressive --aggressive "%%i"
)

echo All Python files formatted

pause