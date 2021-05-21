import requests
import json
ENDPOINT = "http://127.0.0.1:8000/api/status/"
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/token/"
data = {
    "username" : 'admin',
    "password" : 'admin'
}

r = requests.post(AUTH_ENDPOINT, data=data)
token = r.json()["access"]
print(token)

post_data = json.dumps({"content": "random"})
post_headers = {
    'content-type' : 'application/json',
    "Authorization": "Bearer "+ token,
}

# post_response = requests.post(ENDPOINT, data=post_data, headers = post_headers)
# print(post_response.text)

GET_ENDPOINT = "http://127.0.0.1:8000/api/status/?page=1"
get_response = requests.get(GET_ENDPOINT)
# print(dir(get_response))
print(get_response.text)


# get and post data

# get_endpoint = ENDPOINT + str(5)
# post_data = json.dumps({"content": "anything"})
#
# r = requests.get(get_endpoint)
# print(r.text)
#
# r2 = requests.get(ENDPOINT)
# print(r2.status_code)
#
# post_headers = {
#     'content_type' : 'application/json'
# }
#
# post_response = requests.post(ENDPOINT, data=post_data, headers = post_headers)
# print(post_response.text)
