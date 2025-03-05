from flask import Flask,render_template,flash,redirect,url_for,session
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class SimpleForm(FlaskForm):

    breed = StringField('What breed you are?',validators=[DataRequired()])
    submit = SubmitField("Click on Me.")


@app.route('/',methods = ["GET","POST"])
def index():
    
    form = SimpleForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(f'You just changed you breed to: {session['breed']}')
        return redirect(url_for('index'))


    return render_template('index.html',form = form)

if __name__ == '__main__':
    app.run(debug=True)