"""
Python CI Demo - Flask Web Application
Author: xuyuan9817
Version: 2.0.0
"""
from flask import Flask, jsonify, request
from datetime import datetime
import platform
import sys

app = Flask(__name__)

# Simulated task database
TASKS = [
    {"id": 1, "title": "Learn CI/CD", "done": True},
    {"id": 2, "title": "Configure SonarCloud", "done": True},
    {"id": 3, "title": "Deploy SonarQube", "done": False},
    {"id": 4, "title": "Set up code review", "done": False},
]


@app.route("/")
def index():
    """Home page"""
    return jsonify(
        message="Hello from Python CI Demo!",
        version="2.0.0",
        timestamp=datetime.utcnow().isoformat(),
    )


@app.route("/health")
def health():
    """Health check endpoint"""
    return jsonify(status="healthy", uptime="ok")


@app.route("/version")
def version():
    """Version information"""
    return jsonify(
        version="2.0.0",
        author="xuyuan9817",
        python=sys.version,
        platform=platform.system(),
    )


@app.route("/tasks", methods=["GET"])
def get_tasks():
    """Get task list with optional filtering"""
    status_filter = request.args.get("status")
    if status_filter == "done":
        result = [t for t in TASKS if t["done"]]
    elif status_filter == "pending":
        result = [t for t in TASKS if not t["done"]]
    else:
        result = TASKS
    return jsonify(tasks=result, total=len(result))


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """Get a single task by ID"""
    task = next((t for t in TASKS if t["id"] == task_id), None)
    if task is None:
        return jsonify(error="Task not found"), 404
    return jsonify(task)


@app.route("/status")
def status():
    """System status overview"""
    return jsonify(
        status="running",
        tasks_total=len(TASKS),
        tasks_done=sum(1 for t in TASKS if t["done"]),
        tasks_pending=sum(1 for t in TASKS if not t["done"]),
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
