#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   image_classic.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/28 上午 10:06   hello      1.0         None

'''

import os
import sys
# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
# Some utilites
import numpy as np
from util import base64_to_pil

# Declare a flask app
app = Flask(__name__)
# You can use pretrained model from Keras
# Check https://keras.io/applications/
# or https://www.tensorflow.org/api_docs/python/tf/keras/applications
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2

model = MobileNetV2(weights='imagenet')
print('Model loaded. Check http://127.0.0.1:5000/')
# Model saved with Keras model.save()
MODEL_PATH = 'models/your_model.h5'


# Load your own trained model
# model = load_model(MODEL_PATH)
# model._make_predict_function()          # Necessary
# print('Model loaded. Start serving...')
def model_predict(img, model):
    img = img.resize((224, 224))
    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)
    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    x = preprocess_input(x, mode='tf')
    preds = model.predict(x)
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('home.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the image from post request
        img = base64_to_pil(request.json)
        # Save the image to ./uploads
        # img.save("./uploads/image.png")
        # Make prediction
        preds = model_predict(img, model)
        # Process your result for human
        pred_proba = "{:.3f}".format(np.amax(preds))  # Max probability
        pred_class = decode_predictions(preds, top=1)  # ImageNet Decode
        result = str(pred_class[0][0][1])  # Convert to string
        result = result.replace('_', ' ').capitalize()
        # Serialize the result, you can add additional fields
        return jsonify(result=result, probability=pred_proba)
    return None


if __name__ == '__main__':
    # app.run(port=5002, threaded=False)
    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
