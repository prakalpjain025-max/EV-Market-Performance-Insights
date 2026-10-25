
from flask import Flask, send_from_directory
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent

@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/static/<path:filename>")
def styles(filename):
    return send_from_directory(BASE_DIR / "static", filename)

if __name__ == "__main__":
    app.run(debug=True)
