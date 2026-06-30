from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_base_api():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "hallow"}

    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

    response = client.get('/students/1')
    assert response.status_code == 200