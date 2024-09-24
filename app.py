from flask import Flask, request, jsonify

## Create a Flask app
app = Flask(__name__)

## Define a route
@app.route('/', methods=['GET'])
def hello_world():
    return "Hello, World from Hants Williams!"

## run on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)

