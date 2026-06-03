import pickle
with open('LinearRegressionModel.pkl', 'rb') as f:
    try:
        model = pickle.load(f)
    except ModuleNotFoundError as e:
        print("ModuleNotFoundError:", e)
        import traceback
        traceback.print_exc()
