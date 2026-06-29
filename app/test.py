from fastapi.testclient import TestClient
import main

client = TestClient(app)

def test_base_api():
    resp = client.get('/')
    print(resp.json())

    resp = client.get('/health')
    print(resp.json()[0])

    resp = client.get('/students')
    print(resp.json()[0])