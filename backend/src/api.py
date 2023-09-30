import os
from flask import Flask, request, jsonify, abort, redirect, url_for, session
from sqlalchemy import exc
import json
from flask_cors import CORS
from datetime import datetime

from .database.models import db_drop_and_create_all, setup_db, Actor, Movie
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
with app.app_context():
    setup_db(app)
    CORS(app)


    '''
    @TODO uncomment the following line to initialize the datbase
    !! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
    !! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
    !! Running this funciton will add one
    '''
    db_drop_and_create_all()

# ROUTES
'''
@TODO implement endpoint
    GET /actors
        it should require the 'get:actors-detail' permission
        it should be a public endpoint
        it should contain only the actor.short() data representation
    returns status code 200 and json {"success": True, "actors": actors} where actors is the list of actors
        or appropriate status code indicating reason for failure
'''
@app.route('/')
def index():
    return "Welcome to Capstone !"

@app.route('/login')
def login():
    url = "https://dev-4yewlodtqwpxz0xf.us.auth0.com/authorize?audience=capstone&response_type=token&client_id=8uN9Sn2mv9tzwzbg1VdStZ8PfO1pUtbj&redirect_uri=https://casting-agency-service-tuanpm22.onrender.com/"
    return redirect(url)

@app.route('/logout')
def logout():
    url = "https://dev-4yewlodtqwpxz0xf.us.auth0.com/oidc/logout?post_logout_redirect_uri=https://casting-agency-service-tuanpm22.onrender.com/"
    return redirect(url)

@app.route('/actors')
@requires_auth('get:actors-detail')
def get_actor():
    list_actors = Actor.query.all()

    if len(list_actors) == 0:
        abort(404)
    return {
        "success": True,
        "actors":  [actor.format() for actor in list_actors]
    }

'''
@TODO implement endpoint
    GET /movies
        it should require the 'get:movies-detail' permission
        it should be a public endpoint
        it should contain only the movie.short() data representation
    returns status code 200 and json {"success": True, "movies": movies} where movies is the list of movies
        or appropriate status code indicating reason for failure
'''
@app.route('/movies')
@requires_auth('get:movies-detail')
def get_movie():
    list_movies = Movie.query.all()

    if len(list_movies) == 0:
        abort(404)
    return {
        "success": True,
        "movies":  [movie.format() for movie in list_movies]
    }

'''
@TODO implement endpoint
    DELETE /actors
        it should require the 'delete:actors' permission
    returns status code 200 and json {"success": True, "id": id} where id is the id of deleted actor
        or appropriate status code indicating reason for failure
'''
@app.route('/actors/<int:id>', methods =['DELETE'])
@requires_auth('delete:actors')
def actor_delete(id):
    actor = Actor.query.filter(Actor.id == id ).first()

    if not actor:
        abort(404)

    try:
        actor.delete()
        return {
        "success": True,
        "id": id
    }
    except:
        abort(422)

'''
@TODO implement endpoint
    DELETE /movies
        it should require the 'delete:movies' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "id": id} where id is the id of deleted movies
        or appropriate status code indicating reason for failure
'''
@app.route('/movies/<int:id>', methods =['DELETE'])
@requires_auth('delete:movies')
def movie_delete(id):
    movie = Movie.query.filter(Movie.id == id ).first()

    if not movie:
        abort(404)

    try:
        movie.delete()
        return {
        "success": True,
        "id": id
    }
    except:
        abort(422)

'''
@TODO implement endpoint
    POST /movies
        it should create a new row in the movies table
        it should require the 'post:movies' permission
        it should contain the movie.long() data representation
    returns status code 200 and json {"success": True, "movie": movie} where movie an array containing only the newly created movie
        or appropriate status code indicating reason for failure
'''
@app.route('/movies', methods =['POST'])
@requires_auth('post:movies')
def create_movies():
    body = request.get_json()

    
    title = body['title']
    release_date = datetime.strptime(body['release_date'], "%Y-%m-%d")

    movie = Movie(title, release_date)

    try:
        movie.insert()
        return {
        "success": True,
        "movies": movie.format()
    }
        
    except:
        abort(422)


'''
@TODO implement endpoint
    POST /actors
        it should create a new row in the movies table
        it should require the 'post:movies' permission
        it should contain the actor data representation
    returns status code 200 and json {"success": True, "actor": actor} where actor an array containing only the newly created movie
        or appropriate status code indicating reason for failure
'''
@app.route('/actors', methods =['POST'])
@requires_auth('post:actors')
def create_actors():
    body = request.get_json()

    name = body['name']
    age = body['age']
    gender = body['gender']

    actor = Actor(name, age, gender)

    try:
        actor.insert()
        return {
        "success": True,
        "actors": actor.format()
    }
        
    except:
        abort(422)


'''
@TODO implement endpoint
    PATCH /actors/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:actors' permission
        it should contain the actor data representation
    returns status code 200 and json {"success": True, "actors": actor} where drink an array containing only the updated actor
        or appropriate status code indicating reason for failure
'''
@app.route('/actors/<int:id>', methods =['PATCH'])
@requires_auth('patch:actors')
def patch_actors(id):
    actor = Actor.query.filter(Actor.id == id).first()

    if not actor:
        abort(404)

    body = request.get_json()
    name = body['name']
    age = body['age']
    gender = body['gender']

    if name:
        actor.name = name
    
    if age:
        actor.age = age

    if gender:
        actor.gender = gender
    try:
        actor.update()
        return {
            "success": True,
            "actor": actor.format()
        }
    except:
        abort(422)
    

'''
@TODO implement endpoint
    PATCH /movies/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:actors' permission
        it should contain the actor data representation
    returns status code 200 and json {"success": True, "actors": actor} where drink an array containing only the updated actor
        or appropriate status code indicating reason for failure
'''
@app.route('/movies/<int:id>', methods =['PATCH'])
@requires_auth('patch:movies')
def patch_movies(id):
    movie = Movie.query.filter(Movie.id == id).first()

    if not movie:
        abort(404)

    body = request.get_json()

    title = body['title']
    release_date = datetime.strptime(body['release_date'], "%Y-%m-%d")

    if title:
        movie.title = title
    
    if release_date:
        movie.release_date = release_date
    try:
        movie.update()
        return {
            "success": True,
            "movie": movie.format()
        }
    except:
        abort(422)
    


# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''
@app.errorhandler(404)
def not_found(error):
    return (
            jsonify({"success": False, "error": 404, "message": "resource not found"}),
            404,
    )

'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''
@app.errorhandler(AuthError)
def auth_error(error):
    return (
            jsonify({"success": False, "error": AuthError, "message": "AuthError"}),
            404,
    )