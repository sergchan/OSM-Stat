from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_base_api():
    resp = client.get('/')
    print(resp.json())

    resp = client.get('/health')
    print(resp.json())

    resp = client.get('/students')
    print(resp.json())