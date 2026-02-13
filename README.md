# YouTube-Audio-Mashup
Python-based YouTube mashup generator that downloads videos, extracts audio clips, merges them into a single MP3, and delivers the result via a Flask web app with email integration.

## System Architecture

[ User Input ]
│
▼
[ Flask Web Application ]
│
▼
[ Python CLI Script (102303717.py) ]
│
▼
[ yt-dlp ]
(Video Download)
│
▼
[ FFmpeg ]
(Audio Extraction + Trimming + Merging)
│
▼
[ ZIP Creation ]
│
▼
[ Email Delivery (SMTP) ]
│
▼
[ User Receives Mashup.zip ]
