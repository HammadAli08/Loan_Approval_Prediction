# This will contain the code related to transformation of data. eg. scaling, encoding etc.

import os
import sys

from src.Exception import CustomException
from src.Logger import logging
from src.utils import save_object

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass
from scipy import sparse


class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        """
        Build the preprocessing pipeline.
        Column names are assumed to be stripped of spaces already.
        """
        try:
            numerical_columns = [
                'loan_id', 'no_of_dependents', 'income_annum', 'loan_amount',
                'loan_term', 'cibil_score', 'residential_assets_value',
                'commercial_assets_value', 'luxury_assets_value', 'bank_asset_value'
            ]

            categorical_columns = ['education', 'self_employed']

            # Numerical Pipeline
            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])

            # Categorical Pipeline
            cat_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('one_hot_encoder', OneHotEncoder(handle_unknown='ignore')),
                ('scaler', StandardScaler(with_mean=False))
            ])

            logging.info(f'Numerical columns: {numerical_columns}')
            logging.info(f'Categorical columns: {categorical_columns}')

            preprocessor = ColumnTransformer(
                transformers=[
                    ('num_pipeline', num_pipeline, numerical_columns),
                    ('cat_pipelines', cat_pipeline, categorical_columns)
                ],
                remainder='drop'
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            # ✅ Normalize column names (strip spaces, lowercase them if needed)
            train_df.columns = train_df.columns.str.strip()
            test_df.columns = test_df.columns.str.strip()

            logging.info("Read train and test data completed")
            logging.info(f"Train columns: {list(train_df.columns)}")

            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "loan_status"

            # Split input features and target
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_series = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_series = test_df[target_column_name]

            # Clean and encode target
            target_feature_train_series = target_feature_train_series.astype(str).str.strip()
            target_feature_test_series = target_feature_test_series.astype(str).str.strip()

            le = LabelEncoder()
            y_train = le.fit_transform(target_feature_train_series)
            y_test = le.transform(target_feature_test_series)

            logging.info("Applying preprocessing object on training and testing features.")
            X_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            X_test_arr = preprocessing_obj.transform(input_feature_test_df)

            if sparse.issparse(X_train_arr):
                X_train_arr = X_train_arr.toarray()
            if sparse.issparse(X_test_arr):
                X_test_arr = X_test_arr.toarray()

            train_arr = np.c_[X_train_arr, y_train]
            test_arr = np.c_[X_test_arr, y_test]

            logging.info("Saved preprocessing object.")
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e, sys)
