import requests

url = "https://www.example.com"
response = requests.get(url)

print (response)
print(response.status_code)