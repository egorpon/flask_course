from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from secure_check import authenticate 



app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


api = Api(app)
jwt = JWTManager(app)


puppies = []


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
        
        for pup in puppies:
            if pup['name'] == name:
                return pup
            
        return {'name': None}, 404
    
    def post(self, name):
        
        pup = {'name':name}
        puppies.append(pup)

        return pup
    
    def delete(self, name):
        
        for index, pup in enumerate(puppies):
            if pup['name'] == name:
                deleted_pup = puppies.pop(index)
                return {'note': 'delete success'}
            
     
class AllNames(Resource):
    @jwt_required()
    def get(self):
        return {'puppies':puppies}
    

api.add_resource(PuppyNames,'/puppy/<string:name>')

api.add_resource(AllNames, '/puppies')


if __name__ == '__main__':
    app.run(debug=True)