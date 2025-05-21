from flask import Flask, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/colors')
def get_colors():
    return send_file("color_history.csv", mimetype="text/csv")
