from flask import Flask, request, url_for
from markupsafe import escape


app = Flask(__name__)


@app.route('/')
def hello():
    return '<p>Hello, World!</p>'


@app.route('/<name>')
def greet(name):
    return f'Hello, {escape(name)}!'


@app.route('/post/<int:post_id>') # convert post_id to int
def show_post(post_id):
    next_post = post_id + 1
    return f'Post #{post_id} (next is #{next_post})'


@app.route('/path/<path:subpath>') # retains only the part after path/
def show_subpath(subpath):
    return f'And the subpath is: {escape(subpath)}'


#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        return do_login()
#    else:
#        return show_login_form()
    

# URL building
with app.test_request_context():
    print('hello:', url_for('hello'))
    print('greet:', url_for('greet', name='Bob Dobolina'))
    print('show_post:', url_for('show_post', post_id='33'))
    print('show_subpath:', url_for('show_subpath', subpath='part of a path'))
    print('styles:', url_for('static', filename='style.css'))
