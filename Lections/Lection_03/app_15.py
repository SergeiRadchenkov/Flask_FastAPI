from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = b'2bc64352e8d6be54e518a6731e4a9e8330eee6130559ed5fb6c779bab3f88e3d'
scrf = CSRFProtect(app)
"""
Генерация надёжного секретного кода
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hi!'


@app.route('/form/', methods=['GET', 'POST'])
@scrf.exempt
def my_form():
    ...
    return 'No CSRF protection!'


if __name__ == '__main__':
    app.run(debug=True)
