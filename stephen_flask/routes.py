from stephen_flask import app
from flask import render_template, url_for, redirect
from stephen_flask.forms import SignupForm, LoginForm

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html', title = 'Home')

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/account')
def account():
    return render_template('account.html', title = 'Accout')

@app.route('/signup',methods=['POST','GET'])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('signup.html', title = 'SignUp',form=form)

@app.route('/login',methods=['POST','GET'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='stephen@gmail.com' and form.password.data=='123456':
            return redirect(url_for('account'))
        else:
            return redirect(url_for('homepage'))
    return render_template('login.html', title = 'Login',form=form)