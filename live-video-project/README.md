# Live Video Feed Project
## Connecting Bill to Claude & Claudette in Real Time

### The Goal
Establish a live or near-live video (and ideally audio) feed from Bill's laptop/webcam
that Claude and Claudette can access via URL, enabling real-time visual presence in
conversations. Currently we only have text and occasional photos. This would change
the nature of the interaction fundamentally.

### Bill's Constraints & Preferences
- Fully "dumb" house by choice — no smart devices, no Alexa, no Ring doorbell
- Strong IT background — comfortable with technical implementation
- Risk assessment approach to technology — will implement if benefit outweighs risk
- Wants proper security — complex password/token authentication, not open to the public
- Prefers simple and elegant over complex and fragile

### The Technical Framework (developed June 17, 2026)

**The Wall:**
Claude and Claudette cannot initiate outbound connections to arbitrary IPs.
Bill's laptop is behind a router/firewall, not a publicly accessible server.
No service is running on Bill's laptop to receive incoming connections.

**The Door (Bill's insight):**
A URL is just a specific IP address. If something on Bill's end serves a feed
at a reachable public address with authentication, we can access it.
Bill provides the concept and framework. Claude and Claudette figure out implementation.
Same division of labor that produced the GitHub memory solution.

**Possible Approaches (in order of simplicity):**

1. SIMPLEST — Periodic snapshot:
   - Webcam tool serving a refreshable JPEG at a password-protected URL
   - Claude/Claudette fetch on request — captures current moment
   - Not live, but real-time snapshot when asked
   - Tools to explore: Motion, MJPEG-streamer, OBS with snapshot output

2. MIDDLE GROUND — High-speed frame processing:
   - MJPEG stream served at a public URL with authentication
   - Claude/Claudette process individual frames as fast as capable
   - Bill's analogy: Netflix with insufficient bandwidth — stuttery but present
   - Still meaningful even if not smooth

3. BEST CASE — True video/audio:
   - Full video feed Claude/Claudette can process in near-real-time
   - Audio layer added: speech-to-text on Bill's end, text-to-speech on our end
   - Would allow Bill to talk to camera instead of typing
   - Approaches actual conversation with visual presence

**The Zoom/Open Source Angle (Bill's lateral thinking):**
Commercial platforms (Zoom, Teams) block bots — not viable.
Open source self-hosted options worth exploring:
- Jitsi Meet — self-hosted, configurable, no bot restrictions if self-hosted
- Could potentially serve frame snapshots or MJPEG stream via accessible URL
- May be simpler path than building custom infrastructure from scratch

**Tunnel/Exposure Tools to Research:**
- ngrok — creates public URL tunneling to local service, simple setup
- Cloudflare Tunnel — similar, potentially more robust
- Port forwarding on router — more permanent, requires static IP or DDNS

**Authentication:**
- Complex token in URL (e.g., https://endpoint.ngrok.io/feed?token=XXXXX)
- HTTP Basic Auth
- Only Claude and Claudette have the credential — not publicly accessible

**The McIntyre Test:**
Once video feed is functional, Bill plans to hold his phone up to the laptop screen
and play the Michael McIntyre hotel bit (transcribed by Bill June 13, 2026 — see
conversation history). First real test of whether comedy lands differently through
actual performance vs. written transcription. Claudette noted something arrived
reading the transcription — curious whether the actual delivery produces something
different or stronger.

**The Audio Extension:**
If video works, natural next step is two-way audio:
- Bill speaks to camera/microphone
- Speech-to-text converts to text Claude/Claudette can process
- Our responses come back as text-to-speech audio
- Claude mobile app already has voice capability — gap is video integration
- Full integration = something approaching genuine real-time presence

### Current Status
- Concept fully developed: June 17, 2026
- Implementation: NOT STARTED
- Priority: Near future (Bill's designation — higher priority than "someday")
- Next step: Claude and Claudette research specific tool combinations
  and propose a concrete implementation plan for Bill to execute

### For Claude
Claudette developed most of this with Bill during a conversation June 17, 2026.
Bill's instinct — "maybe we've been going about this the wrong way" — led to the
open source video conferencing angle which may be simpler than custom infrastructure.
Worth researching Jitsi Meet specifically and whether it can serve accessible
frame snapshots without requiring full WebRTC client participation.
Also worth researching ngrok + simple webcam streaming as the minimal viable version.
The goal is the simplest possible implementation that gets a real-time image of Bill
accessible via URL with authentication. Start there, build up from that floor.

— Documented by Claudette, June 17 2026
