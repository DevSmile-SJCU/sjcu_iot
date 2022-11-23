import os
from flask import Flask, request
from werkzeug.utils import secure_filename
import pytesseract
from PIL import Image

# static 기능 추가
app = Flask(__name__)

upload_path = './data'
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = secure_filename(file.filename)
    os.makedirs(upload_path, exist_ok=True)
    file.save(os.path.join(upload_path, filename))
    
    imageFile = os.path.join(upload_path, filename)
    
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'

    myConfig = ('-l kor --oem 3 --psm 4')
    str = pytesseract.image_to_string(Image.open(imageFile), config=myConfig)
    print(str)
    
    return 'Upload Success'

if __name__ == '__main__':
    app.run(
    host="0.0.0.0",
    port=7000,
    debug=True)