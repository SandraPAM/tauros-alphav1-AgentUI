from flask import Flask, render_template, send_file, request, jsonify
from adk_client import ADKClient

app = Flask(__name__)
client = ADKClient()

@app.route("/")
def index():
    return render_template('index.html')

# Create a global variable to hold the session ID
active_session_id = None

@app.route('/chat', methods=['POST'])
def chat():
    global active_session_id
    data = request.json
    user_id = data.get("user_id", "user123")
    message = data.get("message")

    # Only create a session if we don't have one
    if not active_session_id:
        active_session_id = client.create_session(user_id)
        print(f"--- NEW SESSION STARTED: {active_session_id} ---")
    else:
        print(f"--- REUSING EXISTING SESSION: {active_session_id} ---")

    # Send the message to the SAME session ID
    adk_response = client.send_message(user_id, active_session_id, message)
    
    return jsonify({
        "status": "success",
        "session_id": active_session_id, # Send it back to the UI to verify
        "agent_answer": adk_response
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)