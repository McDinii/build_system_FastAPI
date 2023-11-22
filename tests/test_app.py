from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_toposort_success():
    """
    Validate if a correct topo sort order is received for a given build.
    """
    # Replace 'forward_interest' with a build in your builds.yaml
    response = client.post("/get_tasks", json={"build": "forward_interest"})
    assert response.status_code == 200
    task_order = response.json()
    assert isinstance(task_order, list)
    assert len(task_order) > 0


def test_unknown_build():
    """
    Test handling of unknown build.
    """
    response = client.post("/get_tasks", json={"build": "unknown_build"})
    assert response.status_code == 400
    assert "Build or task not found in yaml files" in response.text


def test_get_tasks_empty_build():
    """
    Test handling of empty build.
    """
    response = client.post("/get_tasks", json={"build": "empty_build"})
    assert response.status_code == 200
    task_order = response.json()
    assert isinstance(task_order, list)
    assert len(task_order) == 0


def test_invalid_request():
    """
    Test handling of invalid request
    """
    response = client.post("/get_tasks", json={"unknown_field": "unknown_build"})
    assert response.status_code == 400
