# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:05:53 2022

@author: iTs
"""

import numpy as np
from flask import Flask
from flask import request, jsonify, render_template
import pickle

# app
app = Flask(__name__)

# load model
model = pickle.load(open('model.pkl','rb'))

@app.route('/')

def home():
    return render_template("index.html")

# routes
@app.route('/predict', methods=['POST'])

def predict():
    ...
    # For rendering results on HTML GUI
    ...
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    # predictions
    
    output = round(prediction[0], 2)
           
    # return data
    
        
    return render_template('index.html', prediction_text='Survival prediction {} '.format(output))

@app.route('/predict_api',methods=['POST'])

def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug = False)
