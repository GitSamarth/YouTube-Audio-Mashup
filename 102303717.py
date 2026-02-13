import sys, os, subprocess

if len(sys.argv) != 5:
    print("Usage: python file.py <Singer> <N> <Y> <Output>")
    exit()

singer = sys.argv[1]
N = int(sys.argv[2])
Y = int(sys.argv[3])
output = sys.argv[4]

if N <= 10 or Y <= 20:
    print("N must >10 and Y >20")
    exit()

os.makedirs("videos", exist_ok=True)
os.makedirs("audio", exist_ok=True)
os.makedirs("trimmed", exist_ok=True)

print("Downloading videos...")

subprocess.run([
    "yt-dlp",
    "--ignore-errors",
    "-f", "mp4",
    f"ytsearch{N}:{singer}",
    "-o", "videos/%(id)s.%(ext)s"
])

print("Extracting audio...")

for v in os.listdir("videos"):
    ip = os.path.join("videos", v)
    op = os.path.join("audio", v.split(".")[0] + ".mp3")

    subprocess.run([
        "ffmpeg","-y",
        "-i", ip,
        op
    ])

print("Trimming...")

for a in os.listdir("audio"):
    ip = os.path.join("audio", a)
    op = os.path.join("trimmed", a)

    subprocess.run([
        "ffmpeg","-y",
        "-i", ip,
        "-t", str(Y),
        op
    ])

print("Merging...")

with open("list.txt","w") as f:
    for t in os.listdir("trimmed"):
        f.write(f"file '{os.path.abspath(os.path.join('trimmed',t))}'\n")

subprocess.run([
    "ffmpeg","-y",
    "-f","concat",
    "-safe","0",
    "-i","list.txt",
    "-c","copy",
    output
])

print("DONE ✅", output)
