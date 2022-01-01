import os
import sys
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from sqlalchemy import or_

from models import setup_db, Question, Category, RequestError

# general project structure with empty TODOs was given by Udacity as initial starter code
# the major parts of endpoint implementations are inspired from instructions video course(including how pagination is implemented),
#  a personalized implemention in quizz endpoint
QUESTIONS_PER_PAGE = 10

def paginate_questions(request,selection):
        current_page = request.args.get('page',1,type=int)
        start = (current_page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE
        questions = [quest.format() for quest in selection]
        current_questions = questions[start:end]
        return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  
  CORS(app, resources={r"/*": {"origins": "*"}})
 
  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization,true")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,PATCH,POST,DELETE,OPTIONS")
    return response
  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route("/categories")
  def get_all_categories():
    try:
      categories = Category.query.all()
      list_categories = {categ.id : categ.type  for categ in categories}
      if len(categories) == 0:
            abort(404)
      return jsonify({
            'success':True,
            'categories': list_categories,
            'totalCategories':len(categories)
        })
    except:
      #print(sys.exc_info())
      abort(422)

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions') 
  def get_all_questions():
    ret_category = request.args.get('current_category','1',type=int)
    #current_page = request.args.get('page',1,type=int)
    #print(current_page )
    questions = Question.query.order_by(Question.id).all()
    current_questions = paginate_questions(request,questions)
    if len(current_questions) == 0:
      abort(404)
    categories = Category.query.all()
    current_category = Category.query.get(ret_category)
    list_categories = {categ.id : categ.type  for categ in categories}
    
    return jsonify({
            'success':True,
            'questions':current_questions,
            'totalQuestions':len(questions),
            'currentCategory':current_category.type,
            'categories':list_categories
        })
    
   
  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route("/questions/<int:question_id>", methods=["DELETE"])
  def delete_question(question_id):
    try:
      current_question = Question.query.filter(Question.id == question_id).one_or_none()
      #print("current_question")
      #print(current_question)
      if current_question is None:
        raise RequestError(404)
      current_question.delete()
      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)
      list_of_questions = Question.query.order_by(Question.id).all()
      return jsonify(
                    {
                    "success": True,
                    "deleted": question_id,
                    "questions": current_questions,
                    "totalQuestions": len(list_of_questions),
                     }
                     )
    except RequestError as error:
      abort(error.status)

    except:
      #print(sys.exc_info()) 
      abort(422)
    
    
         
        
  
      
   
  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  # this endpoint will treated with search endpoint in the same entry


  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route("/questions",methods=['POST'])
  def quetions_post_request():
    body = request.get_json()
    #print("body")
    #print(body)

    
    
    try:
      
      search_term = body.get('searchTerm',None)
      current_categ = body.get('current_category',1)
      new_question_text = body.get('question',None)
      new_answer_text = body.get('answer',None)
      new_category = body.get('category',None)
      new_difficulty = body.get('difficulty',None)
     


      if search_term is not None :

        #print("searchTerm")
        #print(search_term)
        questions_result = Question.query.filter(Question.question.ilike(f'%{search_term}%')).all()
      
        list_questions =[quest.format() for quest in questions_result]
      
        current_category = Category.query.filter(Category.id == current_categ).one_or_none()

        if len(list_questions) == 0 :
          raise RequestError(404)

      
        return jsonify({
                    'success':True,
                    'questions':list_questions,
                    'totalQuestions':len(list_questions),
                    'currentCategory': current_category.format(),
                    
                })
      else:
        if (new_question_text is not None) and (new_answer_text is not None) :

          try:
            to_be_added = Question(question=new_question_text, answer=new_answer_text, category=new_category, difficulty=new_difficulty)
            to_be_added.insert()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request,selection)
            return jsonify({
                        'success':True,
                        'created':to_be_added.id,
                        'questions':current_questions,
                        'totalQuestions':len(Question.query.all())
                    })
           

          except RequestError as error:
            #print(sys.exc_info())
            abort(error.status)
          except:
            abort(422)
        

        

       


    
    except RequestError as error:
      #print(sys.exc_info()) 
      abort(error.status)
    except:
       print(sys.exc_info()) 
       abort(422)



     

    
    
    



  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route("/categories/<int:id_category>/questions")
  def filter_quetions_by_category(id_category):
      try:
        current_page = request.args.get('page',1,type=int)
        start = (current_page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE
        questions = Question.query.filter(Question.category == id_category).order_by(Question.id).all()
        #print("'questions'")
        # print(len(questions))
        if len(questions) == 0:
         raise RequestError(404)

        list_questions =[quest.format() for quest in questions]
        categories = Category.query.order_by(Category.id).all()
        current_category= Category.query.filter(Category.id == id_category).one_or_none()
        #print("'current_category'")
        #print(current_category.format())
        if current_category is None :
         raise RequestError(404)
        
        return jsonify({
              'success':True,
              'questions':list_questions[start:end],
              'totalQuestions':len(list_questions),
              'currentCategory':current_category.format()
          })

      except RequestError as error:
        abort(error.status)

      except:
       #print(sys.exc_info()) 
       abort(422)

  

  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route("/quizzes", methods=['POST'])
  def get_quizz_question():
    body = request.get_json()

    try:

      
      previous_questions = body.get('previous_questions',None)
      #print("previous_questions")
      #print(previous_questions)
      
      quiz_category = body.get('quiz_category',None)
      print("quiz_category")
      print(quiz_category)
      #print(quiz_category['id'])
      # as detected : frontend sends {'type': 'click', 'id': 0} object when "all categories" button is selected so we use this to test
      questions_to_select_from =  Question.query.filter(Question.id.notin_((previous_questions))).order_by('id').filter(or_(Question.category == quiz_category['id'],  0 == quiz_category['id'])).all()
      
      
      if len(questions_to_select_from) == 0:

        return jsonify({'questions': None })
      else:
        #print("[r.id for r in questions_to_select_from]")
        
        list_ids = []
        #print([list_ids.append(r.id) for r in questions_to_select_from])
        [list_ids.append(r.id) for r in questions_to_select_from]
        random_returned_id = random.choice(list_ids)
        #previous_questions.add(random_returned_id)

        return jsonify({'question': Question.query.filter(Question.id == random_returned_id).one_or_none().format() })
        
         
    except RequestError as error:
      print(sys.exc_info())
      abort(error.status)

    except:
      print(sys.exc_info())
      abort(422)

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found_hand(error):
      return jsonify({
        "success": False, 
        "error": 404, 
        "message": "resource not found"
      }),404
       

  @app.errorhandler(422)
  def unprocessoblle_handler(error):
    return jsonify({
      "success":True,
      "error":422,
      "message":"Unprocessable error"
    }), 422

  @app.errorhandler(400)
  def bad_request400_handler(error):
    return jsonify({
      'success':True,
      'error':400,
      'message':'Bad request'
    }), 400

  @app.errorhandler(405)
  def bad_request405_handler(error):
    return jsonify({
      'success':False,
      'error':405,
      'message':'Method not allowed'
    }), 405

  return app

    