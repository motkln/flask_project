from app import app
from flask import render_template

@app.route('/hello')
def hello():
    return 'Hello, world!'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/info')
def show_info():
    return 'This is informational page.'


@app.route('/calc/<number1>/<number2>')
def sum_two(number1, number2):
    try:
        res = f'The sum of {number1} and {number2} is {int(number1) + int(number2)}'
    except Exception:
        return 'Both arguments must be integers'
    else:
        return res


@app.route('/reverse/<input_str>')
def reverse_str(input_str):
    return input_str[::-1]


@app.route('/reverse/')
def error_reverse():
    return 'String lenght must be at least 1'


@app.route('/user/<name>/<int:age>')
def name_age(name, age):
    if age > 0:
        return f'Hello, {name}. You are {age} years old.'
    else:
        return 'Your age can not be less than 0'


if __name__ == '__main__':
    app.run(debug=True)
