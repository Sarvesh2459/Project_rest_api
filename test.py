import requests
BASE = "http://localhost:5000/"
response = requests.delete(BASE + "video/11")
print(response.json())
