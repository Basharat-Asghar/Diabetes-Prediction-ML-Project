# 🩺 Diabetes Risk Prediction – End-to-End Machine Learning Web Application

## 📌 Project Overview

This project is an end-to-end machine learning solution designed to predict the risk of diabetes based on lifestyle, demographic, and clinical health indicators.  

The goal is to help identify individuals who may be at higher risk of diabetes so that early interventions and preventive care can be encouraged.

The complete system follows **industry best practices**, including:
- Modular coding architecture
- Feature engineering 
- Data transformation
- Machine learning pipelines   
- Model training and evaluation  
- Web application development using Flask  
- Cloud deployment with Render 

---

## 🌐 Live Application

You can access the deployed web application here:

🔗 **Live Demo:**  
https://diabetes-prediction-app-8y4j.onrender.com

## 📸 Web Application Screenshots

![Input Form](screenshots/diabetes_prediction_webapp_1.png)
![Prediction Result](screenshots/diabetes_prediction_webapp_2.png)

---

## 🎯 Key Objectives

- Build a **reliable diabetes prediction model**
- Follow **clean software engineering principles**
- Ensure **training-serving consistency**
- Provide a **user-friendly web interface**
- Deploy the application to the cloud

---

## 📂 Project Structure

project_root/
|
├── artifacts/
│ └── model.pkl # Trained ML pipeline
| └── data.csv
| └── test.csv
| └── train.csv
|
├── notebook/
| └── 1_EDA_Diabetes_Prediction.ipynb
| └── 2_Model_Training.ipynb
|
├── screenshots/
│
├── src/
│ ├── components/
| | ├── __init__.py
│ │ ├── data_ingestion.py
│ │ ├── feature_engineering.py
│ │ ├── data_transformation.py
│ │ └── model_trainer.py
│ │
│ ├── pipeline/
| | ├── __init__.py
│ │ ├── train_pipeline.py
│ │ └── predict_pipeline.py
│ │
| ├── __init__.py
│ ├── utils.py
| ├── logger.py
| └── exception.py
|
├── templates/
│ └── index.html # Web UI
|
├── .gitignore
├── app.py # Flask web application
├── render.yaml
├── requirements.txt # Dependencies
├── setup.py