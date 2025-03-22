#!/bin/bash
export PYTHONPATH=/Users/pradeepyadav/AI-SOCIAL-APP
fuser -k 8000/tcp  # Pehle se chal raha server stop karein
uvicorn ai_integration.server_scripts.main:app --host 0.0.0.0 --port 8000 --reload˝cd ~/AI-SOCIAL-APP/ai_integration/server_scripts