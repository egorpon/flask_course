from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    
    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):

    id = IntegerField('Id Number of Puppy to Remove: ')
    submit = SubmitField('Remove Puppy') 

class AddOwnerForm(FlaskForm):

    name = StringField('Name of Owner: ')
    id_pup = IntegerField('Id of Puppy: ')
    submit = SubmitField('Add Owner')

