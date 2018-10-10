from flask import Flask, render_template, request
import requests
import cv2
import numpy as np
import os
import glob
from random import randint

app = Flask(__name__)


def image_preprocess(img_array):
    img_height, img_width, _ = np.shape(img_array)
    image_resize = cv2.resize(img_array,
                              (1024, int(1024 * img_height / img_width)))
    img_height, img_width, _ = np.shape(image_resize)
    return image_resize, img_height, img_width


def draw_label(image, point, image_box, label, font=cv2.FONT_HERSHEY_SIMPLEX,
               font_scale=1, thickness=2):
    size = cv2.getTextSize(label, font, font_scale, thickness)[0]
    x1, y1 = point
    x2, y2 = image_box
    cv2.rectangle(image, (x1, y1 - size[1]), (x1 + size[0], y1), (255, 0, 0))
    cv2.putText(image, label, point, font, font_scale,
                (255, 255, 255), thickness)
    cv2.rectangle(image, (int(x1), int(y1)),
                  (int(x2), int(y2)), (0, 255, 255), 2)


@app.route('/', methods=['POST', 'GET'])
def root():

    # removing all previous files in folder before start processing
    output_folder = 'static/img/temp'
    for file in glob.glob(output_folder + '/*'):
        os.remove(file)

    # on post handle upload
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
        complete code - 1
        """
        result_age =

        """
        complete code - 2
        """
        # extracting prediction
        output_data =
        result =

        total_age = 0

        if len(result) <= 0:
            return "No Face detected !! Upload new image"
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
                    output_name = output_folder + '/' + file_name
                    cv2.imwrite(output_name, image_processed)

        average_age = total_age / len(result)
        ppl_count = len(result)

        """
        complete code - 3
        """
        return
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=8000)
