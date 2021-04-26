import json
import requests
import jsonpath

payload = {
    "name": "Anupam",
    "job": "leader"
}

Resp = requests.post("https://reqres.in/api/users", data=json.loads(open("Mydata.json", "r").read()))

if Resp.status_code == 201:
    assert True
    print(Resp.json())
else:
    assert False

if Resp.json()['job'] == 'leadership':
    assert True
    print(Resp.headers.get("Content Type"))
    
else:
    assert False