import requests

resp = requests.get('https://localhost:8000/', params={})
print(resp.json()[0])

resp = requests.get('https://localhost:8000/health', params={})
print(resp.json()[0])

resp = requests.get('https://localhost:8000/students', params={})
print(resp.json()[0])