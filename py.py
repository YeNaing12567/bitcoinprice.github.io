from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/prediction', methods=['GET'])
def get_prediction():
    # Example of prediction logic
    # Replace this with actual model prediction logic
    prediction = {'prediction': 'Up'}
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True)
