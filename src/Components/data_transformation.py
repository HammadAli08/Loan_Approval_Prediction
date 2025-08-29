# This will contain the code related to transformation of data. eg. scaling, encoding etc.


import os
import sys

from src.Exception import CustomException
from src.Logger import logging
from src.utils import save_object 

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer # This is to handle missing values
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer # This is to create a pipeline for numerical and categorical columns
from dataclasses import dataclass
import pickle


class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        '''
        try:
            numerical_columns = ['loan_id', ' no_of_dependents', ' income_annum', ' loan_amount',
            ' loan_term', ' cibil_score', ' residential_assets_value',
            ' commercial_assets_value', ' luxury_assets_value',
            ' bank_asset_value']
            categorical_columns = [' education', ' self_employed']
            # Numerical Pipeline
            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ]) 
            # Categorical Pipeline
            cat_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('one_hot_encoder', OneHotEncoder()),
                ('scaler', StandardScaler(with_mean=False))
            ])
            logging.info(f'Numerical columns: {numerical_columns}')
            logging.info(f'Categorical columns: {categorical_columns}')
            
            preprocessor=ColumnTransformer(
                [
                    ('num_pipeline', num_pipeline, numerical_columns),
                    ('cat_pipelines', cat_pipeline, categorical_columns)
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info('Read train and test data completed')
            logging.info('Obtaining preprocessor object')
                         
            preprocessor_obj = self.get_data_transformer_object()
            target_column_name = ' loan_status'
            numerical_columns = ['loan_id', ' no_of_dependents', ' income_annum', ' loan_amount',
                                 ' loan_term', ' cibil_score', ' residential_assets_value',
                                 ' commercial_assets_value', ' luxury_assets_value',
                                 ' bank_asset_value']
            
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]
            
            logging.info(f'Input features: {input_feature_train_df.shape}')
            logging.info(f'Target features: {target_feature_train_df.shape}')
            
            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(test_df.drop(columns=[target_column_name], axis=1))
            
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(test_df[target_column_name])]
            
            logging.info(f'Train array: {train_arr.shape}')
            logging.info(f'Test array: {test_arr.shape}')
            
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e, sys)