import os
import sys

import pandas as pd

from src.exception import CustomException
from src.utils import load_object

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join('artifacts', 'model.pkl')
            model = load_object(model_path)
            preds = model.predict(features)

            return preds
            
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                 age: int,
                 gender: str,
                 ethnicity: str,
                 education_level: str,
                 income_level: str,
                 employment_status: str,
                 smoking_status: str,
                 alcohol_consumption_per_week: int,
                 physical_activity_minutes_per_week: int,
                 diet_score: float,
                 sleep_hours_per_day: float,
                 screen_time_hours_per_day: float,
                 family_history_diabetes: int,
                 hypertension_history: int,
                 cardiovascular_history: int,
                 bmi: float,
                 waist_to_hip_ratio: float,
                 systolic_bp: int,
                 diastolic_bp: int,
                 heart_rate: int,
                 cholesterol_total: int,
                 hdl_cholesterol: int,
                 ldl_cholesterol: int,
                 triglycerides: int,
                 glucose_fasting: int,
                 glucose_postprandial: int,
                 insulin_level: float,
                 hba1c: float):
        self.age = age
        self.gender = gender
        self.ethnicity = ethnicity
        self.education_level = education_level
        self.income_level = income_level
        self.employment_status = employment_status
        self.smoking_status = smoking_status
        self.alcohol_consumption_per_week = alcohol_consumption_per_week
        self.physical_activity_minutes_per_week = physical_activity_minutes_per_week
        self.diet_score = diet_score
        self.sleep_hours_per_day = sleep_hours_per_day
        self.screen_time_hours_per_day = screen_time_hours_per_day
        self.family_history_diabetes = family_history_diabetes
        self.hypertension_history = hypertension_history
        self.cardiovascular_history = cardiovascular_history
        self.bmi = bmi
        self.waist_to_hip_ratio = waist_to_hip_ratio
        self.systolic_bp = systolic_bp
        self.diastolic_bp = diastolic_bp
        self.heart_rate = heart_rate
        self.cholesterol_total = cholesterol_total
        self.hdl_cholesterol = hdl_cholesterol
        self.ldl_cholesterol = ldl_cholesterol
        self.triglycerides = triglycerides
        self.glucose_fasting = glucose_fasting
        self.glucose_postprandial = glucose_postprandial
        self.insulin_level = insulin_level
        self.hba1c = hba1c

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "age": [self.age],
                "gender": [self.gender],
                "ethnicity": [self.ethnicity],
                "education_level": [self.education_level],
                "income_level": [self.income_level],
                "employment_status": [self.employment_status],
                "smoking_status": [self.smoking_status],
                "alcohol_consumption_per_week": [self.alcohol_consumption_per_week],
                "physical_activity_minutes_per_week": [self.physical_activity_minutes_per_week],
                "diet_score": [self.diet_score],
                "sleep_hours_per_day": [self.sleep_hours_per_day],
                "screen_time_hours_per_day": [self.screen_time_hours_per_day],
                "family_history_diabetes": [self.family_history_diabetes],
                "hypertension_history": [self.hypertension_history],
                "cardiovascular_history": [self.cardiovascular_history],
                "bmi": [self.bmi],
                "waist_to_hip_ratio": [self.waist_to_hip_ratio],
                "systolic_bp": [self.systolic_bp],
                "diastolic_bp": [self.diastolic_bp],
                "heart_rate": [self.heart_rate],
                "cholesterol_total": [self.cholesterol_total],
                "hdl_cholesterol": [self.hdl_cholesterol],
                "ldl_cholesterol": [self.ldl_cholesterol],
                "triglycerides": [self.triglycerides],
                "glucose_fasting": [self.glucose_fasting],
                "glucose_postprandial": [self.glucose_postprandial],
                "insulin_level": [self.insulin_level],
                "hba1c": [self.hba1c]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)