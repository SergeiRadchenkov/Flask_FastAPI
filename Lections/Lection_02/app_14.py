from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    # Устанавливаем cookie
    responce = make_response('Cookie установлен')
    responce.set_cookie('username', 'admin')
    return responce


@app.route('/getcookie/')
def get_cookies():
    # Получаем значения cookie
    name = request.cookies.get('username')
    return f'Значения cookies: {name}'


if __name__ == '__main__':
    app.run(debug=True)
