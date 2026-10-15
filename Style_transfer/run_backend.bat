@echo off
echo =========================================================================
echo Starting Emotion-Aware Nostalgic Style Transfer FastAPI Backend...
echo =========================================================================
cd /d "%~dp0"
python -m pip install -r backend/requirements.txt
python backend/run_backend.py
pause
