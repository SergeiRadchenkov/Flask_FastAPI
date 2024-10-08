from flask import Flask, render_template, jsonify
from models_05 import db, User, Post
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


@app.route('/users/<username>/')
def users_by_username(username):
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify(
            [{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at}
             for post in posts])
    else:
        return jsonify({'error': 'Posts not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
