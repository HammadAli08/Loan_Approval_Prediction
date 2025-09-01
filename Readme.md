# 🚀 Loan Approval Prediction 🏦✨

<p align="center">
  <img src="https://media.giphy.com/media/xT9IglZzyhrlHX1Syk/giphy.gif" width="250" />
</p>

## 🌟 About the Project
Tired of long manual loan approval processes?  
This **Loan Approval Prediction System** uses **Machine Learning** to instantly predict whether a loan should be **Approved ✅** or **Rejected ❌**.  

With an impressive **97% accuracy**, this project demonstrates how AI can streamline financial decision-making! 🎯  

---

## 📊 Input Columns (What You Provide)
To get the prediction, you’ll need to provide these details:

| Column Name            | Description                                      |
|------------------------|--------------------------------------------------|
| `Gender`              | Male / Female 👨👩 |
| `Married`             | Yes / No 💍 |
| `Dependents`          | Number of dependents 👶 |
| `Education`           | Graduate / Not Graduate 🎓 |
| `Self_Employed`       | Yes / No 🏢 |
| `ApplicantIncome`     | Monthly income of applicant 💵 |
| `CoapplicantIncome`   | Monthly income of co-applicant 💵 |
| `LoanAmount`          | Loan amount requested 💰 |
| `Loan_Amount_Term`    | Duration of loan in months ⏳ |
| `Credit_History`      | 1 (Good) / 0 (Bad) 📈📉 |
| `Property_Area`       | Urban / Semiurban / Rural 🏙️🌆🌄 |

---

## 🎯 Output (What You Get)
After feeding the above data, the model will predict:

- **Loan_Status** →  
  ✅ **Approved**  
  ❌ **Rejected**  

<p align="center">
  <img src="https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif" width="300" />
</p>

---

## ⚡ Accuracy
- Achieves a **97% prediction accuracy** 📈  
- Trained on real-world loan applicant data 🗂️  
- Optimized using feature engineering + ML pipelines 🛠️  

---

## 🛠️ Tech Stack
- **Python** 🐍  
- **Pandas / NumPy** for data handling  
- **Scikit-Learn** for machine learning models  
- **Matplotlib / Seaborn** for data visualization  

---

## 🚀 How to Run Locally
```bash
# Clone the repository
git clone https://github.com/HammadAli08/Loan_Approval_Prediction.git

# Navigate to the project folder
cd Loan_Approval_Prediction

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
