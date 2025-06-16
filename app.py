from flask import Flask, render_template, request
import yt_dlp
import os

app = Flask(__name__)
DOWNLOAD_FOLDER = "downloads"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            ydl_opts = {'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s')}
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                return render_template("index.html", message="✅ Download complete.")
            except Exception as e:
                return render_template("index.html", message=f"❌ Error: {e}")
        else:
            return render_template("index.html", message="❌ Please enter a URL.")
    return render_template("index.html", message="")

if __name__ == "__main__":
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
