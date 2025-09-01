# src/Pipeline/train_pipeline.py

import sys
from src.Exception import CustomException
from src.Logger import logging
from src.Components.data_ingestion import DataIngestion
from src.Components.data_transformation import DataTransformation
from src.Components.model_trainer import ModelTrainer

def run_training():
    try:
        logging.info("===== Training Pipeline Started =====")

        # 1. Data Ingestion
        data_ingestion = DataIngestion()
        train_data, test_data = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")

        # 2. Data Transformation
        data_transformation = DataTransformation()
        train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
            train_data, test_data
        )
        logging.info("Data Transformation Completed")

        # 3. Model Training
        model_trainer = ModelTrainer()
        model_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
        logging.info("Model Training Completed")

        logging.info(f"Training pipeline finished successfully with score: {model_score}")
        print(f"Training Completed. Final Model Score: {model_score}")

        logging.info("===== Training Pipeline Finished =====")

    except Exception as e:
        logging.error("Error in training pipeline")
        raise CustomException(e, sys)

if __name__ == "__main__":
    run_training()