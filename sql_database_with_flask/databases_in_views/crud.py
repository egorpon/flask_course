from adoption_site import db, Owner, app

with app.app_context():
    db.session.query(Owner).filter(Owner.name == 'Chris').update({'id_pup': 1})
    db.session.commit()