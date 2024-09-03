from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'Главная',
        'name': 'Харитон'
    }
    responce = make_response(render_template('main.html', **context))
    responce.headers['new_head'] = 'New-value'
    responce.set_cookie('username', context['name'])
    return responce


@app.route('/getcookie/')
def get_cookies():
    # Получаем значения cookie
    name = request.cookies.get('username')
    return f'Значения cookies: {name}'


if __name__ == '__main__':
    app.run(debug=True)
