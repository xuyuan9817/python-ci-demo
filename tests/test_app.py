"""
Comprehensive test suite for Flask Web Application
Coverage: 10 test cases across all endpoints
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import app, TASKS


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class TestBasicEndpoints:
    """Test basic health and info endpoints"""

    def test_index_returns_welcome(self, client):
        """Test home page returns welcome message"""
        resp = client.get("/")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["version"] == "2.0.0"
        assert "timestamp" in data
        assert "Hello" in data["message"]

    def test_health_check(self, client):
        """Test health check returns healthy status"""
        resp = client.get("/health")
        assert resp.status_code == 200
        assert resp.get_json()["status"] == "healthy"

    def test_version_info(self, client):
        """Test version endpoint returns correct info"""
        resp = client.get("/version")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["version"] == "2.0.0"
        assert data["author"] == "xuyuan9817"
        assert "python" in data

    def test_system_status(self, client):
        """Test system status endpoint"""
        resp = client.get("/status")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["status"] == "running"
        assert data["tasks_total"] == len(TASKS)
        assert data["tasks_done"] + data["tasks_pending"] == data["tasks_total"]


class TestTaskEndpoints:
    """Test task management endpoints"""

    def test_get_all_tasks(self, client):
        """Test getting all tasks returns full list"""
        resp = client.get("/tasks")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["total"] == len(TASKS)

    def test_get_done_tasks(self, client):
        """Test filtering completed tasks"""
        resp = client.get("/tasks?status=done")
        assert resp.status_code == 200
        data = resp.get_json()
        for task in data["tasks"]:
            assert task["done"] is True

    def test_get_pending_tasks(self, client):
        """Test filtering pending tasks"""
        resp = client.get("/tasks?status=pending")
        assert resp.status_code == 200
        data = resp.get_json()
        for task in data["tasks"]:
            assert task["done"] is False

    def test_get_task_by_id(self, client):
        """Test getting a specific task"""
        resp = client.get("/tasks/1")
        assert resp.status_code == 200
        assert resp.get_json()["id"] == 1

    def test_task_not_found(self, client):
        """Test 404 for non-existent task"""
        resp = client.get("/tasks/999")
        assert resp.status_code == 404
        assert "error" in resp.get_json()
