import requests

from app.logger import log


def test_root():
    """
    This fails and stops container. Fix it
    """
    response = requests.get("http://api")
    assert response.status_code == 200


def test_run_task():
    payload = {"name": "app.tasks.util.talk_to_me"}
    response = requests.post("http://api/tasks/task", json=payload)
    body = response.json()
    assert body["id"]
    assert body["name"] == "app.tasks.util.talk_to_me"
    assert body["status"] == "sent"
    assert response.status_code == 201


def test_run_task_bad_request():
    response = requests.post("http://api/tasks/task", data={})
    assert response.status_code == 422
