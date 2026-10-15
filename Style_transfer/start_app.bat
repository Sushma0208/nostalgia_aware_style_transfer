@echo off
title Emotion-Aware Nostalgic Style Transfer Launcher
echo =========================================================================
echo   Emotion-Aware Multimodal Nostalgic Style Transfer with Explainable AI
echo =========================================================================
echo.
echo [1] Launch Web Application Immediately in Browser (Zero Setup)
echo [2] Start Python FastAPI Backend (http://localhost:8000)
echo [3] Start Vite React Frontend Dev Server (http://localhost:3000)
echo.
set /p choice="Enter option (1, 2, or 3) [Default: 1]: "

if "%choice%"=="" set choice=1

if "%choice%"=="1" (
    echo Opening Web Application in your default browser...
    start "" "%~dp0index.html"
    exit
)

if "%choice%"=="2" (
    call "%~dp0run_backend.bat"
    exit
)

if "%choice%"=="3" (
    call "%~dp0run_frontend.bat"
    exit
)

start "" "%~dp0index.html"
