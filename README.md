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


---

## 🔹 Modular Coding Approach

Instead of writing everything in one file, the project is divided into **logical modules**, each responsible for a specific task:

| Module | Purpose |
|--------|----------|
| Data Ingestion | Reads and loads dataset |
| Feature Engineering | Creates new meaningful features |
| Data Transformation | Scaling & encoding |
| Model Trainer | Builds and trains ML model |
| Train Pipeline | Orchestrates training |
| Predict Pipeline | Handles inference |
| Flask App | User interface |

This structure makes the system:
- Easy to maintain  
- Easy to debug  
- Production-ready  

---

## 🔹 Data Ingestion

**Purpose:**  
Load the dataset from a file source into a Pandas DataFrame.

**What happens:**
- Reads CSV file
- Performs basic validation
- Returns dataset for further processing

---

## 🔹 Feature Engineering

We create new features based on medical knowledge to improve model performance.

### Examples

**1. homa_ir**
**2. obesity_risk_indexr**
**3. lifestyle_risk_score**

---

## 🔹 Data Preprocessing

Different numerical features behave differently, so we use different scalers:

| Technique | Used for |
|-----------|----------|
| StandardScaler | Normally distributed data |
| RobustScaler | Data with outliers |
| Ordinal Encoding | Ordered categories |
| Pass-through | Nominal categories |

This ensures:
- No data leakage  
- Model stability  
- Real-world reliability  

---

## 🔹 Machine Learning Pipeline

We use **Scikit-learn Pipelines** to combine all steps:
> Feature Engineering → Preprocessing → Model

This guarantees:
- Same transformations during training & prediction  
- No manual preprocessing  
- Clean production workflow  

---