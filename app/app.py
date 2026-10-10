from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(service="pi-platform-app", status="ok")

@app.get("/health")
def health():
    return jsonify(status="ok")
    
