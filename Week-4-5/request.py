# -*- coding: utf-8 -*-
"""
Created on Sat May 14 15:06:59 2022

@author: iTs
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())
