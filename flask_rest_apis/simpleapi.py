from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from secure_check import authenticate 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)

api = Api(app)
jwt = JWTManager(app)


class Puppy(db.Model):

    name = db.Column(db.String(80), primary_key = True)

    def __init__(self,name):
        self.name = name

    def json(self):
        return {'name':self.name}
        

@app.route('/login',methods =['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')


    user = authenticate(username,password)
    if user:
        accses_token = create_access_token(identity=user.id)
        return jsonify(accses_token=accses_token)
    return jsonify({'message':'Invalid credentials'}),401

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

class PuppyNames(Resource):
    
    def get(self, name):
        
        pup = Puppy.query.filter_by(name = name).first()
        
        if pup:
            return pup.json()
        else:
            return {'name': None}, 404
    
    def post(self, name):
        
        pup = Puppy(name=name)
        db.session.add(pup)
        db.session.commit()

        return pup.json()
    
    def delete(self, name):
        
        pup = Puppy.query.filter_by(name=name).first()
        db.session.delete(pup)
        db.session.commit()
        return {'note': 'delete success'}
            
     
class AllNames(Resource):

    # @jwt_required()
    def get(self):
        puppies = Puppy.query.all()

        return [pup.json() for pup in puppies]
    

api.add_resource(PuppyNames,'/puppy/<string:name>')

api.add_resource(AllNames, '/puppies')


if __name__ == '__main__':
    app.run(debug=True)