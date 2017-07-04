import requests
url='http://localhost:8000'
resp=requests.get(url)
print(resp.text)
