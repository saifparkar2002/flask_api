import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes":69, "name":"saif", "views":420},
        {"likes":1000, "name":"REST API", "views":10000},
        {"likes":15000, "name":"Python", "views":100000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/2")
print(response.json())