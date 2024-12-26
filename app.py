from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return (
        "Bonsoir, Welcome to the Agondo's Flask App! Please use the following endpoints:\n"
        "/add?num1=<num1>&num2=<num2> - To add two numbers.\n"
        "/subtract?num1=<num1>&num2=<num2> - To subtract two numbers."
    )

#Here we'll be adding two integers
@app.route('/add', methods=['GET'])
def add_numbers():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        result = num1 + num2
        return jsonify({
            "operation": "addition",
            "num1": num1,
            "num2": num2,
            "result": result
        })
    except ValueError:
        return jsonify({
            "error": "Invalid input. Please provide numbers."
        }), 400

#Here we'll be substructing two integers
@app.route('/subtract', methods=['GET'])
def subtract_numbers():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        result = num1 - num2
        return jsonify({
            "operation": "subtraction",
            "num1": num1,
            "num2": num2,
            "result": result
        })
    except ValueError:
        return jsonify({
            "error": "Invalid input. Please provide numbers."
        }), 400

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
