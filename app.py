from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Flask backend is running.'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '').strip().lower()

    if message == 'hi':
        response = 'Hello!'
    else:
        response = "I don't understand."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
