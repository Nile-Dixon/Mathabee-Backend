import requests

#test_one = requests.post("http://localhost:5000/game",json = {
#		'game_type' : 'basic_addition',
#		'number_of_questions' : '10'
#	})

#test_three = requests.post("http://localhost:5000/player",json = {
#		'join_code' : '76561659',
#		'nickname' : 'ndixon'
#	})
#print(test_three.text)

test_five = requests.post('http://localhost:5000/check-answer', json = {
		'player_id' : 'LMggSclrxdLMUlQcHoY3',
		'player_answer' : '8'
	})
print(test_five.text)
#
#test_four = requests.post("http://localhost:5000/get-question", json = {
#		'player_id' : 'LMggSclrxdLMUlQcHoY3'
#	})
#print(test_four.text)
#
#test_two = requests.get("http://localhost:5000/game/CShK79wdvOe7S")
#print(test_two.text)