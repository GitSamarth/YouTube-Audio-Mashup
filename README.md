# YouTube-Audio-Mashup
Python-based YouTube mashup generator that downloads videos, extracts audio clips, merges them into a single MP3, and delivers the result via a Flask web app with email integration.

## System Architecture

+--------------------+
| User Input |
+--------------------+
|
v
+--------------------+
| Flask Web App |
+--------------------+
|
v
+------------------------------+
| Python CLI Script (102303717.py) |
+------------------------------+
|
v
+--------------------+
| yt-dlp |
| (Video Download) |
+--------------------+
|
v
+-----------------------------+
| FFmpeg |
| Audio Extract • Trim • Merge |
+-----------------------------+
|
v
+--------------------+
| ZIP Creation |
+--------------------+
|
v
+--------------------+
| Email via SMTP |
+--------------------+
|
v
+--------------------+
| User Receives ZIP |
+--------------------+
