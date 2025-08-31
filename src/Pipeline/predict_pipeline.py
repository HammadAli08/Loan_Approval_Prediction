# This will contain the code for reading the data from the source

# This will contain the code for reading the data from the source


import sys
import os
import pandas as pd
from src.Exception import CustomException
from src.Logger import logging
from src.utils import load_object
from dataclasses import dataclass


class Predictpipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class costum_data:
    def __init__(self,
                 loan_id: int,
                 no_of_dependents: int,
                 income_annum: float,
                 loan_amount: float,
                 loan_term: float,
                 cibil_score: float,
                 residential_assets_value: float,
                 commercial_assets_value: float,
                 luxury_assets_value: float,
                 bank_asset_value: float,
                 education: str,
                 self_employed: str):

        self.loan_id = loan_id
        self.no_of_dependents = no_of_dependents
        self.income_annum = income_annum
        self.loan_amount = loan_amount
        self.loan_term = loan_term
        self.cibil_score = cibil_score
        self.residential_assets_value = residential_assets_value
        self.commercial_assets_value = commercial_assets_value
        self.luxury_assets_value = luxury_assets_value
        self.bank_asset_value = bank_asset_value
        self.education = education
        self.self_employed = self_employed

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "loan_id": [self.loan_id],
                "no_of_dependents": [self.no_of_dependents],
                "income_annum": [self.income_annum],
                "loan_amount": [self.loan_amount],
                "loan_term": [self.loan_term],
                "cibil_score": [self.cibil_score],
                "residential_assets_value": [self.residential_assets_value],
                "commercial_assets_value": [self.commercial_assets_value],
                "luxury_assets_value": [self.luxury_assets_value],
                "bank_asset_value": [self.bank_asset_value],
                "education": [self.education],
                "self_employed": [self.self_employed]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df

        except Exception as e:
            raise CustomException(e, sys)


