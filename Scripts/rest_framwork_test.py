import requests
import json


# #----------------------Authentication-----------------------------
# ENDPOINT = "http://127.0.0.1:8000/api/status/"
# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/token/"
# data = {
#     "username" : 'admin',
#     "password" : 'admin'
# }
#
# r = requests.post(AUTH_ENDPOINT, data=data)
# token = r.json()["access"]
# print(token)
#
# post_data = json.dumps({"content": "random"})
# post_headers = {
#     'content-type' : 'application/json',
#     "Authorization": "Bearer "+ token,
# }
#
# # post_response = requests.post(ENDPOINT, data=post_data, headers = post_headers)
# # print(post_response.text)
#
# GET_ENDPOINT = "http://127.0.0.1:8000/api/status/?page=1"
# get_response = requests.get(GET_ENDPOINT)
# # print(dir(get_response))
# print(get_response.text)
#
# #------
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
#---------------------------------------------------------------------


#------------------MIDDLEWARE ---------------------------

from Induction.settings import key


# ENDPOINT = "http://127.0.0.1:8000/new/"
# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/token/"
# data = {
#     "username" : 'admin',
#     "password" : 'admin'
# }
#
# r = requests.post(AUTH_ENDPOINT, data=data)
# token = r.json()["access"]
# # print(token)
#
# # Encrypting the data
# from cryptography.fernet import Fernet
# from Induction.settings import  key
# post_data = "Hello"
# encoded =  post_data.encode()
# print("post data:", post_data)
#
# f = Fernet(key)
# post_data = f.encrypt(encoded)
# print("Encrypting post data:", post_data.decode('UTF-8'))
# print()
# # post_data =["gAAAAABgrgrPkaKxIZebn9k0s7CZC2dmne3JIG6EhkFjH5r0NyNQ1CavQMf38AWjFPtGDgMnFUdl-_a51BCMmStRhU1kPbZYcw=="]
# ###
#
# post_headers = {
#     'content-type' : 'text/html',
#     "Authorization": "Bearer "+ token,
# }
#
#
# post_response = requests.post(ENDPOINT, data=post_data, headers = post_headers)
# print("Response Decrypted :",post_response.text)
#
# print("After decrypting response", f.decrypt(post_response.text.encode()).decode('UTF-8'))

#--------------------------------------------------------------------------


# AUTH_ENDPOINT = "http://127.0.0.1:8000/customauth/auth/"
#
# post_headers = {
#     'content-type' : 'application/json'
# }
#
# data = {
#     "username" : "admin",
#     "password" : "admin"
# }
#
# r = requests.post(AUTH_ENDPOINT, data=data,  headers = post_headers)
# print(r)
# token = r.json()["access_token"]

