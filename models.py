from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

db = SQLAlchemy()

class Hosts(db.Model):
	id = db.Column(db.String(255), primary_key = True)
	first_name = db.Column(db.String(100))
	last_name = db.Column(db.String(100))
	email = db.Column(db.String(500))
	password = db.Column(db.String(500))
	salt = db.Column(db.String(20))

	def __init__(self, id, first_name, last_name, email, password, salt):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
		self.salt = salt


class GameTypes(db.Model):
	id = db.Column(db.String(10), primary_key = True)
	name = db.Column(db.String(255))
	description = db.Column(db.Text)
	category = db.Column(db.String(100))

	def __init__(self, id, name, description, category):
		self.id = id
		self.name = name
		self.description = description
		self.category = category


class Games(db.Model):
	id = db.Column(db.String(255), primary_key = True)
	host_id = db.Column(db.String(255), default = "public")
	game_type_id = db.Column(db.String(30))
	num_of_questions = db.Column(db.Integer)
	live_game = db.Column(db.Integer)
	game_created = db.Column(db.DateTime, default = datetime.utcnow)
	join_code = db.Column(db.String(10))

	def __init__(self, id, host_id, game_type_id, num_of_questions, live_game, join_code):
		self.id = id
		self.host_id = host_id
		self.game_type_id = game_type_id
		self.num_of_questions = num_of_questions
		self.live_game = live_game
		self.join_code = join_code

	def json(self):
		current_players = Players.query.filter_by(game_id = self.id).order_by(
			Players.end_time,
			Players.question_number.desc()
		).all()
		return {
			'id' : self.id,
			'host_id' : self.host_id,
			'game_type_id' : self.game_type_id,
			'num_of_questions' : self.num_of_questions,
			'join_code' : self.join_code,
			'players' : [player.json() for player in current_players]
		}


class Questions(db.Model):
	id = db.Column(db.String(255), primary_key = True)
	game_id = db.Column(db.String(255))
	number = db.Column(db.Integer)
	text = db.Column(db.Text)
	answer = db.Column(db.Float)

	def __init__(self, id, game_id, number, text, answer):
		self.id = id
		self.game_id = game_id
		self.number = number
		self.text = text
		self.answer = answer

	def json(self):
		return {
			'text' : self.text
		}


class Players(db.Model):
	id = db.Column(db.String(255), primary_key = True)
	nickname = db.Column(db.String(30))
	game_id = db.Column(db.String(255))
	question_number = db.Column(db.Integer, default = 1)
	start_time = db.Column(db.DateTime, default = datetime.utcnow)
	end_time = db.Column(db.DateTime)

	def __init__(self, id, nickname, game_id):
		self.id = id
		self.nickname = nickname
		self.game_id = game_id

	def current_place(self):
		if self.end_time != None:
			return 'Finished'
		return str(self.question_number)


	def json(self):
		return {
			'id' : self.id,
			'nickname' : self.nickname,
			'current_place' : self.current_place()
		}
