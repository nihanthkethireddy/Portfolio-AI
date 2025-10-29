# api/index.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello from Python on Vercel!")

# This is important for Vercel to recognize the Flask app
# For local development, you might run `uvicorn api.index:app --reload`
# In Vercel, this is handled automatically.