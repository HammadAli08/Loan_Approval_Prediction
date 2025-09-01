from flask import Flask, jsonify, render_template, request
from src.utils import load_object
from src.Pipeline.predict_pipeline import Predictpipeline, costum_data
import pandas as pd

application = Flask(__name__)
app = application


# Home page
@app.route('/')
def home():
    return render_template('home.html')


# Prediction route
@app.route('/loan_predictions', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            # Collect form data
            data = costum_data(
                loan_id=int(request.form.get('loan_id')),
                no_of_dependents=int(request.form.get('no_of_dependents')),
                income_annum=float(request.form.get('income_annum')),
                loan_amount=float(request.form.get('loan_amount')),
                loan_term=float(request.form.get('loan_term')),
                cibil_score=float(request.form.get('cibil_score')),
                residential_assets_value=float(request.form.get('residential_assets_value')),
                commercial_assets_value=float(request.form.get('commercial_assets_value')),
                luxury_assets_value=float(request.form.get('luxury_assets_value')),
                bank_asset_value=float(request.form.get('bank_asset_value')),
                education=request.form.get('education'),
                self_employed=request.form.get('self_employed')
            )

            # Convert to DataFrame
            pred_df = data.get_data_as_data_frame()

            # Predict
            predict_pipeline = Predictpipeline()
            results = predict_pipeline.predict(pred_df)

            # Ensure results is displayable
            if isinstance(results, (list, pd.Series, pd.DataFrame)):
                results = results[0]

            return render_template('results.html', results=results)

        except Exception as e:
            # Friendly error page
            return render_template('results.html', results=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
