import pickle

# Load the model

input_file = 'model_C=1.0.bin'


# Load the model from the pickle file
with open(input_file, 'rb') as f_in: 
    dv, model = pickle.load(f_in)


dv, model


customer = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}


X = dv.transform([customer])
X


y_pred = model.predict_proba(X)[0, 1]


print('input:', customer)
print('output:', y_pred)
