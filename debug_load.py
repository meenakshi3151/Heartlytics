import joblib

try:
    joblib.load("xgbm_model_with_tuned_params.pkl")
except Exception as e:
    print("\n------------------------------------")
    print("FINAL ERROR MESSAGE:")
    print("------------------------------------\n")
    print(repr(e))
    print("\n------------------------------------")
    raise
