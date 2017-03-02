from flask import Flask,render_template,session,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required
app = Flask(__name__)
app.config['SECRET_KEY']='itsveryhardtoguess'
moment=Moment(app)
bootstrap=Bootstrap(app)

# @app.route('/index')
# def hello_world():
#     return render_template('index.html',current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

class NameForm(FlaskForm):
    name=StringField('what\'s your name?',validators=[Required()])
    submit=SubmitField('Submit')

@app.route('/index',methods=['GET','POST'])
def index():
    form=NameForm()
    if form.validate_on_submit():
        session['name']=form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'))
if __name__ == '__main__':
    app.run()