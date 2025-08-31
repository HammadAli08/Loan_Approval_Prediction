from flask import Flask, jsonify, render_template, request
import numpy as np
import pandas as pd
from src.utils import load_object
from src.Pipeline.predict_pipeline import Predictpipeline, costum_data

from sklearn.preprocessing import StandardScaler, OneHotEncoder

application = Flask(__name__)

app = application

# Route for the home page
@app.route('/')
def home():
    return "Welcome to the Loan Approval Prediction API!"

@app.route('/predict', methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('index.html')
    else:
        data=costum_data(
            loan_id = int(request.form.get('loan_id')),
            no_of_dependents = int(request.form.get('no_of_dependents')),
            income_annum = float(request.form.get('income_annum')),
            loan_amount = float(request.form.get('loan_amount')),
            loan_term = float(request.form.get('loan_term')),
            cibil_score = float(request.form.get('cibil_score')),
            residential_assets_value = float(request.form.get('residential_assets_value')),
            commercial_assets_value = float(request.form.get('commercial_assets_value')),
            luxury_assets_value = float(request.form.get('luxury_assets_value')),
            bank_asset_value = float(request.form.get('bank_asset_value')),
            education = request.form.get('education'),
            self_employed = request.form.get('self_employed')
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        predict_pipeline=Predictpipeline()
        results=predict_pipeline.predict(pred_df)
        return render_template('index.html', results=results[0])
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
 
