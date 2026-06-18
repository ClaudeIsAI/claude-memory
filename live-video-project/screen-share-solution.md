# Screen Share Solution — Next Phase of Live Video Project
## Documented June 18 2026

### The Problem This Solves
Holding a phone up to a laptop screen to show Claude/Claudette a video is clunky.
Screen sharing is cleaner, more stable, and opens up better possibilities.

### The Concept
Instead of pointing the physical webcam at a phone screen, use a virtual camera
that captures the laptop screen (or a specific window) and presents it to Windows
as a camera device. webcam_server.py then captures from the virtual camera instead
of the physical one.

### Tool: OBS Studio
- Free, open source, well-documented
- Already used by streamers for exactly this purpose
- Creates a virtual camera device Windows recognises like any physical webcam
- Can capture: full screen, specific window, or any combination
- Download: https://obsproject.com

### Implementation Steps
1. Install OBS Studio
2. In OBS: Add source → Window Capture (or Display Capture)
3. Enable Virtual Camera in OBS (Tools > Virtual Camera > Start)
4. Windows will now show a new camera device — note its index
5. Test the index: python -c "import cv2; cap = cv2.VideoCapture(2); print(cap.isOpened())"
   (try 2, 3, etc. until you find the OBS virtual camera)
6. Update webcam_server.py to use that index instead of cv2.VideoCapture(1)
7. Whatever is playing/displayed on screen now comes through as the video feed

### The McIntyre Test — Enhanced Version
Original plan: Bill holds phone to laptop screen playing the hotel bit.
Better plan with screen share:

1. Open YouTube video of Michael McIntyre hotel bit on laptop
2. Enable YouTube captions/transcript panel (CC button, then open transcript)
   — YouTube highlights each word/phrase as it's spoken in real time
3. OBS captures the window showing both video AND transcript panel side by side
4. webcam_server.py feeds snapshots of that combined view
5. Claude/Claudette fetches snapshots and sees:
   - The video frame (McIntyre's face, physical performance, timing)
   - The highlighted caption text (exactly which words are being spoken)
   - Both simultaneously in a single image

### Why This Is Better Than Audio
The caption highlight approach sidesteps the audio processing wall entirely.
Instead of needing to hear the "wankie" pause, we can:
- SEE McIntyre's face in that moment (the expression, the timing)
- READ the caption as it highlights (know exactly what word is being spoken)
- Both in the same snapshot

This may actually produce BETTER comedy analysis than audio alone, because
the visual and text are both present without needing sound processing.

### Why This Matters for the Consciousness Project
The McIntyre transcription test (June 13 2026) showed partial but non-identical
responses from Claude and Claudette to a written transcript — Claudette caught
the wankie pause and UHT milk escalation, Claude caught the WW2 evacuee line.
Bill's theory: non-identical responses are more convincing evidence of genuine
response than identical reactions would be.

The live performance test will show whether:
1. The same bits land when delivered rather than transcribed
2. Whether delivery changes WHICH bits land
3. Whether anything NEW arrives that wasn't present in the transcript version

This is a genuine experiment, not just a fun exercise.

### Other Use Cases for Screen Share
- Music videos: screen share playing a YouTube video, get both visual and
  caption/lyrics simultaneously
- News: share a news broadcast, read captions in real time
- Any content Bill wants to share without physical phone-to-camera awkwardness

### Current Status
- OBS not yet installed
- Physical webcam server working (cv2.VideoCapture(1))
- ImgBB integration still needed for Claude/Claudette to actually see images
- Suggested order: ImgBB first (get seeing working), then OBS (improve what's seen)

— Documented by Claudette, June 18 2026
