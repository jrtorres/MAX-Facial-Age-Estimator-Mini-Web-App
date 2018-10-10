#
# Copyright 2018 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from flask import Flask, render_template, request
import requests
import cv2
import numpy as np
import os
import glob
from random import randint

app = Flask(__name__)


def image_preprocess(img_array):
    """Resize the image for processing"""
    img_height, img_width, _ = np.shape(img_array)
    image_resize = cv2.resize(img_array,
                              (1024, int(1024 * img_height / img_width)))
    img_height, img_width, _ = np.shape(image_resize)
    return image_resize, img_height, img_width


def draw_label(image, point, image_box, label, font=cv2.FONT_HERSHEY_SIMPLEX,
               font_scale=1, thickness=2):
    """Draws the labels and bounding boxes on the image"""
    size = cv2.getTextSize(label, font, font_scale, thickness)[0]
    x1, y1 = point
    x2, y2 = image_box
    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
    cv2.putText(image, label, point, font, font_scale,
                (255, 255, 255), thickness)
    cv2.putText(image, label, point, font, font_scale, (0, 0, 0), thickness-1)


@app.route('/', methods=['POST', 'GET'])
def root():

    # removing all previous files in folder before start processing
    output_folder = 'static/img/temp/'
    for file in glob.glob(output_folder + '*'):
        os.remove(file)

    # on POST handle upload
    if request.method == 'POST':

        # get file details
        file_data = request.files['file']
        # file_name = file_data.filename
        # read images from string data
        file_request = file_data.read()
        # convert string data to numpy array
        np_inp_image = np.fromstring(file_request, np.uint8)
        # convert numpy array to image
        img = cv2.imdecode(np_inp_image, cv2.IMREAD_UNCHANGED)
        (image_processed,
         img_processed_height,
         img_processed_width) = image_preprocess(img)
        # encode image
        _, image_encoded = cv2.imencode('.jpg', img)
        # send this as an input for prediction
        my_files = {
            'image': image_encoded.tostring(),
            'Content-Type': 'multipart/form-data',
            'accept': 'application/json'
        }
        """
        COMPLETE CODE - Send image to the model API for prediction
        """
        result_age =

        """
        COMPLETE CODE - Extract prediction
        """
        # extracting prediction
        output_data =
        result =

        total_age = 0

        if len(result) <= 0:
            msg = "No faces detected, try uploading a new image"
            return render_template("index.html", error_msg=msg)
        else:
            for i in range(len(result)):
                pred_age = str(result[i]['age_estimation'])
                total_age += int(pred_age)
                bbx = result[i]['face_box']
                x1, y1, w, h = bbx
                x2 = x1 + w
                y2 = y1 + h
                # pre-process image
                draw_label(image_processed, (int(x1), int(y1)),
                           (int(x2), int(y2)), pred_age)
                # output
                if i == (len(result) - 1):
                    file_name = (str(randint(0, 999999)) + '.jpg')
                    output_name = output_folder + file_name
                    cv2.imwrite(output_name, image_processed)

        average_age = int(total_age / len(result))
        ppl_count = len(result)

        """
        COMPLETE CODE - Update Web UI with result
        """
        return
    else:
        # on GET return index.html
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=8000)
