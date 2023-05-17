import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app =Flask(__name__, template_folder='templates1', static_folder='static')
model = pickle.load(open('models1/best_model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index11.html')

@app.route('/predict',methods=['POST'])
def predict():
    age = int(request.form['age'])
    hypertension = int(request.form['hypertension'])
    heart_disease = int(request.form['heart_disease'])
    work_type = int(request.form['work_type'])
    avg_glucose_level = float(request.form['avg_glucose_level'])
    bmi = float(request.form['bmi'])
    smoking_status = int(request.form['smoking_status'])
    gender = int(request.form['gender'])
    marital_status = int(request.form['marital_status'])
    residence = int(request.form['residence_type'])

    features = {
    'age': age,
    'hypertension': hypertension,
    'heart_disease': heart_disease,
    'work_type': work_type,
    'avg_glucose_level': avg_glucose_level,
    'gender_Female': 0,
    'gender_Male': 0,
    'gender_Other': 0,
    'ever_married_No': 0,
    'ever_married_Yes': 0,
    'Residence_type_Rural': 0,
    'Residence_type_Urban': 0,
    'bmi': bmi,
    'smoking_status': smoking_status
    }

    if gender==0:
        features['gender_Female'] = 1
    elif gender==1:
        features['gender_Male'] = 1
    else:
        features['gender_Other'] = 1
    
    if marital_status == 0:
        features['ever_married_No'] = 1
    else:
        features['ever_married_Yes'] = 1

    if residence==0:
        features['Residence_type_Rural'] = 1
    else:
        features['Residence_type_Urban'] = 1

    for key, value in features.items():
        print(key, value)
    df = pd.DataFrame([features])
    prediction = model.predict(df) #model.predict(final)
    output = prediction[0]
    out = 'you might be safe!'
    if output == 1:
        out = 'you might suffer from stroke. contact your doc'
    
    return render_template('index11.html', prediction_text='{}'.format(out))

if __name__ == "__main__":
    app.run(debug = True)
