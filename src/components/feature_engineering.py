from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np

class FeatureEngineering(BaseEstimator, TransformerMixin):
    """
    Custom transformer for:
    - Creating new features
    - Dropping irrelevant columns
    """

    def __init__(self):
        pass

    def fit(self, X, y=none):
        return self

    def transform(self, X):
        try:
            X = X.copy()

            ### Create New Features
            X['homa_ir'] = (X['glucose_fasting'] * X['insulin_level']) / 405
            X['tg_hdl_ratio']= X['triglycerides'] / X['hdl_cholesterol']
            X['glysemic_gap'] = X['glucose_postprandial'] - X['glucose_fasting']
            X['mean_arterial_pressure'] = (2 * X['diastolic_bp'] + X['systolic_bp']) / 3
            X['obesity_risk_index'] = X['bmi'] * X['waist_to_hip_ratio']
            X['lifestyle_risk_score'] = (
                (1 / (X['physical_activity_minutes_per_week'] + 1)) +
                (1 / (X['diet_score'] + 1)) +
                X['screen_time_hours_per_day']
                )
            X['cardiometabolic_burden'] = (
                (X['hypertension_history'] == 1).astype(int) +
                (X['tg_hdl_ratio'] > 3).astype(int) +
                (X['bmi'] > 30).astype(int)
                >= 2
                ).astype(int)
            X['pulse_pressure'] = (
                X['systolic_bp'] - X['diastolic_bp']
                )
        
            ### Drop Columns
            drop_cols = ["diabetes_risk_score", "diabetes_stage"]
            X.drop(columns=drop_cols, inplace=True, errors='ignore')
            
            logging.info("Feature engineering completed successfully")

            return X
        except Exception as e:
            raise CustomException(e, sys)