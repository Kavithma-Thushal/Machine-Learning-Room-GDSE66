from flask import Flask, request, jsonify
import joblib

# Load the pre-trained model
model = joblib.load('music-recommender.joblib')

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        age = data['age']
        gender = data['gender']

        predictions = model.predict([[age, gender]])
        prediction_list = predictions.tolist()

        return jsonify({'prediction': prediction_list})

    except Exception as e:
        return jsonify({'error': str(e)})


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
