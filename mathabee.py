import random
from statistics import mean, median
from math import gcd

def create_question(question_type):
	question_bank = {
		'basic_addition' : create_basic_add,
		'advanced_addition' : create_advanced_add,
		'basic_subtraction' : create_basic_subtract,
		'advanced_subtraction' : create_advanced_subtract,
		'basic_multiplication' : create_basic_multiply,
		'advanced_multiplication' : create_advanced_multiply,
		'basic_division' : create_basic_divide,
		'advanced_division' : create_advanced_divide,
		'basic_mixed' : create_basic_mixed,
		'advanced_mixed' : create_advanced_mixed,
		'add_fractions'  : create_add_fractions,
		'subtract_fractions' : create_subtract_fractions,
		'multiply_fractions' : create_multiply_fractions,
		'divide_fractions' : create_divide_fractions,
		'simplify_fractions' : create_simplify_fractions,
		'angles' : create_angles,
		'perimeter' : create_perimeter,
		'area' : create_area,
		'pythagorean' : create_pythagorean,
		'average' : create_average,
		'median' : create_median,
		'range' : create_range,
		'dollars_and_cents' : create_dollars,
		'exponents_and_powers' : create_powers_and_exponents,
		'square_roots' : create_square_roots
	}

	return question_bank[question_type]()

def create_basic_add():
	part_one = random.randint(1,10)
	part_two = random.randint(1,10)
	answer = part_one + part_two

	return {
		'question_text' : 'What is {} plus {}?'.format(part_one, part_two),
		'answer' : '{}'.format(answer)
	}

def create_advanced_add():
	part_one = random.randint(50,500)
	part_two = random.randint(50,500)
	answer = part_one + part_two

	return {
		'question_text' : 'What is {} plus {}?'.format(part_one, part_two),
		'answer' : '{}'.format(answer)
	}

def create_basic_subtract():
	answer = random.randint(1,10)
	part_one = random.randint(1,10)
	part_two = part_one + answer

	return {
		'question_text' : 'What is {} minus {}?'.format(part_two, part_one),
		'answer' : '{}'.format(answer)
	}

def create_advanced_subtract():
	answer = random.randint(1,10)
	part_one = random.randint(1,10)
	part_two = part_one + answer

	return {
		'question_text' : 'What is {} minus {}?'.format(part_two, part_one),
		'answer' : '{}'.format(answer)
	}

def create_basic_multiply():
	part_one = random.randint(1,12)
	part_two = random.randint(1,12)
	answer = part_one * part_two

	return {
		'question_text' : 'What is {} times {}?'.format(part_one, part_two),
		'answer' : '{}'.format(answer)
	}

def create_advanced_multiply():
	part_one = random.randint(10,30)
	part_two = random.randint(10,30)
	answer = part_one * part_two

	return {
		'question_text' : 'What is {} times {}?'.format(part_one, part_two),
		'answer' : '{}'.format(answer)
	}

def create_basic_divide():
	part_one = random.randint(1,12)
	answer = random.randint(1,12)
	part_two = part_one * answer

	return {
		'question_text' : 'What is {} divided by {}?'.format(part_two, part_one),
		'answer' : '{}'.format(answer)
	}

def create_advanced_divide():
	part_one = random.randint(6,22)
	answer = random.randint(17,50)
	part_two = part_one * answer

	return {
		'question_text' : 'What is {} divided by {}?'.format(part_two, part_one),
		'answer' : '{}'.format(answer)
	}

def create_basic_mixed():
	pick = random.randint(0,3)
	if pick == 0:
		return create_basic_add()
	elif pick == 1:
		return create_basic_subtract()
	elif pick == 2:
		return create_basic_multiply()
	else:
		return create_basic_divide()

def create_advanced_mixed():
	pick = random.randint(0,3)
	if pick == 0:
		return create_advanced_add()
	elif pick == 1:
		return create_advanced_subtract()
	elif pick == 2:
		return create_advanced_multiply()
	else:
		return create_advanced_divide()


