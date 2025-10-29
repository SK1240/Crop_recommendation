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

## 🎯 Output

✅ **Recommended Crop Name** — optimized for soil and climate conditions provided by the user.

## 💻 Deployment

The application runs seamlessly through **Streamlit**, allowing real-time interaction with minimal setup.

The app can be deployed locally or hosted on platforms such as Streamlit Cloud or Render for wider accessibility.

## ⚙️ Quick Start

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/Crop-Recommendation-System.git
cd Crop-Recommendation-System
```

### 2️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Run the app
```
streamlit run app.py
```

## 🗂️ Project Structure
```
Crop_recommendation/
│
├── app.py                        # Main Streamlit web application
├── crop_recommendation.ipynb     # Jupyter Notebook for model training and analysis
├── knn_crop_model.pkl            # Trained KNN model file (stored using Pickle)
├── Crop_recommendation_data.csv  # Crop recommendation dataset 
├── requirements.txt              # List of dependencies
└── README.md                     # Project documentation

```

Each file serves a clear purpose:

* `app.py` → Handles the app’s logic and user interaction.

* `crop_recommendation.ipynb` → Contains data analysis, preprocessing, and model training steps.

* `knn_crop_model.pkl` → Stores the pre-trained KNN model for quick predictions.

* `Crop_recommendation_data.csv` → Dataset used during internship.

* `requirements.txt` → Ensures easy setup for other users or recruiters.

* `README.md` → Provides complete project documentation.

## 🌟 Highlights

🌿 Completed during Data Science Internship to apply ML in agriculture.

⚡ Predicts optimal crops with speed and accuracy.

💾 Stores trained model using Pickle for efficient loading.

📓 Includes Jupyter Notebook for transparent model-building workflow.

💬 Simple, interactive, and user-friendly Streamlit interface.
