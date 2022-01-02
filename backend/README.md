**Udacity QUIZZ PROJECT**

This project is my  second project in Full Stack Developer Nanodegree and it comes to build a bonding experience for employees and studens Of Udacity, this project will build out a provided  Trivia App API to make all web frontend pages functional.

I used and inspired from a   provided examples coding from instructor's videos course.
For this project we use virtual environement venv to manage separatly all dependencies needed by project 

# create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate


# Getting Started

# Pererequisites  & Installations
Python3 ,pip3 and node are required for a developper to use  current API.

to install all needed moduls including Flask ,SQLAlchemy ,Flask-Cors and softwares :
   pip3 install requirements.txt

with postgres running lunch:
psql trivia < trivia.psql
after moving to [starter] directory , run the backend as following:

# For Mac/Linux
```
export FLASK_APP=backend/flaskr
export FLASK_ENV=development
```
# Make sure to run this command from the project directory (not from the flaskr)
```
flask run
```


# Tests
For Tests, you need to lunch following command to prepare test environement.
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py

```

All API Endpoints where tested by TDD Approach.

# API References

**Getting started**

This app can be hosted only locally at following base url : (http://127.0.0.1:5000/) and it communicates with frontend part(given by Udacity as ready implemented part).

**Errors handling**

the errors are returned in the following [json formats] :
```
{
  "error": 422, 
  "message": "Unprocessoble error", 
  "success": true
}
The API can return following error codes:
404 : if resource wasn't found
422 : if error is not processable 
400 : if the request is bad
405 : if the method is not allowed
```

**Endpoints**
 
 # GET /categories
retuns a ist of categories 
```
sample:  curl http://127.0.0.1:5000/categories

    {
     "categories":{ "1":"Science",
         "2":"Art",
         "3":"Geography",
         "4":"History",
         "5":"Entertainment",
         "6":"Sports" },
     "success":true,
     "totalCategories":6
    }
```

# GET /questions
return paginated questions 

```
sample:  curl 'http://127.0.0.1:5000/questions?page=1'

                {
                "categories": [
                    {
                    "id": 1, 
                    "type": "Science"
                    }, 
                    {
                    "id": 2, 
                    "type": "Art"
                    }, 
                    {
                    "id": 3, 
                    "type": "Geography"
                    }, 
                    {
                    "id": 4, 
                    "type": "History"
                    }, 
                    {
                    "id": 5, 
                    "type": "Entertainment"
                    }, 
                    {
                    "id": 6, 
                    "type": "Sports"
                    }
                ], 
                "currentCategory": "Science", 
                "questions": [
                    {
                    "answer": "Apollo 13", 
                    "category": 5, 
                    "difficulty": 4, 
                    "id": 2, 
                    "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
                    }, 
                    {
                    "answer": "Tom Cruise", 
                    "category": 5, 
                    "difficulty": 4, 
                    "id": 4, 
                    "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
                    }, 
                    {
                    "answer": "Maya Angelou", 
                    "category": 4, 
                    "difficulty": 2, 
                    "id": 5, 
                    "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
                    }, 
                    {
                    "answer": "Edward Scissorhands", 
                    "category": 5, 
                    "difficulty": 3, 
                    "id": 6, 
                    "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
                    }, 
                    {
                    "answer": "Muhammad Ali", 
                    "category": 4, 
                    "difficulty": 1, 
                    "id": 9, 
                    "question": "What boxer's original name is Cassius Clay?"
                    }, 
                    {
                    "answer": "Brazil", 
                    "category": 6, 
                    "difficulty": 3, 
                    "id": 10, 
                    "question": "Which is the only team to play in every soccer World Cup tournament?"
                    }, 
                    {
                    "answer": "Uruguay", 
                    "category": 6, 
                    "difficulty": 4, 
                    "id": 11, 
                    "question": "Which country won the first ever soccer World Cup in 1930?"
                    }, 
                    {
                    "answer": "George Washington Carver", 
                    "category": 4, 
                    "difficulty": 2, 
                    "id": 12, 
                    "question": "Who invented Peanut Butter?"
                    }, 
                    {
                    "answer": "Lake Victoria", 
                    "category": 3, 
                    "difficulty": 2, 
                    "id": 13, 
                    "question": "What is the largest lake in Africa?"
                    }, 
                    {
                    "answer": "The Palace of Versailles", 
                    "category": 3, 
                    "difficulty": 3, 
                    "id": 14, 
                    "question": "In which royal palace would you find the Hall of Mirrors?"
                    }
                ], 
                "success": true, 
                "totalQuestions": 19
                }
