import json
import os
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

DB_FILE = 'notes.json'

def load_notes():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_notes(notes):
    with open(DB_FILE, 'w') as f:
        json.dump(notes, f, indent=2)

@app.route('/api/sync', methods=['POST'])
def sync_notes():
    data = request.json
    client_notes = data.get('notes', {})
    
    server_notes = load_notes()
    
    # Merge notes: keep newest version based on timestamp
    for note_id, client_note in client_notes.items():
        if note_id not in server_notes:
            server_notes[note_id] = client_note
        else:
            server_version_time = server_notes[note_id].get('updated', 0)
            client_version_time = client_note.get('updated', 0)
            
            # Keep the version with the newer timestamp
            if client_version_time > server_version_time:
                server_notes[note_id] = client_note
    
    # IMPORTANT: Keep deleted notes in database for sync tracking (don't remove them)
    save_notes(server_notes)
    
    # But return only active notes to client
    active_notes = {k: v for k, v in server_notes.items() if not v.get('deleted')}
    
    return jsonify({
        'success': True,
        'notes': active_notes,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/notes', methods=['GET'])
def get_notes():
    notes = load_notes()
    # Filter out deleted notes
    active_notes = {k: v for k, v in notes.items() if not v.get('deleted')}
    return jsonify(active_notes)

@app.route('/')
def index():
    return send_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
