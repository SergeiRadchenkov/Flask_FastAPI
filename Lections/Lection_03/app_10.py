from flask import Flask, render_template
from models_05 import db, User
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'mydatabase.db')
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/data/')
def data():
    return 'You data!'


@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
