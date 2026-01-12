import os
import sys

from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

from src.logger import logging
from src.exception import CustomException
from src.components.feature_engineering import FeatureEngineering
from src.components.data_transformation import DataTransformation

class ModelTrainer:
    def build_pipeline(self):
        try:
            fe = FeatureEngineering()
            transformer = DataTransformation.get_data_transformer_object()

            model = RandomForestClassifier(
            n_estimators=500,
            max_depth=8,
            min_samples_split=100,
            min_samples_leaf=50,
            n_jobs=-1,
            random_state=42
            )

            pipeline = Pipeline(
                [
                    ('feature_engineering', fe),
                    ('preprocessor', transformer),
                    ('model', model)
                ]
            )
            logging.info('RandomForest Model Pipeline is Created')

            return model
        except Exception as e:
            raise CustomException(e, sys)
