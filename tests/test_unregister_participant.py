from fastapi.testclient import TestClient

from src.app import app


def test_unregister_participant_from_activity():
    client = TestClient(app)
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {email} from {activity_name}"

    activity = client.get("/activities").json()[activity_name]
    assert email not in activity["participants"]

    # Restore the original state for subsequent tests or runs.
    client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
