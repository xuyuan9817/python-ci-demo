@
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(message="Hello from Python CI Demo!", status="ok")

@app.route("/health")
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


@app.route("/version")
def version():
    return jsonify(version="1.0.0", author="xuyuan9817", ci="GitHub Actions")

@app.route("/status")
def status():
    return jsonify(
        services="all operational",
        uptime="running",
        build="automated"
    )