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
        Create preprocessing pipelines for numerical and categorical features.
        """
        try:
            numerical_columns = [
                'loan_id', 'no_of_dependents', 'income_annum', 'loan_amount',
                'loan_term', 'cibil_score', 'residential_assets_value',
                'commercial_assets_value', 'luxury_assets_value', 'bank_asset_value'
            ]

            categorical_columns = ['education', 'self_employed']

            # Numerical pipeline
            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])

            # Categorical pipeline
            cat_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('one_hot_encoder', OneHotEncoder(handle_unknown='ignore')),
                ('scaler', StandardScaler(with_mean=False))
            ])

            logging.info(f'Numerical columns: {numerical_columns}')
            logging.info(f'Categorical columns: {categorical_columns}')

            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline', num_pipeline, numerical_columns),
                    ('cat_pipeline', cat_pipeline, categorical_columns)
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            # Strip spaces from column names
            train_df.columns = train_df.columns.str.strip()
            test_df.columns = test_df.columns.str.strip()

            logging.info("Read train and test data completed")
            logging.info(f"Train columns after cleaning: {list(train_df.columns)}")

            target_column_name = "loan_status"

            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            preprocessing_obj = self.get_data_transformer_object()

            logging.info("Applying preprocessing object on training and testing features.")

            X_train = preprocessing_obj.fit_transform(input_feature_train_df)
            X_test = preprocessing_obj.transform(input_feature_test_df)

            # Ensure dense arrays
            if sparse.issparse(X_train):
                X_train = X_train.toarray()
            if sparse.issparse(X_test):
                X_test = X_test.toarray()

            # Encode target labels
            le = LabelEncoder()
            y_train = le.fit_transform(target_feature_train_df.astype(str).str.strip())
            y_test = le.transform(target_feature_test_df.astype(str).str.strip())

            train_arr = np.c_[X_train, y_train]
            test_arr = np.c_[X_test, y_test]

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