def create_add_fractions():
	numerator_one = random.randint(2,8)
	numerator_two = random.randint(2,8)

	denominator_one = random.randint(0,4) + numerator_one
	denominator_two = random.randint(0,4) + numerator_two

	if denominator_two == denominator_one:
		denominator_three = denominator_two
		numerator_three = numerator_one + numerator_two
	else:
		denominator_three = denominator_two * denominator_one
		numerator_three = (denominator_two * numerator_one) + (denominator_one * numerator_two)

	simplified_factor = gcd(numerator_three, denominator_three)

	simplified_numerator = int(numerator_three / simplified_factor)
	simplified_denominator = int(denominator_three / simplified_factor)

	return {
		'question_text' : '<sup>{}</sup>&frasl;<sub>{}</sub> plus <sup>{}</sup>&frasl;<sub>{}</sub> equals <sup>X</sup>&frasl;<sub>{}</sub>. What is X?'.format(numerator_one, denominator_one, numerator_two, denominator_two, simplified_denominator),
		'answer' : '{}'.format(simplified_numerator)
	}

def create_subtract_fractions():
	numerator_one = random.randint(2,8)
	numerator_two = random.randint(2,8)

	denominator_one = random.randint(0,4) + numerator_one
	denominator_two = random.randint(0,4) + numerator_two

	if denominator_two == denominator_one:
		denominator_three = denominator_two
		numerator_three = numerator_one + numerator_two
		answer = numerator_three - numerator_two
	else:
		denominator_three = denominator_two * denominator_one
		numerator_three = (denominator_two * numerator_one) + (denominator_one * numerator_two)
		answer = numerator_three - (numerator_two * denominator_one)

	simplified_factor = gcd(answer, denominator_three)

	simplified_numerator = int(answer / simplified_factor)
	simplified_denominator = int(denominator_three / simplified_factor)


	return {
		'question_text' : '<sup>{}</sup>&frasl;<sub>{}</sub> minus <sup>{}</sup>&frasl;<sub>{}</sub> equals <sup>X</sup>&frasl;<sub>{}</sub>. What is X? Do not simplify.'.format(numerator_three, denominator_three, numerator_two, denominator_two, simplified_denominator),
		'answer' : '{}'.format(answer)
	}

def create_multiply_fractions():
	numerator_one = random.randint(2,9)
	numerator_two = random.randint(2,9)

	denominator_one = random.randint(0,4) + numerator_one
	denominator_two = random.randint(0,4) + numerator_two

	numerator_three = numerator_one * numerator_two
	denominator_three = denominator_one * denominator_two

	simplified_factor = gcd(numerator_three, denominator_three)

	simplified_numerator = int(numerator_three / simplified_factor)
	simplified_denominator = int(denominator_three / simplified_factor)

	return {
		'question_text' : '<sup>{}</sup>&frasl;<sub>{}</sub> multiplied by <sup>{}</sup>&frasl;<sub>{}</sub> equals <sup>X</sup>&frasl;<sub>{}</sub>. What is X? Do not simplify.'.format(numerator_one, denominator_one, numerator_two, denominator_two, simplified_denominator),
		'answer' : '{}'.format(simplified_numerator)
	}

def create_divide_fractions():
	numerator_one = random.randint(2,9)
	numerator_two = random.randint(2,9)

	denominator_one = random.randint(0,4) + numerator_one
	denominator_two = random.randint(0,4) + numerator_two

	numerator_three = numerator_one * denominator_two
	denominator_three = numerator_two * denominator_one

	simplified_factor = gcd(numerator_three, denominator_three)

	simplified_numerator = int(numerator_three / simplified_factor)
	simplified_denominator = int(denominator_three / simplified_factor)

	return {
		'question_text' : '<sup>{}</sup>&frasl;<sub>{}</sub> divided by <sup>{}</sup>&frasl;<sub>{}</sub> equals <sup>X</sup>&frasl;<sub>{}</sub>. What is X? Do not simplify.'.format(numerator_one, denominator_one, numerator_two, denominator_two, simplified_denominator),
		'answer' : '{}'.format(simplified_numerator)
	}

