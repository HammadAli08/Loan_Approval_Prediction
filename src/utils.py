# This will have the common utility functions which can be used in different modules of the project

import sys
import os
import pandas as pd
from src.Exception import CustomException
import numpy as np
import dill

def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)