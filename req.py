

import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse


data = {"name": "Salah", "message": "Hello!"}
url = "https://httpbin.org/post"

response = requests.post(url, json=data)

response_data = response.json()
# Shows the data as a dictionary
print(response_data)

# here we use an endpoint that always gives a 404 status error
response = requests.get("https://httpbin.org/status/404")
# if status code is not 200 (successful response), then show error message
if response.status_code != 200:
    print(f"HTTP Error: {response.status_code}")

url = "https://httpbin.org/delay/10"

try:
    response = requests.get(url, timeout=5)
except requests.exceptions.Timeout as err:
    print(err)

    auth_token = "XXXXXXXX"

    # here we set the authorization header with the 'bearer token' for authentication purposes.
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    url = "https://httpbin.org/headers"
    response = requests.get(url, headers=headers)
    print(response.json())

    url = "https://www.example.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.text
    content = soup.find("p").text
    links = [a["href"] for a in soup.find_all("a")]

    print(title, content, links)

    data = urllib.parse.urlencode({"key": "value"}).encode("utf-8")
    req = urllib.request.Request("https://www.example.com", data=data, method="post")
    with urllib.request.urlopen(req) as response:
        html = response.read().decode("utf-8")
    print(html)