def create_simplify_fractions():
	bases = [3,5,7,11,13,17,19,23,29,31,37]
	denominator = bases[random.randint(0,len(bases) - 1)]
	numerator = random.randint(1,denominator - 1)

	factor = random.randint(2,11)

	unsimplified_numerator = numerator * factor
	unsimplified_denominator = denominator * factor

	return {
		'question_text' : 'What would be the numerator of this fraction if simplified: <sup>{}</sup>&frasl;<sub>{}</sub>?'.format(unsimplified_numerator, unsimplified_denominator),
		'answer' : '{}'.format(numerator)
	}

def create_angles():
	question_types = ['complementary','supplementary']
	question_type = question_types[random.randint(0,1)]
	if question_type == "complementary":
		angle_one = random.randint(0,74)
		angle_two = 90 - angle_one

		return {
			'question_text' : 'What is the complementary angle of {} degrees?'.format(angle_one),
			'answer' : '{}'.format(angle_two)
		}
	else:
		angle_one = random.randint(0,176)
		angle_two = 180 - angle_one

		return {
			'question_text' : 'What is the supplementary angle of {} degrees?'.format(angle_one),
			'answer' : '{}'.format(angle_two)
		}

def create_perimeter():
	question_types = ['square','circle','triangle','rectangle']
	question_type = question_types[random.randint(0,3)]
	if question_type == "square":
		side = random.randint(1,20)
		return {
			'question_text' : 'This square has a side length of {} units. What is the perimeter of this shape?'.format(side),
			'answer' : '{}'.format(side * 4)
		}

	elif question_type == "circle":
		radius = random.randint(1,50)
		pi = 3.14
		circumference = 2 * pi * radius

		return {
			'question_text' : 'A circle has a radius of {} units. What is the circumference of that circle? Round to the nearest whole number.'.format(radius),
			'answer' : '{}'.format(round(circumference))
		}

	elif question_type == "triangle":
		length_one = random.randint(1,50)
		length_two = random.randint(1,50)
		length_three = random.randint(max(length_one,length_two), length_one + length_two - 1)

		return {
			'question_text' : 'A triangle has three sides: one of length {} units, one of length {} units, and one of length {} units. What is the perimeter of this triangle?'.format(length_one, length_two, length_three),
			'answer' : '{}'.format(length_one + length_two + length_three)
		}

	else:
		length_one = random.randint(1,50)
		length_two = random.randint(1,50)

		return {
			'question_text' : 'A rectangle has a length of {} units and a width of {} units. What is the perimeter of the rectangle?'.format(length_one, length_two),
			'answer' : '{}'.format(2 * length_one + 2 * length_two)
		}

def create_area():
	question_types = ['square','rectangle','circle','triangle','trapezoid']
	question_type = question_types[random.randint(0,4)]

	if question_type == "square":
		side = random.randint(1,50)
		return {
			'question_text' : 'A square has a side length of {} units. What is the area of the square?'.format(side),
			'answer' : '{}'.format(side * side)
		} 

	elif question_type == "rectangle":
		length = random.randint(1,50)
		width = random.randint(1,50)

		return {
			'question_text' : 'A rectangle has a length of {} units and a width of {} units. What is the area of the rectangle?'.format(length, width),
			'answer' : '{}'.format(length * width)
		}

	elif question_type == "circle":
		radius = random.randint(1,50)
		area = radius * radius * 3.14

		return {
			'question_text' : 'A circle has a radius of {} units. What is the area of the circle? Round to the nearest whole number.'.format(radius),
			'answer' : '{}'.format(round(area))
		}

	elif question_type == "triangle":
		base = random.randint(1,50)
		height = random.randint(1,50)

		return {
			'question_text' : 'A triangle has a base length of {} units and a height of {} units. What is the area of the triange? Round to the nearest whole number.'.format(base, height),
			'answer' : '{}'.format(round(base * height / 2))
		}

	else:
		length_one = random.randint(1,50)
		length_two = random.randint(1,50)
		height = random.randint(1,50)

		area = (length_one + length_two) * height / 2

		return {
			'question_text' : 'A trapezoid has a base length of {} units and {} units and a height of {} units. What is the area of the trapezoid? Round to the nearest whole number.'.format(length_one, length_two, height),
			'answer' : '{}'.format(round(area))
		}

