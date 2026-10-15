@echo off
echo =========================================================================
echo Starting Emotion-Aware Nostalgic Style Transfer Vite Frontend...
echo =========================================================================
cd /d "%~dp0\frontend"
call npm install
call npm run dev
pause
