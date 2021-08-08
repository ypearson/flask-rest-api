import requests

BASE = "http://127.0.0.1:5000"

videos = [
    {"likes": "15", "views": 100, "name": "Some Video 1"},
    {"likes": "215", "views": 200, "name": "Some Video 2"},
    {"likes": "43", "views": 130, "name": "Some Video 3"},
    {"likes": "1245", "views": 500, "name": "Some Video 4"},
    {"likes": "500", "views": 700, "name": "Some Video 5"}]

response = requests.get(
    BASE+'/api/video/'+str(1))
print(response.status_code)
print(response.json())

input()

for i in range(0, len(videos)):
    response = requests.post(
        BASE+'/api/video/'+str(i), data=videos[i])
    print(response.status_code)
    print(response.json())

    input()

    response = requests.delete(
        BASE+'/api/video/'+str(i))
    print("delete")
    print(response.status_code)
    print(response.json())


response = requests.patch(
    BASE+'/api/video/'+str(0), data={"views": 100, "name": "Some Video 1 PATCHED"})
print(response.status_code)
print(response.json())