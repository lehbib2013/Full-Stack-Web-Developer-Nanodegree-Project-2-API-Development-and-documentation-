import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
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

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_categories(self):

        res = self.client().get("/categories")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["categories"])
        self.assertTrue(data["totalCategories"])

    def test_405_get_categories(self):
        res = self.client().post("/categories",json={"type":"1"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Method not allowed")

    def test_200_get_questions(self):

        res = self.client().get("/questions?page=1")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertTrue(data["totalQuestions"])
        self.assertTrue(data["categories"])
        self.assertTrue(data["currentCategory"])
       
    def test_404_get_questions(self):
        res = self.client().get("/questions?page=10000")
        data = json.loads(res.data)

        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"],404)
        self.assertEqual(data["message"],'resource not found')
       

    def test_200_delete_question(self):


        res = self.client().delete("/questions/25")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["deleted"])
        self.assertTrue(data["questions"])
        self.assertTrue(data["totalQuestions"])


    def test_422_delete_non_existing_question(self):


        res = self.client().delete("/questions/100000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"],404)
        self.assertEqual(data["message"],'resource not found')
         

    def test_200_create_new_question(self):


        res = self.client().post("/questions",json={'question':'Question pour test 1','answer':'answer pour Question 1','category':'2','diffuculty':'20'})
        data = json.loads(res.data)
         
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["created"])
        self.assertTrue(data["questions"]) 
        self.assertTrue(data["totalQuestions"]) 
        

    def test_405_not_allowed_creating_question(self):

        res = self.client().get("/questions/1",json={'ii':'0'})
        data = json.loads(res.data)
         
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
         
        self.assertTrue(data["error"],405) 
        self.assertTrue(data["message"],'Method not allowed') 
          


    def test_200_paginated_search_question(self):
        res = self.client().post("/questions",json={'searchTerm':'a'})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
         
        self.assertTrue(data["questions"]) 
        self.assertTrue(data["totalQuestions"]) 
        self.assertTrue(data["currentCategory"])

    def test_404_search_ques_with_empty_results(self):
        res = self.client().post("/questions",json={'searchTerm':'xxx'})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"],404)
        self.assertEqual(data["message"],'resource not found')
        
     

    def test_200_questions_by_category(self):

        res = self.client().get("/categories/1/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertTrue(data["totalQuestions"])
        self.assertTrue(data["currentCategory"])

    def test_404_empty_result_questions_by_category(self):

        res = self.client().get("/categories/1500/questions")
        data = json.loads(res.data)
         
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"],404)
        self.assertEqual(data["message"],'resource not found') 
    
     
    def test_200_quizz(self):
        res = self.client().post("/quizzes", json={"previous_questions":["23","2"], "quiz_category": {"type": "History", "id": 2}})
        data = json.loads(res.data)
         
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["question"]) 
    
    def test_405_quizz(self):
        res = self.client().get("/quizzes",json={'previous_questionss': [12, 5, 9], 'quiz_categoryy': {"type": "History", "id": 2}})
        data = json.loads(res.data)
         
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"],False) 
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Method not allowed")
         

     
     
     


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()