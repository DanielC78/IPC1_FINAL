from flask import Flask, jsonify, request

operations = ["+", "-", "*", "/"]

app = Flask(__name__)
# Endpoints calculator


@app.route("/calculator", methods=["POST"])
def calculator():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid request", "status": 400}), 400
    if "number1" not in data or "number2" not in data or "operation" not in data:
        return jsonify({"error": "Fill all the fields", "status": 400}), 400
    if (type(data["number1"]) is not int and type(data["number1"]) is not float) or (type(data["number2"]) is not int and type(data["number2"]) is not float) or data["operation"] not in operations:
        return jsonify({"error": "Invalid data type", "status": 400}), 400
    if data["operation"] in operations:
        try:
            result = eval(
                f"{data['number1']}{data['operation']}{data['number2']}")
            return jsonify({"result": result, "status": 200})
        except ZeroDivisionError:
            return jsonify({"result": "Division by zero", "status": 400})
    else:
        return jsonify({"result": "Operation not found", "status": 400})

# Endpoints average


@app.route("/average", methods=["POST"])
def average():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid request", "status": 400}), 400
    if not "numbers" in data:
        return jsonify({"result": "Numbers not found", "status": 400})
    if not isinstance(data["numbers"], list):
        return jsonify({"result": "Is not list", "status": 400})
    if not data["numbers"]:
        return jsonify({"result": "Empty list", "status": 400})
    if data["numbers"] is None:
        return jsonify({"result": "No data", "status": 400})
    aux = 0

    for numbers in data["numbers"]:
        if numbers is None:
            return jsonify({"result": "No data", "status": 400})
        if type(numbers) is not int:
            return jsonify({"result": numbers+" is not a number", "status": 400})
        if type(numbers) is complex:
            return jsonify({"result": numbers+" is not a number", "status": 400})

    try:
        for i in data["numbers"]:
            aux += i
        return jsonify({"mean": aux/len(data["numbers"]), "status": 200})
    except ZeroDivisionError:
        return jsonify({"result": "Division by zero", "status": 400})


if __name__ == '__main__':
    app.run(debug=True)
