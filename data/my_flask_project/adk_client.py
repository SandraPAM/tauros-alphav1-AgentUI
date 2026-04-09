import requests
import os
#from dotenv import load_dotenv

#load_dotenv()

class ADKClient:
    def __init__(self):
        self.base_url = os.getenv("ADK_BASE_URL")
        self.agent_name = os.getenv("AGENT_NAME")

    def create_session(self, user_id):
        url = f"{self.base_url}/apps/{self.agent_name}/users/{user_id}/sessions"
        response = requests.post(url)
        return response.json().get("id")

    def send_message(self, user_id, session_id, text):
        url = f"{self.base_url}/run"
        payload = {
            "app_name": self.agent_name,
            "user_id": user_id,
            "session_id": session_id,
            "new_message": {
                "parts": [{"text": text}]
            }
        }
        response = requests.post(url, json=payload)
        return response.json()