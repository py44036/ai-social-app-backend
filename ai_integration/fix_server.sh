#!/bin/bash
echo "🔴 Stopping all processes using port 8000..."
sudo lsof -t -i:8000 | xargs -r sudo kill -9

echo "✅ Port 8000 is now free."

echo "🔄 Restarting FastAPI Server..."
uvicorn main:app --host 0.0.0.0 --port 8000 --reload