def create_pythagorean():
	list_of_perfect_triangles = [
		[3,4,5],
		[5,12,13],
		[7,24,25],
		[8,15,17],
		[9,40,41],
		[11,60,61],
		[12,35,37],
		[13,84,85],
		[16,63,65],
		[20,21,29],
		[20,99,101],
		[28,45,53],
		[33,56,65],
		[36,77,85]
	]

	perfect_triangle = list_of_perfect_triangles[random.randint(0,len(list_of_perfect_triangles) - 1)]
	scale_factor = random.randint(1,9)

	return {
		'question_text' : 'A person travels north {} miles and travels east {} miles. How far is he from his original starting point?'.format(
			perfect_triangle[0] * scale_factor,
			perfect_triangle[1] * scale_factor,
		),
		'answer' : '{}'.format(perfect_triangle[2] * scale_factor)
	}

def create_average():
	list_of_numbers = []
	for x in range(random.randint(7,13)):
		list_of_numbers.append(random.randint(1,150))

	mean_of_numbers = mean(list_of_numbers)

	return {
		'question_text' : 'Here is a list of numbers: {}. What is the mean? Round to the nearest whole number.'.format(", ".join([str(x) for x in list_of_numbers])),
		'answer' : '{}'.format(round(mean_of_numbers))
	}

def create_median():
	list_of_numbers = []
	for x in range(random.randint(7,13)):
		list_of_numbers.append(random.randint(1,150))

	median_of_numbers = median(list_of_numbers)

	return {
		'question_text' : 'Here is a list of numbers: {}. What is the median? Round to the nearest whole number if necessary.'.format(", ".join([str(x) for x in list_of_numbers])),
		'answer' : '{}'.format(round(median_of_numbers))
	}

def create_range():
	list_of_numbers = []
	for x in range(random.randint(7,13)):
		list_of_numbers.append(random.randint(1,100))

	min_num = min(list_of_numbers)
	max_num = max(list_of_numbers)

	range_num = max_num - min_num

	return {
		'question_text' : 'Here is a list of numbers: {}. What is the range?'.format(", ".join([str(x) for x in list_of_numbers])),
		'answer' : '{}'.format(round(range_num))
	}

def create_dollars():
	number_bills = random.randint(0,3)
	number_quarters = random.randint(0,4)
	number_dimes = random.randint(0,10)
	number_nickels = random.randint(0,20)
	number_pennies = random.randint(0,25)

	total_value = number_bills * 1 + number_quarters * 0.25 + number_dimes * 0.1 + number_nickels * 0.05 + number_pennies * 0.01

	return {
		'question_text' : 'I have {} dollar bills, {} quarters, {} dimes, {} nickels, and {} pennies. How much money do I have?'.format(number_bills,
			number_quarters, number_dimes, number_nickels, number_pennies),
		'answer' : '{}'.format(round(total_value,2))
	}


def create_powers_and_exponents():
	base = random.randint(1,20)
	exponent = random.randint(0,4)

	answer = pow(base, exponent)

	return {
		'question_text' : '{}<sup>{}</sup> equals what?'.format(base, exponent),
		'answer' : '{}'.format(answer)
	}


def create_square_roots():
	base = random.randint(1,20)
	exponent = random.randint(2,3)

	if exponent == 2:
		return {
			'question_text' : 'What is the square root of {}?'.format(base * base),
			'answer' : '{}'.format(base)
		
		}
	else:
		return {
			'question_text' : 'What is the cube root of {}?'.format(base * base * base),
			'answer' : '{}'.format(base)
		}