import pandas as pd
import pickle

model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

# Test multiple predictions
test_cases = [
    {'name': 'Maruti Suzuki Alto', 'company': 'Maruti', 'year': 2015, 'kms_driven': 60000, 'fuel_type': 'Petrol'},
    {'name': 'Honda City', 'company': 'Honda', 'year': 2015, 'kms_driven': 55000, 'fuel_type': 'Petrol'},
    {'name': 'Toyota Innova 2.0', 'company': 'Toyota', 'year': 2012, 'kms_driven': 82000, 'fuel_type': 'Diesel'},
    {'name': 'BMW 3 Series', 'company': 'BMW', 'year': 2014, 'kms_driven': 40000, 'fuel_type': 'Diesel'},
]

print("COMPARING PREDICTIONS WITH ACTUAL DATA:")
print("=" * 80)

df = pd.read_csv('Cleaned_Car_data.csv')

for test in test_cases:
    test_df = pd.DataFrame([test])
    pred = model.predict(test_df)[0]
    
    # Find similar cars in dataset
    similar = df[
        (df['name'] == test['name']) & 
        (df['fuel_type'] == test['fuel_type'])
    ]
    
    print(f"\nCar: {test['name']} ({test['year']}, {test['fuel_type']})")
    print(f"Test km: {test['kms_driven']:,}")
    print(f"Prediction: ₹{pred:,.2f}")
    
    if len(similar) > 0:
        print(f"Actual prices in dataset for this model:")
        for _, row in similar.head(3).iterrows():
            print(f"  Year {row['year']}, {row['kms_driven']:,} km: ₹{row['Price']:,}")
