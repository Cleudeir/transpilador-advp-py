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
start /B cmd /c "cd backend && .venv\Scripts\activate && python main.py"

echo 💻 Starting Frontend (Vite/React)...
cd frontend
:: We run the frontend in the foreground so the terminal stays open
npm run dev -- --host 0.0.0.0

echo ✅ Servers initialized.
pause
