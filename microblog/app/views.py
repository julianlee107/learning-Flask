from flask import render_template,flash,redirect,request,url_for,g,session
from .forms import LoginForm,SignUpForm
from flask_login import login_user,logout_user,current_user,login_required
from .models import User,Post,Role_USER,Role_ADMIN
from app import app,db,lm
import datetime

@app.route('/')
@app.route('/index')
def index():
    user={
        'nickname':'Julian'
    }
    return render_template('index.html',user=user)
@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
@app.route('/login', methods=['GET', 'POST'])
def login():
    # 验证用户是否被验证
    if current_user.is_authenticated:
        return redirect('index')
    # 注册验证
    form = LoginForm()
    if form.validate_on_submit():
        user = User.login_check(request.form.get('user_name'))
        if user:
            login_user(user)
            user.last_seen = datetime.datetime.now()
            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("The Database error!")
                return redirect('/login')

            flash('Your name: ' + request.form.get('user_name'))
            flash('remember me? ' + str(request.form.get('remember_me')))
            return redirect(url_for("users", user_name=current_user.nickname))
        else:
            flash('Login failed, Your name is not exist!')
            return redirect('/login')

    return render_template(
        "login.html",
        title="Sign In",
        form=form)
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('index')
@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    user = User()
    if form.validate_on_submit():
        user_name = request.form.get('user_name')
        user_email = request.form.get('user_email')

        register_check = User.query.filter(db.or_(
            User.nickname == user_name, User.email == user_email)).first()
        if register_check:
            flash("error: The user's name or email already exists!")
            return redirect('/sign-up')

        if len(user_name) and len(user_email):
            user.nickname = user_name
            user.email = user_email
            user.role = Role_USER
            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("The Database error!")
                return redirect('/sign-up')

            flash("Sign up successful!")
            return redirect('/index')

    return render_template(
        "sign_up.html",
        form=form)
@app.route('/users')
def users():
    return 'hello world'
