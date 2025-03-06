from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddOwnerForm(FlaskForm):

    name = StringField('Name of Owner: ')
    id_pup = IntegerField('Id of Puppy: ')
    submit = SubmitField('Add Owner')