from flask import Flask, render_template, request
import pandas as pd

from src.pipeline.predict_pipeline import PredictionPipeline, CustomData

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        data = CustomData(
            age=int(request.form.get('age')),
            gender=request.form.get('gender'),
            ethnicity=request.form.get('ethnicity'),
            education_level=request.form.get('education_level'),
            income_level=request.form.get('income_level'),
            employment_status=request.form.get('employment_status'),
            smoking_status=request.form.get('smoking_status'),
            alcohol_consumption_per_week=int(request.form.get('alcohol_consumption_per_week')),
            physical_activity_minutes_per_week=int(request.form.get('physical_activity_minutes_per_week')),
            diet_score=float(request.form.get('diet_score')),
            sleep_hours_per_day=float(request.form.get('sleep_hours_per_day')),
            screen_time_hours_per_day=float(request.form.get('screen_time_hours_per_day')),
            family_history_diabetes=int(request.form.get('family_history_diabetes')),
            hypertension_history=int(request.form.get('hypertension_history')),
            cardiovascular_history=int(request.form.get('cardiovascular_history')),
            bmi=float(request.form.get('bmi')),
            waist_to_hip_ratio=float(request.form.get('waist_to_hip_ratio')),
            systolic_bp=int(request.form.get('systolic_bp')),
            diastolic_bp=int(request.form.get('diastolic_bp')),
            heart_rate=int(request.form.get('heart_rate')),
            cholesterol_total=int(request.form.get('cholesterol_total')),
            hdl_cholesterol=int(request.form.get('hdl_cholesterol')),
            ldl_cholesterol=int(request.form.get('ldl_cholesterol')),
            triglycerides=int(request.form.get('triglycerides')),
            glucose_fasting=int(request.form.get('glucose_fasting')),
            glucose_postprandial=int(request.form.get('glucose_postprandial')),
            insulin_level=float(request.form.get('insulin_level')),
            hba1c=float(request.form.get('hba1c'))
        )
