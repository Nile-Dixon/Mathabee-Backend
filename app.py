#FLASK LIBRARIES
from flask import Flask, request, Response, render_template, jsonify
from flask_cors import CORS

#CUSTOM FILES
from mathabee import create_question
from models import db, Hosts, GameTypes, Games, Questions, Players
from functions import generate_random_string, generate_short_code

#STANDARD LIBRARIES
import os
from datetime import datetime

#OTHER THIRD PARTY LIBRARIES
from dotenv import load_dotenv

load_dotenv(verbose = True)

app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/', methods = ['GET'])
def index_route():
	return "Hi."

@app.route('/game/<game_id>', methods = ['GET'])
def get_game_route(game_id):
	current_game = Games.query.filter_by(id = game_id).first()
	if current_game == None:
		return jsonify({
				'status' : 'error',
				'message' : 'Game information not found.'
			})
	return jsonify({
			'status' : 'success',
			'data' : current_game.json()
		})

@app.route('/game', methods = ['POST'])
def create_game_route():
	content = request.json
	game_types = [
		'basic_addition',
		'advanced_addition',
		'basic_subtraction' ,
		'advanced_subtraction',
		'basic_multiplication',
		'advanced_multiplication', 
		'basic_division',
		'advanced_division',
		'basic_mixed',
		'advanced_mixed', 
		'add_fractions',
		'subtract_fractions',
		'multiply_fractions',
		'divide_fractions',
		'simplify_fractions', 
		'angles',
		'perimeter', 
		'area',
		'pythagorean',
		'average',
		'median',
		'range',
		'dollars_and_cents',
		'exponents_and_powers',
		'square_roots'
	]

	if content['game_type'] not in game_types:
		return jsonify({
				'status' : 'error',
				'message' : 'Invalid game type.'
			})
	number_of_questions = int(content['number_of_questions'])

	#MAKE TEMPORARY UNIQUE JOIN CODE
	found_join_code = False
	join_code = ""
	while found_join_code == False:
		join_code = generate_short_code()
		query = Games.query.filter_by(live_game = 1).filter_by(join_code = join_code).first()
		if query == None:
			found_join_code = True

	#CREATE GAME HERE
	game_id = generate_random_string(10,20)
	new_game = Games(
		game_id,
		"public",
		content['game_type'],
		number_of_questions,
		1,
		join_code
	)
	db.session.add(new_game)

	#CREATE QUESTIONS
	for x in range(number_of_questions):
		question_data = create_question(content['game_type'])
		new_question = Questions(
			generate_random_string(10,200),
			game_id,
			x + 1,
			question_data['question_text'],
			question_data['answer']
		)
		db.session.add(new_question)

	db.session.commit()

	return jsonify({
			'status' : 'success',
			'game_id' : game_id
		})


@app.route('/player', methods = ['POST'])
def create_user_route():
	content = request.json

	current_game = Games.query.filter_by(live_game = 1).filter_by(join_code = content['join_code']).first()
	if current_game == None:
		return jsonify({
				'status' : 'error',
				'message' : 'Game code does not exist.'
			})

	current_user = Players.query.filter_by(game_id = current_game.id).filter_by(nickname = content['nickname']).first()
	if current_user != None:
		return jsonify({
				'status' : 'error',
				'message' : 'Player currently using that nickname. Please pick a different nickname.'
			})

	player_id = generate_random_string(10,30)
	new_player = Players(player_id, content['nickname'], current_game.id)
	db.session.add(new_player)
	db.session.commit()

	return jsonify({
			'status' : 'success',
			'id' : player_id,
			'game_id' : current_game.id
		})

@app.route('/player', methods = ['GET'])
def get_user_route():
	current_player = Players.query.filter_by(id = request.headers['X-User-Header']).first()
	if current_player == None:
		return jsonify({
				'status' : 'error',
				'message' : 'Player does not exist.'
			})
	return jsonify({
			'id' : current_player.id,
			'game_id' : current_player.game_id
		})

@app.route('/get-question', methods = ['POST'])
def get_question_route():
	content = request.json

	current_user = Players.query.filter_by(id = content['player_id']).first()
	if current_user == None:
		return jsonify({
				'status' : 'error',
				'message' : 'Player does not exist.'
			})

	current_game = Games.query.filter_by(id = current_user.game_id).filter_by(live_game = 1).first()
	if current_game == None:
		return jsonify({
				'status' : 'error',
				'message' : 'Game does not exist.'
			})

	current_question = Questions.query.filter_by(game_id = current_user.game_id).filter_by(number = current_user.question_number).first()
	if current_question == None:
		current_user.end_time = datetime.utcnow()
		db.session.commit()
		current_players = Players.query.filter_by(game_id = current_user.game_id).order_by(
			Players.end_time,
			Players.question_number.desc()
		).all()
		winner_message = "Congratulations, you finished number {}."
		place = len(winner_message)
		for x in range(len(current_players)):
			place = x + 1
			if current_players[x].id == current_user.id:
				break
		winner_message = winner_message.format(place)
		return jsonify({
				'status' : 'warning',
				'message' : 'No questions left.',
				'completion_message' : winner_message
			})

	return jsonify({
			'question' : current_question.json()
		})

@app.route('/check-answer', methods = ['POST'])
def check_answer_route():
	content = request.json
	
	current_user = Players.query.filter_by(id = content['player_id']).first()
	if current_user == None:
		return jsonify({
				'status' : 'error',
				'message' : 'Player does not exist.'
			})

	current_game = Games.query.filter_by(id = current_user.game_id).filter_by(live_game = 1).first()
	if current_game == None:
		return jsonify({
				'status' : 'error',
				'message' : 'Game does not exist.'
			})

	current_question = Questions.query.filter_by(game_id = current_user.game_id).filter_by(number = current_user.question_number).first()
	if current_question == None:
		return jsonify({
				'status' : 'warning',
				'message' : 'No questions left.'
			})

	user_answer = float(content['player_answer'])
	if user_answer == current_question.answer:
		current_user.question_number += 1
		db.session.commit()

		return jsonify({
				'status' : 'success',
				'message' : 'Correct answer'
			})
	return jsonify({
			'status' : 'warning',
			'message' : 'Incorrect answer'
		})


if __name__ == "__main__":
	app.run(debug = True, use_reloader = True)