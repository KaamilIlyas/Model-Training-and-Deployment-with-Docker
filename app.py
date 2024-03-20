from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/api/predict', methods=['POST'])
def predict():
    # Get the data from the request
    data = request.get_json()

    # Make prediction
    prediction = model.predict([data])

    # Return the prediction as JSON
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
