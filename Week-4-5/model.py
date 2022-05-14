# -*- coding: utf-8 -*-
"""
Created on Fri May 13 15:41:29 2022

@author: iTs
"""



# data processing
import pandas as pd

# algorithms
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import  train_test_split


# serializing
import pickle

# create df
train = pd.read_csv('titanic.csv')

# drop null values
train.dropna(inplace=True)

# features and target
target = 'Survived'
features = ['Pclass', 'Age', 'SibSp', 'Fare'] 

# X matrix, y vector
X = train[features]
y = train[target]


train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.2, random_state=0)


# Random Forest
rf = RandomForestClassifier(n_estimators=100)

rf.fit(train_X, train_y)

rf_predictions = rf.predict(test_X)
rf_predictions

# Make pickle file

pickle.dump(rf, open("model.pkl", "wb"))