# Casting Agency Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Role Casting Assistant:
   - Permission:
      - `get:actors-detail`
      - `get:movies-detail`
   - Account: trung@gmail.com/Abcde12345@

2. Role Casting Director:
   - Permission:
      - `delete:actors`
      - `get:actors-detail`
      - `get:movies-detail`
      - `patch:actors`
      - `patch:movies`
      - `post:actors`
   - Account: nganld@gmail.com/Abcde12345@

3. Role Executive Producer:
   - Permission:
      - `delete:actors`
      - `get:actors-detail`
      - `get:movies-detail`
      - `patch:actors`
      - `patch:movies`
      - `post:actors`
      - `post:movies`
      - `delete:movies`
   - Account: trung@gmail.com/Abcde12345@
4. Role - API mapping
   - Role Casting Assistant: GET /actors, GET /movies
   - Role Casting Director: All role of Casting Assisstant & DELETE /actors, POST /actors, PATCH /actors, PATCH /movies
   - Role Executive Producer: All roles and can access to all API

4. Login to application and get JWT token for each role
   - Go to: https://casting-agency-service-tuanpm22.onrender.com/login
   - Type in account password for each role
   - After login successfully, copy the access_token from the url, this will be the JWT token to use to test the endpoint on Postman

7. Test your endpoints with [Postman](https://getpostman.com).
   - Open postman, paste the Bearer token Authentication is the JWT token copy from above
   - Test with each endpoints:
   - GET /actors: https://casting-agency-service-tuanpm22.onrender.com/actors
   - GET /movies: https://casting-agency-service-tuanpm22.onrender.com/movies
   - DELETE /actors: https://casting-agency-service-tuanpm22.onrender.com/actors/1
   - DELETE /movies: https://casting-agency-service-tuanpm22.onrender.com/movies/1
   - POST /actors: https://casting-agency-service-tuanpm22.onrender.com/actors 
      - Body {"age": 34,"gender": "Male","name": "Ngan"}
   
   ### Release date format %yyyy_mm_dd&
   - POST /movies: https://casting-agency-service-tuanpm22.onrender.com/movies 
      - Body {"title": "Gon with the wind","release_date": "2023-07-09"}

   - PATCH /actors: https://casting-agency-service-tuanpm22.onrender.com/actors/1
      - Body {"age": 26,"gender": "Male","name": "Minh Tuan"}
   - PATCH /movies: https://casting-agency-service-tuanpm22.onrender.com/movies /1
      - Body {"title": "Avenger: End game","release_date": "2025-07-09"}

### Implement The Server
- Application was deployed to Render
- Live endpoint: https://casting-agency-service-tuanpm22.onrender.com/
