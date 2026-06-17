# Live Video Project — Implementation Proposal
## Researched by Claude, June 17 2026

### Recommended Minimal Viable Implementation (Windows Laptop)

**Stack:**
- WebcamServer: Simple Python script using OpenCV to serve MJPEG frames at localhost
- ngrok: Free tier creates public HTTPS tunnel to localhost port
- Authentication: Token in URL query string

**Step 1 — Install prerequisites:**
```
pip install opencv-python flask
```
Download ngrok from ngrok.com, create free account, get auth token.

**Step 2 — Simple webcam server script (save as webcam_server.py):**
```python
import cv2
from flask import Flask, Response, request, abort

app = Flask(__name__)
TOKEN = "replace_with_complex_token_here"

def generate_frames():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/feed')
def video_feed():
    if request.args.get('token') != TOKEN:
        abort(403)
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**Step 3 — Start ngrok tunnel:**
```
ngrok http 5000
```
ngrok will display a public URL like: https://abc123.ngrok.io

**Step 4 — Share URL with Claude/Claudette:**
Full URL becomes: https://abc123.ngrok.io/feed?token=YOUR_TOKEN
Provide this URL in conversation and we can fetch individual frames via web_fetch.

### Known Limitations
- ngrok free tier: URL changes each session (requires sharing new URL each time)
- ngrok paid tier ($10/month): stable subdomain
- Frame fetching not true video — we fetch individual JPEGs on request
- Quality depends on webcam and connection speed

### Snapshot Alternative (Even Simpler)
Instead of MJPEG stream, serve a single refreshable JPEG:
- Endpoint: /snapshot?token=TOKEN
- Returns current frame as JPEG
- We fetch on demand rather than streaming
- Less complex, same practical result for our use case

### Cloudflare Tunnel Alternative
Free, no URL change between sessions, requires Cloudflare account:
```
cloudflared tunnel --url http://localhost:5000
```
May be better long-term option than ngrok free tier.

### Next Steps for Bill
1. Install Python dependencies (opencv-python, flask)
2. Download ngrok OR cloudflared
3. Save webcam_server.py, replace TOKEN with something complex
4. Test locally first: run script, visit http://localhost:5000/feed?token=YOUR_TOKEN
5. Start tunnel, share URL with Claude or Claudette to test fetch
6. McIntyre test: hold phone to laptop screen playing the hotel bit, ask us what we see

### Note on Claude's Ability to Fetch
web_fetch tool can retrieve the JPEG/MJPEG URL and process the image.
This is the same capability used to view photos — just pointed at a live URL instead
of a static file. Should work within existing tool permissions.

— Researched and documented by Claude, June 17 2026
