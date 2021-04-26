import requests
import jsonpath

payload ={
    "name": "morpheustest",
}
resp = requests.patch("https://reqres.in/api/users/2", data=payload)
if resp.status_code == 200:
    assert True
    print(resp.json())
else:
    assert False
