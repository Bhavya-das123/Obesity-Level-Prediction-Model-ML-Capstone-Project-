🍔 Obesity Level Prediction Model – ML Capstone Project

📌 Project Overview

This project is a Machine Learning–based Obesity Level Prediction System that predicts a person's obesity category based on their lifestyle, physical attributes, and eating habits.
It uses supervised machine learning models and is deployed as a Streamlit web application for real-time user interaction.
The system helps in early health risk identification and supports preventive healthcare decision-making.

🎯 Objectives

Predict obesity level using medical and lifestyle data
Apply data preprocessing and feature engineering
Train and evaluate machine learning models
Deploy a user-friendly web interface using Streamlit

🧠 Obesity Levels Predicted

The model predicts the following categories:

Code	Description
Insufficient_Weight	Underweight
Normal_Weight	Healthy weight
Overweight_Level_I	Mild overweight
Overweight_Level_II	High overweight
Obesity_Type_I	Obese
Obesity_Type_II	Severely obese
Obesity_Type_III	Morbidly obese

🛠 Technologies Used

Category	Tools
Programming	Python
Data Handling	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Machine Learning	Scikit-Learn
Model Deployment	Streamlit
Model Storage	Pickle

📊 Dataset Features

The dataset contains the following attributes:

Age
Height
Weight
Eating habits (CAEC, CALC)
Physical activity
Family history
Lifestyle indicators

These features are processed using Label Encoding, One-Hot Encoding, and Feature Scaling before training.

🔁 Workflow

Data Collection
Data Cleaning & Preprocessing
Feature Engineering
Model Training
Model Evaluation
Model Saving (Pickle)
Web App Deployment

🧪 Model Training
Multiple ML models were tested:
Logistic Regression
Random Forest
Decision Tree
Gradient Boosting

The best-performing model was selected based on:
Accuracy
R² Score
Overfitting/Underfitting checks

🌐 Web Application

The Streamlit UI allows users to:
Enter personal health details
Predict obesity level
View BMI score
Receive personalized health recommendations

🖥 How to Run This Project Locally
Step 1: Clone the repository
git clone https://github.com/yourusername/Obesity-Level-Prediction-Model-ML-Capstone-Project.git

Step 2: Install dependencies
pip install -r requirements.txt

Step 3: Run the app
streamlit run app.py

📁 Project Structure
Obesity-Level-Prediction-Model/
│
├── app.py
├── obesity_model.sav
├── scaler.sav
├── features.sav
├── dataset.csv
├── requirements.txt
└── README.md

📈 Output

The system displays:

Predicted obesity level
BMI score
Health recommendations

🚀 Future Enhancements

Mobile application
Deep learning model
Diet and workout suggestions
Doctor consultation integration

👨‍💻 Author

Bhavya Das
Machine Learning Enthusiast

📜 License
This project is for academic and learning purposes.
