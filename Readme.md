# 💰 Loan Approval Prediction App 🏦✨

![Hero Animation](https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif)

> *"Transforming raw applicant data into instant, reliable loan decisions!"*  
> Built with **Machine Learning**, **Flask**, and **Azure deployment**, achieving **97% accuracy** ⚡  

---

## 📌 Features

- ✅ Real-time loan approval prediction  
- ✅ Interactive and charming interface  
- ✅ Animated demo & visual storytelling  
- ✅ Fully modular ML pipeline  
- ✅ Clean, production-ready code  

---

## 🏷️ Badges

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)  
![Accuracy](https://img.shields.io/badge/Accuracy-97%25-green)  
![License](https://img.shields.io/badge/License-MIT-yellow)  
![GitHub Repo Stars](https://img.shields.io/github/stars/HammadAli08/Loan_Approval_Prediction?style=social)  

---

## 📊 Dataset Overview

The ML model predicts loan approvals using the following features:

<details>
<summary>Click to expand input features</summary>

| Column Name               | Type   | Description |
|---------------------------|--------|-------------|
| `loan_id`                 | int    | Unique loan identifier |
| `no_of_dependents`        | int    | Number of dependents |
| `income_annum`            | float  | Annual income of applicant |
| `loan_amount`             | float  | Requested loan amount |
| `loan_term`               | float  | Loan term duration |
| `cibil_score`             | float  | Credit score of applicant |
| `residential_assets_value` | float | Value of residential assets |
| `commercial_assets_value` | float  | Value of commercial assets |
| `luxury_assets_value`     | float  | Value of luxury assets |
| `bank_asset_value`        | float  | Total bank asset value |
| `education`               | str    | Education status |
| `self_employed`           | str    | Self-employed: Yes / No |

</details>

---

## 🎯 Output

The prediction is simple:

<details>
<summary>Click to see model output</summary>

```json
{ "Loan_Status": "Y" }
