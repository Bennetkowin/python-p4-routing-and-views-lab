#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# 1. Index Route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# 2. Print String Route
@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # Print to console
    return f'<h1>{text}</h1>'  # Return text inside <h1> for display

# 3. Count Route
@app.route('/count/<int:number>')
def count(number):
    numbers = "<br>".join(str(i) for i in range(number + 1))  # 0 through number
    return f"<h1>{numbers}</h1>"

# 4. Math Route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'div':
            result = num1 / num2
        elif operation == 'mod':
            result = num1 % num2
        else:
            return f"<h1>Invalid operation: {operation}</h1>", 400
    except ZeroDivisionError:
        return "<h1>Error: Division or modulo by zero is not allowed.</h1>", 400

    return f"<h1>{result}</h1>"

# Run the Flask application
if __name__ == '__main__':
    app.run(port=5555, debug=True)

