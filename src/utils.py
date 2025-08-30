# This will have the common utility functions which can be used in different modules of the project

import sys
import os
import pandas as pd
from src.Exception import CustomException
import numpy as np
import dill
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
import pickle

def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)

# Model Evaluation function
def evaluate_models(X_train, y_train, X_test, y_test, models):
    report = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        score = accuracy_score(y_test, y_pred)
        report[name] = score
    return report

# To get the best model score from the dictionary
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)