import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/3?id=5&name=anand&likes=1526&views=10")
print(response.json())
