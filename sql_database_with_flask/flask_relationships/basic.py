# CREATE ENTRIES INTO THE TABLES!
from models import db,Puppy,Owner,Toy,app


with app.app_context():
    #CREATING 2 PUPPIES

    # rufus = Puppy('Rufus')
    # fido = Puppy('Fido')

    # ADD PUPPIES TO DB

    # db.session.add_all([rufus,fido])
    # db.session.commit()

    # CHECK!
    print(Puppy.query.all())

    rufus = Puppy.query.filter_by(name = "Rufus").first()
    print(rufus)

    # CREATE OWNER OBJECT

    egor = Owner("Egor",rufus.id)

    # GIVE RUFUS SOME TOYS
    toy1 = Toy('Chew Toy',rufus.id)
    toy2 = Toy('Ball',rufus.id)
    toy3 = Toy('Bone',rufus.id)

    db.session.add_all([egor,toy1,toy2,toy3])
    db.session.commit()
    
    

    #GRAB RUFU AGAIN, AFTER THOSE ADDITIONS!
    rufus = Puppy.query.filter_by(name='Rufus').first()
    print(rufus)

    print(rufus.report_toys())
    # rufus = db.session.get(Puppy,1)
    # db.session.delete(rufus)
    # db.session.commit()