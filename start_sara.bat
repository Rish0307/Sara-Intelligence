@echo off
title Sara Intelligence Launcher
color 0A

echo ===================================================
echo               SARA INTELLIGENCE
echo ===================================================
echo.
echo Starting Python Brain (Mark-XXXIX) in a new window...
start "Sara Brain (Python)" cmd /k "cd Mark-XXXIX && venv\Scripts\activate && python server.py"

echo Starting User Interface (IRIS-AI) in a new window...
start "Sara UI (Electron)" cmd /k "cd IRIS-AI && npm run dev"

echo.
echo Both services have been launched! You can close this window.
timeout /t 5 >nul
