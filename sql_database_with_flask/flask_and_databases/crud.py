from basic import db, Puppy, app

with app.app_context():
    ### CREATE ###
    my_puppy = Puppy('Rufus', 5)
    db.session.add(my_puppy)
    db.session.commit()  


    ### READ ###
    all_puppies = Puppy.query.all() #list of puppies objects in the table!
    print(all_puppies)


    ### SELECT BY ID ###
    puppy_one = db.session.get(Puppy,1)
    print(puppy_one.name)


    ### FILTERS ###
    # PRODUCE SOME SQL CODE FOR US!
    puppy_frankie = Puppy.query.filter_by(name='Rufus')
    print(puppy_frankie.all())
    # ["Frankie is 3 year/s old"]


    ### UPDATE ###
    first_puppy = db.session.get(Puppy,1)
    first_puppy.age = 10
    db.session.add(first_puppy)
    db.session.commit()


    ### DELETE ###
    second_pup = db.session.get(Puppy,3)
    db.session.delete(second_pup)
    db.session.commit()


    #
    all_puppies = Puppy.query.all()
    print(all_puppies)