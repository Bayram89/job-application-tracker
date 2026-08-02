from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Job Application Tracker API"
    }

def test_get_all_applications():
    client = app.test_client()

    response = client.get("/applications")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_unknown_application():
    client = app.test_client()

    response = client.get("/applications/999")

    assert response.status_code == 404
    assert response.get_json() == {
        "error": "Application not found"
    }