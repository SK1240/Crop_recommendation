# 🌾 Crop Recommendation System
A smart **Machine Learning-powered** web app built using **Streamlit** and the **K-Nearest Neighbors (KNN)** algorithm to recommend the most suitable crop for cultivation based on soil nutrients and environmental conditions.
> 🧩 **This project was successfully completed as part of my _Data Science Internship_, showcasing practical implementation of data-driven agriculture solutions.**

## 🚀 Tech Stack

* 🐍 Python — core programming language for logic, computation, and machine learning workflows.

* 📊 pandas, NumPy — for efficient data preprocessing, manipulation, and numerical analysis.

* 🤖 scikit-learn (KNN Model) — used for building and training the K-Nearest Neighbors classification model.

* 💾 Pickle — utilized for saving and loading the trained model (`knn_crop_model`.pkl) to enable fast, reusable predictions.

* 🌐 Streamlit — for developing an interactive and lightweight web application with real-time user inputs.

## 🌱 Dataset

* Source: Dataset provided during my *Data Science Internship*, originally based on the *Kaggle Crop Recommendation Dataset*.

* Description: The dataset contains soil nutrient values and climatic parameters used to recommend the most suitable crop for cultivation.

* Features Used:

     * N (Nitrogen)

     * P (Phosphorus)

     * K (Potassium)

     * Temperature

     * Humidity

     * pH

     * Rainfall

     * Label (Crop Type)

## 🧠 Model Overview

The system employs the **K-Nearest Neighbors (KNN)** classification algorithm to analyze soil composition and environmental conditions.
By finding the “closest match” between user input and historical data, the model predicts which crop performs best in similar conditions.
This makes it an efficient, interpretable, and reliable recommendation system for farmers and agricultural researchers.

## 💡 How It Works

* User enters soil nutrients and environmental parameters through the **Streamlit interface**.

* The trained **KNN model** processes these values and compares them with the dataset.

* Based on similarity, the model outputs the recommended crop that is most likely to yield well.
