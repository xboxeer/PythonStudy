import requests
resp=requests.get("http://localhost:8000/echo/elendil")
print(resp.text)