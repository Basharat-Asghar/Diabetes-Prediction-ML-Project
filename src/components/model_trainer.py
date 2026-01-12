import os
import sys

from sklearn.pipeline import Pipeline
from catboost import CatBoostClassifier

from src.logger import logging
from src.exception import CustomException
from src.components.feature_engineering import FeatureEngineering
from src.components.data_transformation import DataTransformation

class ModelTrainer:
    def build_pipeline(self):
        try:
            fe = FeatureEngineering()
            transformer = DataTransformation.get_data_transformer_object()

            model = CatBoostClassifier(
                iterations = 500,
                depth = 5,
                learning_rate = 0.01,
                verbose = 0,
                random_state = 42
            )

            pipeline = Pipeline(
                [
                    ('feature_engineering', fe),
                    ('preprocessor', transformer),
                    ('model', model)
                ]
            )
            logging.info('CatBoost Model Pipeline is Created')

            return model
        except Exception as e:
            raise CustomException(e, sys)
