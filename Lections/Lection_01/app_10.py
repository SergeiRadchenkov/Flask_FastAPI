from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'

@app.route('/users/')
def users():
    _users = [
        {
            'name': 'Никанор',
            'email': 'nik@mail.ru',
            'phone': '+7-987-564-32-10',
        },
        {
            'name': 'Феофан',
            'email': 'feo@mail.ru',
            'phone': '+7-987-444-33-22',
        },
        {
            'name': 'Оверран',
            'email': 'forest@mail.ru',
            'phone': '+7-903-333-33-33',
        },
    ]
    context = {
        'users': _users,
        'title': 'Точечная нотация'
    }
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
