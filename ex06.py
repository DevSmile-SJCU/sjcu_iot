from PIL import Image
import pytesseract

# pip install speechrecognition
# pip install gTTs  
# pip install playsound==1.2.2
import speech_recognition as sr
from gtts import gTTS
import playsound

filename = '.\data\sound.mp3'
def speak(text):
     tts = gTTS(text=text, lang='ko')
     tts.save(filename)
     playsound.playsound(filename)

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'

myConfig = ('-l kor --oem 3 --psm 4')
str = pytesseract.image_to_string(Image.open('.\data\sjcu.png'), config=myConfig)

print(str)
speak(str)