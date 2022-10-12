from urllib import response
import requests,  json

requestUrl = "http://127.0.0.1:7777/data"

# GET 방식으로 요청, URL Encoded  방식으로 파라미터를 전달.
# http://127.0.0.1:7777/data?msg=hello
data = { "msg" : "Hello, IoT"}
response = requests.get(requestUrl, params=data)
print(response.status_code)
if response.status_code == 200:
    print(response.text)
    
# GET 방식으로 요청    
response = requests.get(requestUrl)
print(response.status_code)
if response.status_code == 200:
    print(response.text)
    
# GET 방식으로 요청 http://127.0.0.1:7777/data/apple
response = requests.get(requestUrl+'/apple')
print(response.status_code)
if response.status_code == 200:
    print(response.text)
    
# POST 방식 - JSON
response = requests.post(requestUrl, json={"param": "apple"})
print(response.status_code)
if response.status_code == 200:
    print(response.text)
    
# POST 방식 - Data
response = requests.post(requestUrl, data="Hello, IoT")
print(response.status_code)
if response.status_code == 200:
    print(response.text)