import os

import psycopg
from flask import Flask, jsonify

app = Flask(__name__)


def db_password():
    with open(os.environ["DB_PASSWORD_FILE"]) as f:
        return f.read().strip()


@app.get("/")
def index():
    return jsonify(service="pi-platform-app", status="ok")


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/db-health")
def db_health():
    try:
        with psycopg.connect(
            host=os.environ["DB_HOST"],
            dbname=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=db_password(),
            connect_timeout=3,
        ) as conn:
            conn.execute("SELECT 1")
        return jsonify(db="ok")
    except psycopg.Error:
        return jsonify(db="unavailable"), 503