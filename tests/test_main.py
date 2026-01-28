"""Tests for main app."""


def test_root(client):
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_check(client):
    """Test health check endpoint."""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_get_users(client):
    """Test get users endpoint."""
    response = client.get("/api/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_users_structure(client):
    """Test users response structure."""
    response = client.get("/api/users")
    assert response.status_code == 200
    users = response.json()
    
    if users:  # If there are users
        user = users[0]
        assert "id" in user
        assert "name" in user
        assert "birthdate" in user
        assert "gender" in user