```

# DELETE /questions/<int:question_id>
delete a question by providing it ID .
```
sample :  curl -X DELETE http://127.0.0.1:5000/questions/17 

            {
            "deleted": 17, 
            "questions": [
                {
                "answer": "Apollo 13", 
                "category": 5, 
                "difficulty": 4, 
                "id": 2, 
                "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
                }, 
                {
                "answer": "Tom Cruise", 
                "category": 5, 
                "difficulty": 4, 
                "id": 4, 
                "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
                }, 
                {
                "answer": "Maya Angelou", 
                "category": 4, 
                "difficulty": 2, 
                "id": 5, 
                "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
                }, 
                {
                "answer": "Edward Scissorhands", 
                "category": 5, 
                "difficulty": 3, 
                "id": 6, 
                "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
                }, 
                {
                "answer": "Muhammad Ali", 
                "category": 4, 
                "difficulty": 1, 
                "id": 9, 
                "question": "What boxer's original name is Cassius Clay?"
                }, 
                {
                "answer": "Brazil", 
                "category": 6, 
                "difficulty": 3, 
                "id": 10, 
                "question": "Which is the only team to play in every soccer World Cup tournament?"
                }, 
                {
                "answer": "Uruguay", 
                "category": 6, 
                "difficulty": 4, 
                "id": 11, 
                "question": "Which country won the first ever soccer World Cup in 1930?"
                }, 
                {
                "answer": "George Washington Carver", 
                "category": 4, 
                "difficulty": 2, 
                "id": 12, 
                "question": "Who invented Peanut Butter?"
                }, 
                {
                "answer": "Lake Victoria", 
                "category": 3, 
                "difficulty": 2, 
                "id": 13, 
                "question": "What is the largest lake in Africa?"
                }, 
                {
                "answer": "One", 
                "category": 2, 
                "difficulty": 4, 
                "id": 18, 
                "question": "How many paintings did Van Gogh sell in his lifetime?"
                }
            ], 
            "success": true, 
            "totalQuestions": 15
           }
```

# POST /questions
this end point combine two functionalties with different returned json responses:
   1. **adds a question into database** .
   ```
   sample : curl -X POST -H "Content-Type: application/json" -d '{"question":"ou est aTAR ","answer":"a ADRAR","category":"2","difficulty":"3"}' http://127.0.0.1:5000/questions

            {
            "created": 26, 
            "questions": [
                {
                "answer": "Apollo 13", 
                "category": 5, 
                "difficulty": 4, 
                "id": 2, 
                "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
                }, 
                {
                "answer": "Tom Cruise", 
                "category": 5, 
                "difficulty": 4, 
                "id": 4, 
                "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
                }, 
                {
                "answer": "Maya Angelou", 
                "category": 4, 
                "difficulty": 2, 
                "id": 5, 
                "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
                }, 
                {
                "answer": "Edward Scissorhands", 
                "category": 5, 
                "difficulty": 3, 
                "id": 6, 
                "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
                }, 
                {
                "answer": "Muhammad Ali", 
                "category": 4, 
                "difficulty": 1, 
                "id": 9, 
                "question": "What boxer's original name is Cassius Clay?"
                }, 
                {
                "answer": "Brazil", 
                "category": 6, 
                "difficulty": 3, 
                "id": 10, 
                "question": "Which is the only team to play in every soccer World Cup tournament?"
                }, 
                {
                "answer": "Uruguay", 
                "category": 6, 
                "difficulty": 4, 
                "id": 11, 
                "question": "Which country won the first ever soccer World Cup in 1930?"
                }, 
                {
                "answer": "George Washington Carver", 
                "category": 4, 
                "difficulty": 2, 
                "id": 12, 
                "question": "Who invented Peanut Butter?"
                }, 
                {
                "answer": "Lake Victoria", 
                "category": 3, 
                "difficulty": 2, 
                "id": 13, 
                "question": "What is the largest lake in Africa?"
                }, 
                {
                "answer": "One", 
                "category": 2, 
                "difficulty": 4, 
                "id": 18, 
                "question": "How many paintings did Van Gogh sell in his lifetime?"
                }
            ], 
            "success": true, 
            "totalQuestions": 18
            }
    ```
    
   2.**get all questions including search term (case insensitive)**:
   ```
   sample : 
    curl -X POST -H "Content-Type: application/json" -d '{"search_term":"africa"}' http://127.0.0.1:5000/questions

     
                {

                "currentCategory": {

                    "id": 1, 

                    "type": "Science"

                }, 

                "questions": [

                    {

                    "answer": "Lake Victoria", 

                    "category": 3, 

                    "difficulty": 2, 

                    "id": 13, 

                    "question": "What is the largest lake in Africa?"

                    }

                ], 

                "success": true, 

                "totalQuestions": 1

                }
    ```


 
# GET /categories/<int:id_category>/questions
returns questions of given category
```
sample : curl -X GET http://127.0.0.1:5000/categories/3/questions


        {

        "currentCategory": {

            "id": 3, 

            "type": "Geography"

        }, 

        "questions": [

            {

            "answer": "Lake Victoria", 

            "category": 3, 

            "difficulty": 2, 

            "id": 13, 

            "question": "What is the largest lake in Africa?"

            }

        ], 

        "success": true, 

        "totalQuestions": 1

        }
```


      
# POST /quizzes
get questions to play the quiz. It takes category and previous question parameters 
and return a random questions within the given category, if provided, and that is not one of the previous questions.
```
sample : curl -X POST 'localhost:5000/quizzes' --data '{"previous_questions": [12, 5, 9], "quiz_category": {"type": "History", "id": 2}}' --header "Content-Type: application/json"

    {
    "question":  {
    "answer":"a ADRAR",
    "category":2,
    "difficulty":3,
    "id":25,
    "question":"ou est aTAR "
                  }
    }

```

# Authors

Mohamed Lehbib Ould Youba

# Acknowledgments

All thanks to Udacity's instructors of this course as well as for technical mentors for helping me during the work on this project.