import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selction import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    pass