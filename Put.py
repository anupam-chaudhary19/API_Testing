import requests
import jsonpath
payload={
    "name": "Anu",
    "job": "zion resident"
}
resp = requests.put("https://reqres.in/api/users/2", data=payload)
if resp.status_code == 200:
    assert True
    print(resp.json())
else:
    assert False