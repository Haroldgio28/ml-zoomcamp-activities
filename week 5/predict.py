import pickle
from flask import Flask
from flask import request
from flask import jsonify

# Load the model

input_file = 'model_C=1.0.bin'


# Load the model from the pickle file
with open(input_file, 'rb') as f_in: 
    dv, model = pickle.load(f_in)


dv, model

app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0',port=9696)
