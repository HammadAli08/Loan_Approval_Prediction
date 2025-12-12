# 🏦 Loan Approval Prediction System

An end-to-end machine learning project that predicts loan approval status based on applicant information using various classification algorithms.

## 📋 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [API Endpoints](#api-endpoints)
- [Model Information](#model-information)
- [Contributing](#contributing)

## ✨ Features

- **Machine Learning Pipeline**: Complete ML pipeline with data ingestion, transformation, and model training
- **Multiple Algorithms**: Compares Random Forest, Decision Tree, Gradient Boosting, Logistic Regression, AdaBoost, and SVC
- **Web Interface**: User-friendly Flask web application for predictions
- **RESTful API**: Health check and prediction endpoints
- **Docker Support**: Containerized application for easy deployment
- **Azure Deployment**: CI/CD pipeline configured for Azure Web Apps
- **Logging**: Comprehensive logging for debugging and monitoring
- **Exception Handling**: Custom exception handling throughout the application

## 🛠 Tech Stack

- **Python 3.11+**
- **Flask** - Web framework
- **scikit-learn** - Machine learning algorithms
- **pandas & numpy** - Data manipulation
- **Gunicorn** - WSGI HTTP Server
- **Docker** - Containerization
- **Azure Web Apps** - Cloud deployment

## 📁 Project Structure

```
ML_Project/
├── src/
│   ├── Components/
│   │   ├── data_ingestion.py      # Data loading and splitting
│   │   ├── data_transformation.py  # Feature engineering
│   │   └── model_trainer.py        # Model training and evaluation
│   ├── Pipeline/
│   │   ├── predict_pipeline.py     # Prediction pipeline
│   │   └── training_pipeline.py    # Training orchestration
│   ├── Exception.py                # Custom exception handling
│   ├── Logger.py                   # Logging configuration
│   └── utils.py                    # Utility functions
├── templates/
│   ├── index.html                  # Input form
│   └── home.html                   # Results page
├── artifacts/                      # Trained models and data
├── logs/                          # Application logs
├── app.py                         # Flask application
├── Dockerfile                     # Docker configuration
├── requirements.txt               # Python dependencies
└── setup.py                       # Package setup

```

## 🚀 Installation

### Local Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd ML_Project
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Docker Setup

1. **Build the Docker image**
```bash
docker build -t loan-approval-prediction .
```

2. **Run the container**
```bash
docker run -p 8000:8000 loan-approval-prediction
```

The application will be available at `http://localhost:8000`

## 💻 Usage

### Web Interface

1. Navigate to `http://localhost:5000/loan_prediction`
2. Fill in the loan application form with:
   - Loan ID
   - Number of Dependents
   - Annual Income
   - Loan Amount
   - Loan Term (months)
   - CIBIL Score
   - Asset Values (Residential, Commercial, Luxury, Bank)
   - Education Level
   - Self-Employment Status
3. Click "Predict" to get the loan approval prediction

### Training the Model

To retrain the model with new data:

```bash
python src/Components/data_ingestion.py
```

This will:
1. Load the dataset
2. Split into train/test sets
3. Transform the data
4. Train multiple models
5. Save the best model to `artifacts/`

## 🌐 Deployment

### Docker Deployment

```bash
# Build
docker build -t loan-approval-prediction .

# Run
docker run -d -p 8000:8000 --name loan-app loan-approval-prediction

# Check logs
docker logs loan-app

# Stop
docker stop loan-app
```

### Azure Web Apps

The project includes a GitHub Actions workflow (`.github/workflows/main_loanapprovalprediction.yml`) for automatic deployment to Azure:

1. Push to the `main` branch
2. GitHub Actions will automatically build and deploy
3. Access your app at: `https://loanapprovalprediction.azurewebsites.net`

### Other Cloud Platforms

**AWS Elastic Beanstalk:**
```bash
eb init -p python-3.11 loan-approval-app
eb create loan-approval-env
eb deploy
```

**Google Cloud Run:**
```bash
gcloud run deploy loan-approval --source . --platform managed --region us-central1
```

**Heroku:**
```bash
heroku create loan-approval-prediction
git push heroku main
```

## 🔌 API Endpoints

### Health Check
```http
GET /health
```
Response:
```json
{
  "status": "healthy",
  "service": "loan-approval-prediction"
}
```

### Home
```http
GET /
```
Returns welcome message

### Loan Prediction Form
```http
GET /loan_prediction
```
Returns the prediction form

### Make Prediction
```http
POST /loan_prediction
Content-Type: application/x-www-form-urlencoded

loan_id=1234&no_of_dependents=2&income_annum=500000&...
```

## 🤖 Model Information

### Features Used

**Numerical Features:**
- loan_id, no_of_dependents, income_annum, loan_amount, loan_term
- cibil_score, residential_assets_value, commercial_assets_value
- luxury_assets_value, bank_asset_value

**Categorical Features:**
- education (Graduate/Not Graduate)
- self_employed (Yes/No)

### Models Evaluated

1. **Random Forest Classifier**
2. **Decision Tree Classifier**
3. **Gradient Boosting Classifier**
4. **Logistic Regression**
5. **AdaBoost Classifier**
6. **Support Vector Classifier (SVC)**

The best performing model (accuracy > 90%) is automatically selected and saved.

### Preprocessing

- **Numerical**: Median imputation + Standard scaling
- **Categorical**: Most frequent imputation + One-hot encoding + Scaling
- **Target**: Label encoding (Approved/Rejected)

## 📊 Performance

The model achieves:
- **Accuracy**: > 90% on test set
- **ROC-AUC**: Calculated for models supporting probability estimates

## 🐛 Troubleshooting

**Issue: Module not found**
```bash
pip install -r requirements.txt
```

**Issue: Port already in use**
```bash
# Change port in app.py or use different port
python app.py  # Modify the port in the file
```

**Issue: Model files missing**
```bash
# Retrain the model
python src/Components/data_ingestion.py
```

## 📝 License

This project is licensed under the MIT License.

## 👤 Author

**Hammad Ali Tahir**
- Email: hammadalitahir8@gmail.com

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For support, email hammadalitahir8@gmail.com or open an issue in the repository.

---

**Note**: Make sure to place your dataset at `src/Notebook/data/loan_approval_dataset.csv` before training the model.
