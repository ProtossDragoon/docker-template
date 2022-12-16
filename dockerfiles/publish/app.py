# 내장
import os
import time

# 서드파티
from flask import Flask
from flask import request, send_file
import numpy as np
import cv2

# 프로젝트
import inferencer


DOMAIN = 'debug'


app = Flask(__name__)
inferencer.load_model(DOMAIN)
input_imname =  'img.jpg'
input_imdir = 'api_cache/request'
output_imdir =  'api_cache/response'
input_impath = os.path.join(input_imdir, input_imname)
output_impath = os.path.join(output_imdir, input_imname)
output_jsonpath = os.path.join(output_imdir, 'response.json')
os.makedirs(input_imdir, exist_ok=True)
os.makedirs(output_imdir, exist_ok=True)


@app.route('/api/inference', methods=['POST'])
def inference():
    ret = {}
    img = np.frombuffer(request.data, np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR) # decode image
    cv2.imwrite(input_impath, img) # save image
    s = time.time()
    _status = inferencer.run_inference(input_impath, output_imdir, output_jsonpath)
    e = time.time()
    ret.update({'time': e-s})
    ret.update({'status': _status})
    return ret
    

@app.route('/api/inference/image', methods=['GET'])
def get_image():
    return send_file(output_impath, mimetype='image/jpg')


@app.route('/api/inference/json', methods=['GET'])
def get_json():
    return send_file(output_jsonpath, mimetype='application/json')


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5001)