import random 

def generate_random_string(min_num, max_num):
	char_bank = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
	ret_string = ""
	for x in range(random.randint(min_num, max_num)):
		ret_string += char_bank[random.randint(0, len(char_bank) - 1)]
	return ret_string

def generate_short_code():
	ret_string = ""
	for x in range(8):
		ret_string += str(random.randint(0,9))
	return ret_string
