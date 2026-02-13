from flask import Flask, render_template, request
import subprocess
import zipfile
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

SENDER_EMAIL = "your@gmail.com"
APP_PASSWORD = "your_app_password_here"  # Replace with your actual app password not your regular email password

def send_email(receiver_email, zip_file):
    msg = EmailMessage()
    msg["Subject"] = "Your Mashup is Ready 🎵"
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg.set_content("Your mashup is attached.")

    with open(zip_file, "rb") as f:
        file_data = f.read()
        file_name = zip_file

    msg.add_attachment(file_data,
                       maintype="application",
                       subtype="zip",
                       filename=file_name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        singer = request.form["singer"]
        n = request.form["videos"]
        y = request.form["duration"]
        email = request.form["email"]

        output = "mashup.mp3"

        subprocess.run([
            "python",
            "102303717.py",
            singer,
            n,
            y,
            output
        ])

        zipname = "result.zip"
        with zipfile.ZipFile(zipname, 'w') as zipf:
            zipf.write(output)

        send_email(email, zipname)

        return "<h3>Email sent successfully! Check your inbox.</h3>"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
