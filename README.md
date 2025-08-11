# Student Performance Prediction using Linear Regression

## 📌 Project Overview
This project predicts a student's **Performance Index** based on various academic and extracurricular factors.  
It uses a **Linear Regression** model from `scikit-learn` to train and evaluate performance and is deployed using **Flask** for real-time predictions via a simple web interface.

---

## 📂 Dataset Information
The dataset contains the following features:

| Column                  | Description |
|-------------------------|-------------|
| Hours Studied           | Number of hours studied per day |
| Previous Scores         | Average previous academic scores |
| Extracurricular Activities | Whether the student participates in extracurricular activities (Yes=1, No=0) |
| Sleep Hours             | Average hours of sleep per day |
| Sample Question Papers Practiced | Number of sample question papers practiced |
| Performance Index       | Target variable - overall performance score |

---

## ⚙️ Installation

```bash
pip install pandas scikit-learn flask
