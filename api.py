from flask import Flask, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/colors')
def get_colors():
    return send_file("color_history.csv", mimetype="text/csv")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
