from flask import Flask, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/colors')
def get_colors():
    file_path = os.path.join(os.path.dirname(__file__), "color_history.csv")
    if not os.path.exists(file_path):
        return "color_history.csv not found", 404
    return send_file(file_path, mimetype="text/csv")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # ← c’est ça la clé
    app.run(host="0.0.0.0", port=port)
