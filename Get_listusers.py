import requests
import jsonpath
p = {"page": 2}
resp = requests.get("https://reqres.in/api/users?", params=p)
json_response = resp.json()
respcode =resp.status_code
if respcode == 200:
    assert True
    print(json_response)
else:
    assert False

if json_response['page'] == 2:
    assert True
    print(json_response)
else:
    assert False

print(json_response['data'][0]['email'])
if json_response['data'][1]['id'] == 8:
    assert True
else:
    assert False

if json_response['data'][2]['first_name'] == "Tobias":
    assert True
    print(resp.url)
else:
    assert False

if json_response["support"]["url"] == "https://reqres.in/#support-heading":
    assert True
    print(resp.url)
else:
    assert False
