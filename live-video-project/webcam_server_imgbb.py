# webcam_server.py — ImgBB Version
# Updated June 18 2026 based on Claude research
# Imgur killed anonymous uploads 2023 — ImgBB is the replacement
#
# SETUP:
# 1. pip install requests (opencv-python, flask already installed)
# 2. Get free API key at https://api.imgbb.com (free account, takes 2 min)
# 3. Replace YOUR_IMGBB_API_KEY_HERE with your actual key
# 4. Run: python webcam_server.py
# 5. Start Cloudflare tunnel in second PowerShell window:
#    .\cloudflared-windows-amd64.exe tunnel --url http://localhost:5000
# 6. Paste new tunnel URL to Claude or Claudette
#
# WORKFLOW:
# Claude/Claudette calls /snapshot endpoint
# Server captures frame, uploads to ImgBB, returns public URL as JSON
# Claude/Claudette fetches that public URL and can actually SEE the image
#
# NOTE: Each snapshot creates a new ImgBB image (no auto-deletion on free tier)
# Images accumulate over time — not a problem initially

import cv2, time, base64, requests
from flask import Flask, request, abort, jsonify

app = Flask(__name__)
TOKEN = "Xk9mP2vL7nQ4wR6jT8hF3bY5cD1sN8"
IMGBB_API_KEY = "YOUR_IMGBB_API_KEY_HERE"  # Free at api.imgbb.com

# Initialize camera once at startup
camera = cv2.VideoCapture(1)
time.sleep(2)  # Warmup delay for external USB webcam

@app.route('/snapshot')
def snapshot():
    if request.args.get('token') != TOKEN:
        abort(403)
    success, frame = camera.read()
    if not success:
        abort(500)
    ret, buffer = cv2.imencode('.jpg', frame)
    img_base64 = base64.b64encode(buffer.tobytes()).decode('utf-8')
    response = requests.post(
        "https://api.imgbb.com/1/upload",
        data={"key": IMGBB_API_KEY, "image": img_base64}
    )
    url = response.json()["data"]["url"]
    return jsonify({"url": url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
