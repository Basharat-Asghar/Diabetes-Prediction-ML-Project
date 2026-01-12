import os
import sys
from dataclasses import dataclass

import pandas as pd
import numpy as np

from sklearn.Pipeline import Pipeline
from sklearn.Compose import ColumnTransformer
from sklearn.Preprocessing import StandardScaler, RobustScaler, OneHotEncoder, OrdinalEncoder

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            num_feat = [
                'age', 'alcohol_consumption_per_week', 'diet_score', 'sleep_hours_per_day',
                'screen_time_hours_per_day', 'bmi', 'waist_to_hip_ratio', 'diastolic_bp',
                'heart_rate', 'cholesterol_total', 'hdl_cholesterol', 'glucose_fasting',
                'glucose_postprandial', 'hba1c', 'homa_ir', 'tg_hdl_ratio', 'glysemic_gap',
                'mean_arterial_pressure', 'obesity_risk_index', 'lifestyle_risk_score',
                'pulse_pressure'
                ]
            num_feat_skewed = [
                            'physical_activity_minutes_per_week', 'systolic_bp',
                            'ldl_cholesterol', 'triglycerides', 'insulin_level'
                            ]
            cat_feat = ['gender', 'ethnicity', 'employment_status', 'smoking_status']
            ordinal_feat = ['education_level', 'income_level']

            education_order = [
                'No formal', 'Highschool', 'Graduate', 'Postgraduate'
            ]

            income_order = [
                'Low', 'Lower-Middle', 'Middle', 'Upper-Middle', 'High'
            ]

            num_std_pipeline = Pipeline(
                steps=[
                    ('scaler', StandardScaler())
                ]
            )

            num_robust_pipeline = Pipeline(
                steps=[
                    ('robust_scaler', RobustScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ('one_hot_encoder', OneHotEncoder())
                ]
            )

            ordinal_pipeline = Pipeline(
                steps=[
                    ('ordinal_encoder', OrdinalEncoder(
                        categories=['education_order','income_order']
                    ))
                ]
            )
            logging.info("Numerical and categorical pipelines created")

            preprocessor = ColumnTransformer(
                [
                    ('num_std_pipeline', num_std_pipeline, num_feat),
                    ('num_robust_pipeline', num_robust_pipeline, num_feat_skewed),
                    ('cat_pipeline', cat_pipeline, cat_feat),
                    ('ordinal_pipeline', ordinal_pipeline, ordinal_feat)
                ],
                remainder='passthrough'
            )

            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)
    '''
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessor object")
            preprocessor_obj = self.get_data_transformer_object()

            target_column_name = 'diagnosed_diabetes'
        except Exception as e:
            raise CustomException(e, sys)
    '''