# The model trainer will take the transformed data and train the model.

import os
import sys
from dataclasses import dataclass

from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split

from src.Logger import logging
from src.Exception import CustomException
from src.utils import save_object
from src.utils import evaluate_models
import numpy as np

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting training and test input data")

            # Last column is the encoded target from DataTransformation
            X_train, y_train = train_array[:, :-1], train_array[:, -1].astype(int)
            X_test, y_test = test_array[:, :-1], test_array[:, -1].astype(int)

            models = {
                "Random Forest": RandomForestClassifier(),
                "Decision Tree": DecisionTreeClassifier(),
                "Gradient Boosting": GradientBoostingClassifier(),
                "Logistic Regression": LogisticRegression(max_iter=1000),
                "AdaBoost Classifier": AdaBoostClassifier(),
                "SVC": SVC()  # decision_function will be used for ROC-AUC if this wins
            }

            model_report: dict = evaluate_models(
                X_train=X_train, X_test=X_test, y_test=y_test,
                y_train=y_train, models=models
            )

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            if best_model_score < 0.9:
                raise CustomException("No best model found")

            logging.info("Best model found on both training and testing dataset")

            # Persist best model
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            logging.info("Trained model saved")

            # Predictions and scores
            preds = best_model.predict(X_test)

            # Compute ROC-AUC robustly (use probabilities if available, else decision scores)
            roc_auc = None
            try:
                if hasattr(best_model, "predict_proba"):
                    y_score = best_model.predict_proba(X_test)[:, 1]
                    roc_auc = roc_auc_score(y_test, y_score)
                elif hasattr(best_model, "decision_function"):
                    y_score = best_model.decision_function(X_test)
                    roc_auc = roc_auc_score(y_test, y_score)
            except Exception as _:
                roc_auc = None  # fallback if something odd happens

            accuracy = accuracy_score(y_test, preds)

            print("Best Model Name:", best_model_name)
            if roc_auc is not None:
                print("Best Model ROC AUC Score:", roc_auc)
            else:
                print("Best Model ROC AUC Score: N/A (no suitable score output)")
            print("Best Model Accuracy Score:", accuracy)

            return {"roc_auc": roc_auc, "accuracy": accuracy, "model": best_model_name}

        except Exception as e:
            raise CustomException(e, sys)