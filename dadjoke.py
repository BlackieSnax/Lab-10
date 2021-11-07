import requests

url = "https://icanhazdadjoke.com/"

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print("Heres a good one for you")
print(response.text)
