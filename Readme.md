# 🚀 Loan Approval Prediction App 🏦💳

![Loan Approval Animation](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzd5d3ZraHZ2b3Y2NGQ1dzZkYmZkYjlzbWR2Ymx0am82cW9naG4wbiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/qgQUggAC3Pfv687qPC/giphy.gif)

> 🌟 A smart ML application that predicts **loan approval chances** based on applicant data.  
> Interactive, intuitive, and designed with a touch of charm ✨.  

---

## 🎯 Features

- ✅ Predicts loan approval in real-time  
- ✅ User-friendly interface  
- ✅ Animated visualizations 📊  
- ✅ Deployed on **Azure Web Apps**  
- ✅ Uses key financial and personal features  

---

## 📊 Input Dataset Columns

To make a prediction, provide the following data:

| Column Name               | Type   | Description |
|---------------------------|--------|-------------|
| `loan_id`                 | int    | Unique loan identifier |
| `no_of_dependents`        | int    | Number of dependents |
| `income_annum`            | float  | Applicant’s annual income |
| `loan_amount`             | float  | Requested loan amount |
| `loan_term`               | float  | Loan term duration |
| `cibil_score`             | float  | Applicant’s credit score |
| `residential_assets_value` | float | Value of residential assets |
| `commercial_assets_value` | float  | Value of commercial assets |
| `luxury_assets_value`     | float  | Value of luxury assets |
| `bank_asset_value`        | float  | Total bank asset value |
| `education`               | str    | Education status |
| `self_employed`           | str    | Self-employed: Yes / No |

---

## 🎯 Output

The model returns:

```json
{ "Loan_Status": "Y" }
