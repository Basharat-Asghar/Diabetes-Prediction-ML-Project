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
        X = X.copy()