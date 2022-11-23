import os
import cv2
from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

upload_path = './data'
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = secure_filename(file.filename)
    os.makedirs(upload_path, exist_ok=True)
    file.save(os.path.join(upload_path, filename))
    
    imageFile = os.path.join(upload_path, filename)
    img  = cv2.imread(imageFile)    # cv2.IMREAD_COLOR
    cv2.imshow('Camera Image',img)
    cv2.waitKey(1500)
    cv2.destroyAllWindows()
    
    return 'Upload Success'

if __name__ == '__main__':
    app.run(
    host="0.0.0.0",
    port=7000,
    debug=True)