import requests
import jsonpath

Resp = requests.delete("https://reqres.in/api/users/2")
if Resp.status_code == 204:
    assert True
else:
    assert False

