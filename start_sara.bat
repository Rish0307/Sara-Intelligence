@echo off
title Sara Intelligence Launcher
color 0A

echo ===================================================
echo               SARA INTELLIGENCE
echo ===================================================
echo.
echo Starting Python Brain (Sara-Brain) in a new window...
start "Sara Brain (Python)" cmd /k "cd Sara-Brain && venv\Scripts\activate && python server.py"

echo Starting User Interface (Sara-UI) in a new window...
start "Sara UI (Electron)" cmd /k "cd Sara-UI && npm run dev"

echo.
echo Both services have been launched! You can close this window.
timeout /t 5 >nul
