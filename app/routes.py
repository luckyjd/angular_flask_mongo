from app import app, db
from flask import render_template, flash, redirect, url_for, request, session, jsonify
from app.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from functools import wraps
from bson.json_util import dumps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect('/login?next=%s' % request.url)
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/api/index')
def api_index():
    if 'username' in session:
        msg = [{'title': 'Home', 'type': 'logged', 'user': 'username'}]
        return dumps(msg)
    else:
        msg = [{'title': 'Home', 'type': 'none'}]
        return dumps(msg)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.User.find_one({'username': form.username.data})
        if user is None or not check_password_hash(user['password_hash'], form.password.data):
            flash("Invalid username or pass")
            return redirect(url_for('login'))
        session['username'] = form.username.data
        #session['role'] = user.user_role
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Log In', form=form)


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = db.User.insert_one(
            {
                'username': form.username.data,
                'password_hash': generate_password_hash(form.password.data),
                'user_role': 2
            }
        )
        flash('Registered successful')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


def check_role(id):
    if db.User.find_one({'account_number': int(id)}):
        return db.User.find_one({'account_number': int(id)}).user_role
    else:
        return False


@app.route('/api/role', methods=['GET', 'POST'])
def api_role():
    if request.args.get('id'):
        return check_role(request.args.get('id'))





@app.route('/search', methods=['GET', 'POST'])
def search():
    list_account = dumps(db.Account.find())
    return list_account


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    acc_number = request.args.get('id')
    raw = db.Account.delete_one({'account_number': int(acc_number)})
    return 'True'




