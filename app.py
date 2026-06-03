from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np
import sys

# Monkeypatch for NumPy compatibility: numpy._core was introduced in NumPy 2.0.
# Our model pickle was created with a version that expects numpy._core.
# Map numpy._core and its submodules back to numpy for older versions.
if not hasattr(np, '_core'):
    # Create a namespace that redirects to numpy
    class NumpyCoreProxy:
        def __getattr__(self, name):
            return getattr(np, name)
    
    np._core = NumpyCoreProxy()
    sys.modules['numpy._core'] = np._core
    sys.modules['numpy._core.multiarray'] = np  # numpy.core.multiarray exists in older numpy
    if hasattr(np.core, 'multiarray'):
        sys.modules['numpy._core.multiarray'] = np.core.multiarray

app = Flask(__name__)

cors = CORS(app)

model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

car = pd.read_csv('Cleaned_Car_data.csv')


@app.route('/', methods=['GET', 'POST'])
def index():

    companies = sorted(car['company'].unique())

    car_models = sorted(car['name'].unique())

    years = sorted(car['year'].unique(), reverse=True)

    fuel_types = car['fuel_type'].unique()

    companies.insert(0, 'Select Company')

    return render_template(
        'index.html',
        companies=companies,
        car_models=car_models,
        years=years,
        fuel_types=fuel_types
    )


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    try:
        company = request.form.get('company')
        car_model = request.form.get('car_models')
        year = int(request.form.get('year'))
        fuel_type = request.form.get('fuel_type')
        driven = int(request.form.get('kilo_driven'))

        # Create DataFrame with proper data types
        input_df = pd.DataFrame({
            'name': [car_model],
            'company': [company],
            'year': [year],
            'kms_driven': [driven],
            'fuel_type': [fuel_type]
        })
        
        # Ensure numeric columns are numeric
        input_df['year'] = input_df['year'].astype(int)
        input_df['kms_driven'] = input_df['kms_driven'].astype(int)

        prediction = model.predict(input_df)
        return str(np.round(prediction[0], 2))
    except Exception as e:
        return str(e), 400


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)