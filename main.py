# import flast module
from flask import Flask
from functools import wraps
from flask import request
from flask import make_response
from flask import jsonify


app = Flask(__name__)

# Authentication decorator
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        # ensure the jwt-token is passed with the headers
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token: # throw error if no token provided
            return make_response(jsonify({"message": "A valid token is missing!"}), 401)
        if(token == "123456"):
            return f(*args, **kwargs)
        else:
            return make_response(jsonify({"message": "Invalid token!"}), 401)
         # Return the user information attached to the token        
    return decorator


@app.route("/")
@token_required
def hello_world():
    return "Hello, World!"


if __name__ == '__main__':  
    app.run(debug=True) 
