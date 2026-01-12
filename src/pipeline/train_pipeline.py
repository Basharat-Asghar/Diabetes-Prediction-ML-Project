import os
import sys
from dataclasses import dataclass

import pandas as pd
import numpy as np

from src.exception import CustomException
from src.logger import logging
#from src.components.data_ingestion import DataIngestion
from src.components.model_trainer import ModelTrainer
from src.utils import save_object

'''
@dataclass
class TrainPipelineConfig:
    train_pipeliine_obj_path: str = os.path.join('artifacts', 'model.pkl')
'''

class TrainPipeline:
    '''
    def __init__(self):
        self.train_pipeline_config = TrainPipelineConfig()
    '''

    def run_train_pipeline(self):
        try:
            train_path = os.path.join('artifacts', 'train.csv') 
            test_path = os.path.join('artifacts', 'test.csv')
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data completed")

            X_train = train_df.drop('diagnosed_diabetes', axis=1)
            y_train = train_df['diagnosed_diabetes']
            X_test = test_df.drop('diagnosed_diabetes', axis=1)
            y_test = test_df['diagnosed_diabetes']
            logging.info("Train & Test set split is completed")

            trainer = ModelTrainer()
            pipeline = trainer.build_pipeline()
            pipeline.fit(X_train, y_train)
            logging.info("Training pipeline build is completed")

            # os.makedirs(os.path.dirname(self.train_pipeline_config.train_pipeliine_obj_path), exist_ok=True)
            model_obj_path = os.path.join('artifacts', 'model.pkl')
            save_object(model_obj_path, pipeline)
            logging.info("Model is saved")

            # return pipeline
        except Exception as e:
            raise CustomException(e, sys)