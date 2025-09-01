# 💰 Loan Approval Prediction App  

Predict whether a loan application will be approved or not using **Machine Learning** 🚀.  
This project is deployed on **Azure Web App** and powered by a custom-trained model.  

---

## ✨ Demo Preview  

> 🌍 Try it live here: [Loan Prediction App](https://your-azure-app-link)  

### 🖼️ Screenshots  
![App Screenshot](https://via.placeholder.com/900x450.png?text=Loan+Approval+Prediction+App)  

---

## 📊 Dataset Overview  

Our dataset contains detailed information about applicants to help predict loan approval.  

### 🗂️ Features Used in the Model  

| Column Name               | Data Type | Description |
|---------------------------|-----------|-------------|
| `loan_id`                 | int       | Unique loan identifier |
| `no_of_dependents`        | int       | Number of dependents |
| `income_annum`            | float     | Applicant’s annual income |
| `loan_amount`             | float     | Total loan amount applied for |
| `loan_term`               | float     | Duration of loan (months/years) |
| `cibil_score`             | float     | Applicant’s CIBIL credit score |
| `residential_assets_value`| float     | Value of residential assets |
| `commercial_assets_value` | float     | Value of commercial assets |
| `luxury_assets_value`     | float     | Value of luxury assets (car, jewelry, etc.) |
| `bank_asset_value`        | float     | Total bank assets value |
| `education`               | str       | Applicant’s education status |
| `self_employed`           | str       | Whether applicant is self-employed (Yes/No) |

---

## ⚙️ How It Works  

1. 📝 User enters loan application details.  
2. 🤖 Machine learning model analyzes the data.  
3. ✅ Output: *Loan Approved* or ❌ *Loan Rejected*.  

---

## 🛠️ Tech Stack  

- **Python** 🐍  
- **Scikit-Learn** for ML  
- **Flask** backend  
- **Azure Web App** deployment  
- **GitHub Actions** CI/CD  

---

## 🎬 Interactive Flow  

```mermaid
graph LR
A[User Input] --> B[Flask API]
B --> C[ML Model Prediction]
C --> D{Approved?}
D -->|Yes| E[✅ Loan Approved]
D -->|No| F[❌ Loan Rejected]
