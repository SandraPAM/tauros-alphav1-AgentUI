# Flask Wrapper UI

This is the frontend and API bridge for the Google ADK agent.

## Setup
1. Ensure the ADK server is running on port 8000
2. Create `.env` file and add:
  * ADK_BASE_URL=http://localhost:8000
  * AGENT_NAME=my_agent
3. Start Flask:
```bash
python app.py
```
4. Access the UI at http://localhost:5000.
