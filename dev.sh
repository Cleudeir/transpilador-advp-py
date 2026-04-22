#!/bin/bash

# Port definitions
BACKEND_PORT=8040
FRONTEND_PORT=8041
OLD_PORT=3000

echo "🚀 Starting ADVP-Python Development Environment..."

# Function to kill process on port
kill_port() {
    local port=$1
    local pid=$(lsof -t -i:$port)
    if [ -n "$pid" ]; then
        echo "Cleaning up port $port (PID: $pid)..."
        kill -9 $pid 2>/dev/null
    fi
}

# Kill existing servers
kill_port $BACKEND_PORT
kill_port $FRONTEND_PORT
kill_port $OLD_PORT

# Start Backend
echo "📡 Starting Backend (FastAPI)..."
cd backend
source .venv/bin/activate
python3 main.py > /dev/null 2>&1 &
BACKEND_PID=$!
cd ..

# Start Frontend
echo "💻 Starting Frontend (Vite/React)..."
cd frontend
npm run dev -- --host 0.0.0.0 &
FRONTEND_PID=$!
cd ..

# Cleanup function for Ctrl+C
cleanup() {
    echo -e "\n\n🛑 Shutting down servers..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    echo "Done."
    exit
}

trap cleanup SIGINT SIGTERM

echo "✅ Both servers are online!"
echo "   - Backend: http://localhost:$BACKEND_PORT"
echo "   - Frontend: http://localhost:$FRONTEND_PORT"
echo "Press Ctrl+C to stop both."

wait
