# AI-Powered Customer Intelligence System (2026)

An end-to-end **Data Science & Machine Learning project** that predicts customer churn, segments customers, and provides actionable business insights using real-world data.

---

## 🚀 Project Overview

Customer churn is a critical problem for telecom and SaaS companies.  
This project builds a **production-style data science pipeline** that:

- Analyzes customer behavior
- Predicts customer churn using Machine Learning
- Segments customers using clustering
- Visualizes insights in an interactive dashboard

---

## 🧠 Key Features

- ✅ Data cleaning & preprocessing
- ✅ Exploratory Data Analysis (EDA)
- ✅ Churn prediction using **XGBoost**
- ✅ Customer segmentation using **KMeans**
- ✅ Interactive dashboard using **Streamlit**
- ✅ Industry-standard project structure

---

## 🛠 Tech Stack

- **Python**
- **Pandas, NumPy**
- **Matplotlib, Seaborn**
- **Scikit-learn**
- **XGBoost**
- **Jupyter Notebook**
- **Streamlit**

---

## 📂 Project Structure

customer-intelligence-ai/
│
├── data/
│ ├── raw/ # Raw dataset
│ └── processed/ # Cleaned data
│
├── notebooks/
│ ├── 01_eda.ipynb
│ └── 03_segmentation.ipynb
│
├── src/
│ ├── preprocessing.py
│ └── train_model.py
│
├── models/
│ └── churn_model.pkl
│
├── app/
│ └── dashboard.py
│
├── requirements.txt
└── README.md


---

## 📊 Dataset

- **Telco Customer Churn Dataset**
- Source: Kaggle  
- File used: `customers.csv`

---

## ⚙️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt

2️⃣ Run data preprocessing
python src/preprocessing.py

3️⃣ Train churn prediction model
python src/train_model.py

4️⃣ Run EDA & Segmentation

Open Jupyter Notebook:

jupyter notebook


Then run:

notebooks/01_eda.ipynb

notebooks/03_segmentation.ipynb

5️⃣ Launch dashboard
streamlit run app/dashboard.py

