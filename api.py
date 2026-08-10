import requests
url = "https://api.example.com/data"
response = requests.get(url)
print(response.json())


{
    "name": "Enes",
    "age": 19
}
data = response.json()

print(data["name"])
print(data["age"])