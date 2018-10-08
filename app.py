from flask import Flask, render_template, request, send_file, send_from_directory, after_this_request, redirect, url_for, make_response
import flask
from werkzeug import secure_filename
import numpy as np
from PIL import Image
import cv2
from flask import make_response
import requests
import json
from io import BytesIO
import io
import os
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove
import StringIO


app = Flask(__name__, template_folder="templates", static_folder="static")

file_name = ' '
image_name = ' '


def image_preprocess(img_array):
    img_height, img_width, _ = np.shape(img_array)
    image_resize = cv2.resize(img_array,(1024, int(1024*img_height/img_width)))
    img_height, img_width, _ = np.shape(image_resize)
    return image_resize, img_height, img_width


def draw_label(image, point, label, font=cv2.FONT_HERSHEY_SIMPLEX,
               font_scale=1, thickness=2):
    size = cv2.getTextSize(label, font, font_scale, thickness)[0]
    x, y = point
    cv2.rectangle(image, (x, y - size[1]), (x + size[0], y),
                  (255, 0, 0))
    cv2.putText(image, label, point, font, font_scale,
                (255, 255, 255), thickness)
    
def serve_pil_image(pil_img):
    img_io = StringIO.StringIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
        #Getting input image
        file_request = request.files['file']
        file_name = file_request.filename
        file_request.save(secure_filename(file_name))
       
        
        #image pre-processing
        img_input = np.asarray(Image.open(file_name))
        image_processed, img_processed_height, img_processed_width = image_preprocess(img_input)
        #
        my_files = {'image': open(file_name, 'rb'),
                        'Content-Type': 'multipart/form-data',
                        'accept': 'application/json'}

        r = requests.post('http://localhost:5000/model/predict',files=my_files, json={"key": "value"})
        
        json_str = json.dumps(r.json())
        data = json.loads(json_str)
        
        result = data['predictions']
        
        if len(data['predictions']) <= 0:
            return "No Face detected !! Upload new image"
        else:
            for i in range(len(result)):
                pred_age = result[i]['age_estimation']
                bbx = result[i]['face_box']
                x1, y1, w, h = bbx
                label = "{}".format(pred_age)
                draw_label(image_processed, (int(x1), int(y1)), label)
                
                x2 = x1 + w
                y2 = y1 + h
                cv2.rectangle(image_processed, (int(x1), int(y1)),
                                  (int(x2), int(y2)), (0, 255, 255), 2)
                
                image_processed = cv2.cvtColor(image_processed, cv2.COLOR_BGR2RGB)
                
                
                image_name = 'static/' + file_name
                cv2.imwrite(image_name, image_processed)
                
            
            with open(image_name, 'rb') as image_file:
                def wsgi_app(environ, start_response):
                        start_response('200 OK', [('Content-type', 'image/jpeg')])
                        return image_file.read()
                os.remove(image_name)
                os.remove(file_name)
                return make_response(wsgi_app)
                
             
if __name__ == '__main__':
    app.run(debug=True)


