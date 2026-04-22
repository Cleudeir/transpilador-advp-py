@echo off
set BACKEND_PORT=8040
set FRONTEND_PORT=8041
set OLD_PORT=3000

echo 🚀 Starting ADVP-Python Development Environment...

echo 🛑 Stopping old servers...
:: Process discovery and termination by port is complex in plain CMD, 
:: so we'll target the known process names.
taskkill /F /IM python.exe /T 2>nul
taskkill /F /IM node.exe /T 2>nul

echo 📡 Starting Backend (FastAPI)...
if exist .venv (
    start /B cmd /c ".venv\Scripts\activate && python -m pyadvpl.engine.server"
) else (
    start /B cmd /c "python -m pyadvpl.engine.server"
)

echo 💻 Starting Frontend (Vite/React)...
cd frontend
:: We run the frontend in the foreground so the terminal stays open
npm run dev -- --host 0.0.0.0
cd ..

echo ✅ Servers initialized.
pause
