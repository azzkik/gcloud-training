import requests

resp = requests.post("http://localhost:5000/", files={'file': open('data/eight.png', 'rb')})

print(resp.json())
