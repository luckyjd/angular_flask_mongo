from app import app, db
from flask import render_template, flash, redirect, url_for, request, session
from app.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect('/login?next=%s' % request.url)
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def default():
    return "nothing here"


# @app.route('/index')
# @login_required
# def index():
#     if 'username' in session:
#         return render_template('index.html', title='Home', username=session['username'])
#     else:
#         return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.User.find_one({'username': form.username.data})
        if user is None or not check_password_hash(user['password_hash'], form.password.data):
            flash("Invalid username or pass")
            return redirect(url_for('login'))
        session['username'] = form.username.data
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Log In', form=form)


@app.route('/logout')
def logout():
    session.pop('username', None)
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


@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    # choose database
    #if request.method == 'POST':

    list_account = db.Account.find()
    return render_template('accounts.html', title='Accounts', accounts=list_account, username=session['username'])






