from tests.conftest import client

def test_valid_workflow(test_db):
    data = {
        "name": "MyWorkflow",
        "components": [
            {"type": "import"},
            {"type": "shadow"},
            {"type": "export"}
        ]
    }
    response = client.post("/api/v1/workflow/", json=data)
    assert response.status_code == 200
    assert response.json()["message"] == "Workflow created successfully"


def test_invalid_workflow_duplicate_components(test_db):
    data = {
        "name": "MyWorkflow",
        "components": [
            {"type": "import", "settings": {"format": "PNG", "downscale": True}},
            {"type": "shadow", "settings": {"intensity": 0.1}},
            {"type": "import"}  # Duplicate import component
        ]
    }
    response = client.post("/api/v1/workflow/", json=data)
    assert response.status_code == 422  # Unprocessable Entity
    assert "Value error, Duplicate component type!" in response.json()["detail"][0]["msg"]


def test_invalid_workflow_missing_settings_for_components(test_db):
    data = {
        "name": "MyWorkflow",
        "components": [
            {"type": "shadow", "settings": {"intensity": 0.1}},
            {"type": "export"}
        ]
    }
    response = client.post("/api/v1/workflow/", json=data)
    assert response.status_code == 422  # Unprocessable Entity
    assert "Value error, Either all components should contain settings or none shall contain it!" in response.json()["detail"][0]["msg"]
