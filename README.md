# Offline Notes Sync App

A minimal web-based note application with offline support and automatic sync.

## Features
- ✅ Create and store notes locally in browser (localStorage)
- ✅ Offline support - works without internet
- ✅ Auto-syncs when reconnected to server
- ✅ Works on Web, iOS, Android (any device with a browser)
- ✅ Central server database (JSON)
- ✅ Real-time sync status indicator
- ✅ Minimal UI and code footprint

## Setup

### Backend (Python Server)

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python server.py
```

The server will start on `http://localhost:5000`

### Frontend (Web App)

1. Open `index.html` in your browser
2. Or open it on the same network using the server's IP address

## How It Works

1. **Frontend**: 
   - Notes are saved to browser localStorage
   - UI shows sync status: SYNCED / PENDING / OFFLINE
   - Auto-syncs every 30 seconds when online

2. **Backend**:
   - Python Flask server
   - Notes stored in `notes.json` file
   - Merges notes by timestamp (keeps newest version)
   - Accessible from any device on the network

## API Endpoints

- `POST /api/sync` - Sync notes with server
- `GET /api/notes` - Get all notes from server

## File Structure
```
.
├── server.py          # Flask backend
├── index.html         # Frontend (single HTML file)
├── notes.json         # Server database (auto-created)
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Usage Tips

- Notes are auto-saved to localStorage
- Click "Sync with Server" to manually trigger sync
- Auto-sync runs every 30 seconds when connected
- Status indicator shows connection state:
  - **SYNCED** (green) - Connected and synced
  - **PENDING** (orange) - Changes waiting to sync
  - **OFFLINE** (red) - No connection

## Multi-Device Access

1. Find your computer's IP address (e.g., 192.168.x.x)
2. On another device, open: `http://<your-ip>:5000`
3. All devices will sync notes automatically

## Notes

- Very minimal implementation (~200 lines total)
- No database setup needed (uses JSON file)
- Simple CORS setup allows access from any origin
- Perfect for local network note sharing
