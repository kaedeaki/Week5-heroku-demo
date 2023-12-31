import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/predict', methods=['POST'])
def predict():

    flag = False
    if request.method == "POST":
        area = int(request.form.get('area'))
        bedrooms = int(request.form.get('bedrooms'))
        bathrooms = int(request.form.get('bathrooms'))
        stories = float(request.form.get('stories'))
        parking = float(request.form.get('parking'))

        basement_input = request.form.get('basement_yes')
        basement_yes = 1 if basement_input == "Yes" else 0

        hotwaterheating_input = request.form.get('hotwaterheating_yes')
        hotwaterheating_yes = 1 if basement_input == "Yes" else 0

        final_features = [area, bedrooms, bathrooms, stories, parking, basement_yes, hotwaterheating_yes]
        features = [np.array(final_features)]

    prediction = model.predict(features)

    output = round(prediction[0], 2)

    return render_template('index2.html', flag=True, prediction_text=f'Housing price should be ${output}.')

if __name__ == "__main__":
    app.run(debug=True)