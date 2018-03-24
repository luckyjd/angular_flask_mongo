from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
def default():
    return "nothing here"

@app.route('/index')
def index():
    user = {'username': 'nhattx'}
    posts = [
        {
            'author': {'username': 'nhattx2'},
            'body': 'that some shit things',
        },
        {
            'author': {'username': 'nhattx3'},
            'body': 'that some crazy things',
        }

    ]

    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me= {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

