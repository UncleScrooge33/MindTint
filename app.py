from flask import Flask, send_file
from flask_cors import CORS
import os
import threading
import time
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)

CSV_FILE = "color_history.csv"
INTERVAL = 10

def generate_colors():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w") as f:
            f.write("Timestamp,R,G,B\n")

    while True:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        timestamp = datetime.utcnow().isoformat()
        with open(CSV_FILE, "a") as f:
            f.write(f"{timestamp},{r},{g},{b}\n")
        print(f"[{timestamp}] RGB: ({r}, {g}, {b})")
        time.sleep(INTERVAL)

@app.route('/colors')
def get_colors():
    if not os.path.exists(CSV_FILE):
        return "CSV not found", 404
    return send_file(CSV_FILE, mimetype="text/csv")

if __name__ == "__main__":
    threading.Thread(target=generate_colors, daemon=True).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
