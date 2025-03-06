from flask import Blueprint, render_template,redirect,url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddOwnerForm


owners_blueprint = Blueprint('owners',__name__,
                             template_folder='templates/owners')




@owners_blueprint.route('/add', methods = ['GET','POST'])
def add_owner():

    form = AddOwnerForm()

    if form.validate_on_submit():
        name = form.name.data
        id_pup = form.id_pup.data
        new_owner = Owner(name,id_pup)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('puppies.list'))
    return render_template('add_owner.html', form=form)