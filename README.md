# YouTube-Audio-Mashup
Python-based YouTube mashup generator that downloads videos, extracts audio clips, merges them into a single MP3, and delivers the result via a Flask web app with email integration.

## System Architecture

User Input → Flask Web App → Python CLI Script → yt-dlp → FFmpeg → ZIP → Email

---
## Methodology

The system follows a modular pipeline combining command-line automation with a web-based interface.

First, user parameters (singer name, number of videos, clip duration, and email) are collected through a Flask web form or command-line arguments.

The backend invokes a Python CLI script which performs automated YouTube search and video download using **yt-dlp**.

Downloaded videos are passed to **FFmpeg**, which handles:

- Audio extraction from video files  
- Trimming of the first *Y* seconds from each clip  
- Concatenation of all processed audio segments into a single MP3 mashup  

After mashup generation, the output MP3 is compressed into a ZIP archive.

Finally, the ZIP file is transmitted to the user via SMTP email using Gmail App Password authentication.

This design separates data acquisition, processing, and delivery into independent stages, improving reliability and maintainability.

---

## Result Table

| Singer        | Videos | Duration (sec) | Output Size (MB) | Status  |
|---------------|--------|----------------|------------------|---------|
| Arijit Singh | 12     | 25             | 5.3              | Success |
| Sharry Mann  | 12     | 30             | 6.1              | Success |
---
## Result Graph

The graph below illustrates the relationship between selected singer and final mashup file size.
<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/64754c95-19b6-4916-93b5-e99e64eaaa77" />

---

## Tools and Technologies

- Python 3.13  
- yt-dlp  
- FFmpeg  
- Flask  
- smtplib  
- zipfile  
- Matplotlib  

---

## Conclusion

The implemented system successfully automates multimedia retrieval, audio processing, and email delivery within a unified workflow.  
The project demonstrates practical integration of web frameworks, command-line utilities, and multimedia processing pipelines, fulfilling all assignment objectives.

---

## Execution

### Command Line

```bash
python 102303717.py "Arijit Singh" 12 25 mashup.mp3
```
web interface 
```
python app.py
```
Open:
http://127.0.0.1:5000

## Performance Analysis

The processing time increases linearly with the number of videos selected, as each video undergoes download, audio extraction, and trimming.
The output file size is approximately proportional to:
Number of Videos × Clip Duration × Bitrate
For example:
- 12 videos × 25 seconds ≈ 300 seconds total mashup.
- At 128 kbps bitrate, final file size ≈ 5–6 MB.
This confirms expected linear scalability of the system.

## Limitations

- Processing time depends on internet speed.
- Large values of N increase download and computation time.
- Gmail SMTP requires App Password authentication.
- YouTube rate limiting may affect large batch downloads.



