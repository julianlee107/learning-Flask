from flask import render_template,flash,redirect,request,url_for,g,session
from .forms import Login
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
@app.route('/login',methods=['GET','POST'])
def login():
    # 验证用户
    if current_user.is_authenticated:
        return redirect('index')
    form=Login()
    if form.validate_on_submit():
        user=User.login_check(request.form.get('user_name'))
        if user:
            login_user(user)
            user.last_seen=datetime.datetime.now()
            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash('The Database error')
                return redirect('/login')
        else:
            flash('Login failed')
            return redirect('/login')
        return redirect('/index')
    return render_template('login.html',
                       title='Sign in',
                           form=form)
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('index')

