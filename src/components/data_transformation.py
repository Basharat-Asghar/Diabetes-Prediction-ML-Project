import os
import sys
from dataclasses import dataclass

import pandas as pd
import numpy as np

from sklearn.Pipeline import Pipeline
from sklearn.Compose import ColumnTransformer
from sklearn.Preprocessing import StandardScaler, RobustScaler, OneHotEncoder

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
            pass
        except:
            pass