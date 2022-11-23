#pip install picamera
#pip install requests

from time import sleep
from picamera import PiCamera, Color
import requests
 
camera = PiCamera()
camera.start_preview()
sleep(2)
camera.capture('capImage.jpg')
camera.stop_preview()
 
# 파일 업로드
requestUrl = "http://192.168.137.1:7000/upload"
files = {'file': open('capImage.jpg', 'rb')}
response = requests.post(requestUrl, files=files)
print(response.status_code)
if response.status_code == 200:
    print(response.text)
else:
    print('Error')