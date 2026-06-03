import pandas as pd
import pickle
import numpy as np

# Load data
df = pd.read_csv('Cleaned_Car_data.csv')

# Check Toyota Corolla prices
print("=" * 60)
print("TOYOTA COROLLA PRICES IN DATASET:")
print("=" * 60)
toyota_corolla = df[df['name'].str.contains('Toyota Corolla', na=False)]
print(toyota_corolla[['name', 'year', 'Price', 'kms_driven', 'fuel_type']])

print("\n" + "=" * 60)
print("PRICE STATISTICS:")
print("=" * 60)
print(f"Min Price: ₹{df['Price'].min():,.0f}")
print(f"Max Price: ₹{df['Price'].max():,.0f}")
print(f"Mean Price: ₹{df['Price'].mean():,.0f}")
print(f"Median Price: ₹{df['Price'].median():,.0f}")
print(f"Std Dev: ₹{df['Price'].std():,.0f}")

# Load model and check what it's expecting
print("\n" + "=" * 60)
print("MODEL INFO:")
print("=" * 60)
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
print(f"Model type: {type(model)}")
print(f"Model: {model}")

# Test prediction
print("\n" + "=" * 60)
print("TEST PREDICTION:")
print("=" * 60)
test_df = pd.DataFrame({
    'name': ['Toyota Corolla'],
    'company': ['Toyota'],
    'year': [2015],
    'kms_driven': [50000],
    'fuel_type': ['Petrol']
})

print(f"Input: {test_df.to_dict('records')}")
try:
    pred = model.predict(test_df)
    print(f"Prediction: ₹{pred[0]:,.2f}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
