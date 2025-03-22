#!/bin/bash

echo "🔄 Checking for process using port 8000..."
PID=$(sudo lsof -t -i:8000) # Port 8000 pe koi process run kar raha hai ya nahi

if [ ! -z "$PID" ]; then
    echo "⚠️ Killing process on port 8000 (PID: $PID)..."
    sudo kill -9 $PID # Process ko forcefully kill karna
    echo "✅ Process $PID killed!"
else
    echo "✅ No process running on port 8000."
fi

echo "🚀 Starting FastAPI Server on port 8000..."
cd ~/AI-SOCIAL-APP/ai_integration
source venv/bin/activate  # Virtual environment activate karein
uvicorn main:app --host 0.0.0.0 --port 8000 --reload & # Background me server start karein
echo "✅ Server restarted successfully!"
