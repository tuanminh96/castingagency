import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = "postgresql://postgres_deployment_example_nl7f_user:HdPIbUUAuJR6vRv3VNPjExxRpFBgCve9@dpg-ck6h72g8elhc73dr5qlg-a.oregon-postgres.render.com/postgres_deployment_example_nl7f"
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    #Test fail cases

    def test_get_actors_notfound(self):
        res = self.client().get("/movies")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_get_movies_notfound(self):
        res = self.client().get("/movies")

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_delete_actors_notfound(self):
        res = self.client().delete("/actors/1")

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_delete_moviess_notfound(self):
        res = self.client().delete("/movies/1")

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_patch_actors_notfound(self):
        res = self.client().patch("/actors/1")

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_patch_movies_notfound(self):
        res = self.client().patch("/movies/1")

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_405_if_actor_creation_not_allowed(self):
        res = self.client().get("/actors", json=self.actors)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")

    def test_405_if_movies_creation_not_allowed(self):
        res = self.client().get("/movies", json=self.movies)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")

    # Test successfull case
    def test_create_actors(self):
        res = self.client().post("/actors", json=self.actors)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_create_movies(self):
        res = self.client().post("/movies", json=self.movies)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_get_actors(self):
        res = self.client().get("/actors")
        data = json.loads(res.data)

        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_get_movies(self):
        res = self.client().get("/movies")
        data = json.loads(res.data)

        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])

    def test_delete_actors(self):
        res = self.client().delete("/actors/1")
        data = json.loads(res.data)

        self.assertEqual(data["success"], True)
        self.assertEqual(data["id"], 1)

    def test_delete_movies(self):
        res = self.client().delete("/movies")
        data = json.loads(res.data)

        self.assertEqual(data["success"], True)
        self.assertEqual(data["id"], 1)

    def test_create_actors(self):
        res = self.client().post("/actors", json=self.actors)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_create_movies(self):
        res = self.client().post("/movies", json=self.movies)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()