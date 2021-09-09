import requests
def runtest():
    BASE = "http://127.0.0.1:8000/"
    response = requests.patch(BASE + "video/4?id=4&name=5&views=6&likes=7")
    return response.json()
print(runtest())